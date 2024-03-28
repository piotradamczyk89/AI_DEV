import asyncio
from dotenv import load_dotenv
import os
import aiohttp
import langchain
import time

load_dotenv()

authorizationURL = "https://tasks.aidevs.pl/token/{}"
taskURL = "https://tasks.aidevs.pl/task/{}"
taskSolutionURL = "https://tasks.aidevs.pl/answer/{}"
open_AI_moderation = "https://api.openai.com/v1/moderations"


async def authorization(session, task_name):
    response = await session.post(authorizationURL.format(task_name), json={"apikey": os.getenv('KEY_APP')})
    json_object = await response.json()
    return json_object.get('token')


async def get_task(session, token):
    response = await session.get(taskURL.format(token))
    return await response.json()


async def solution_task(session, token, answer):
    response = await session.post(taskSolutionURL.format(token), json={"answer": answer})
    return await response.json()


async def first_task(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            response = await solution_task(session, token, task.get('cookie'))
            print(response)


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


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # asyncio.run(first_task("helloapi"))
    asyncio.run(moderation_second_task("moderation"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
