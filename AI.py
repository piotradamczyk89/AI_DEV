import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from AI_devs import authorization, get_task, solution_task
from dotenv import load_dotenv
import os
import aiohttp
import time

load_dotenv()
open_AI_moderation = "https://api.openai.com/v1/moderations"


# _______________________________________________________________________
# FIRST TASK
async def first_task(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            response = await solution_task(session, token, task.get('cookie'))
            print(response)


# _______________________________________________________________________
# SECOND TASK
async def moderation_request(session, text):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPEN_AI_KEY')}"
    }
    async with session.post(open_AI_moderation, json={"input": text}, headers=headers) as response:
        moderation_object = await response.json()
        return 1 if moderation_object.get('results')[0].get("flagged") else 0


def get_moderation_task(session, texts):
    tasks = []
    for sentence in texts:
        tasks.append(asyncio.create_task(moderation_request(session, sentence)))
    return tasks


async def moderation_second_task(name):
    session = aiohttp.ClientSession()
    token = await authorization(session, name)
    if token is not None:
        task = await get_task(session, token)
        text_list = task.get('input')
        moderation_tasks = get_moderation_task(session, text_list)
        moderation_responses = await asyncio.gather(*moderation_tasks)
        solution = await solution_task(session, token, moderation_responses)
        print(solution)
    await session.close()


# _______________________________________________________________________
# THIRD TASK

system_template = ('As a {role} who answers the questions ultra-concisely using CONTEXT below and nothing more and '
                   'truthfully says /"don\'t know" when the CONTEXT is not enough to give an answer.'
                   '\n\n\ncontext###{context}###"')
human_template = '{text}'


def create_prompt(text):
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([
        system_message_prompt,
        human_message_prompt,
    ])

    return chat_prompt.format_prompt(
        role="author of the cook book",
        context=('you are writing a cook '
                 'book and you have to wrote '
                 'around 100 word chapter '
                 'about the given topic'),
        text=text
    ).to_messages()


def create_blog_chapter(title):
    chat = ChatOpenAI()
    value = chat.invoke(create_prompt(title))
    return value.content


async def blog(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            titles = task.get('blog')
            chapters = [create_blog_chapter(title) for title in titles]
            print(chapters)
            response = await solution_task(session, token, chapters)
            print(response)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # asyncio.run(first_task("helloapi"))
    # asyncio.run(moderation_second_task("moderation"))
    asyncio.run(blog("blogger"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
