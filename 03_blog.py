import asyncio
import time
import aiohttp
from dotenv import load_dotenv
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import OpenAI


from AI_devs import authorization, get_task, solution_task

load_dotenv()


system_template = ('As a {role} who answers the questions ultra-concisely .'

                   '\n\n\n context###{context}###"')
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
                 'about the given topic in Polish'),
        text=text
    ).to_messages()



def create_blog_chapter(titles):
    chat = OpenAI()
    return [asyncio.create_task(chat.ainvoke(title)) for title in titles]



async def blog(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            titles = task.get('blog')

            finished_tasks = await asyncio.gather(*create_blog_chapter(titles))
            response = await solution_task(session, token, finished_tasks)

            print(response)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(blog("blogger"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
