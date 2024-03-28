import asyncio

from aiohttp import ClientSession
from dotenv import load_dotenv
import os
import aiohttp
import langchain

load_dotenv()

authorizationURL = "https://tasks.aidevs.pl/token/{}"
taskURL = "https://tasks.aidevs.pl/task/{}"
taskSolutionURL = "https://tasks.aidevs.pl/answer/{}"
open_AI_moderation = "https://api.openai.com/v1/moderations"


async def authorization(session, task_name):
    async with session.post(authorizationURL.format(task_name), json={"apikey": os.getenv('KEY_APP')}) as response:
        json_object = await response.json()
        return json_object.get('token')


async def get_task(session, token):
    async with session.get(taskURL.format(token)) as response:
        return await response.json()


async def solution_task(session, token, answer):
    async with session.post(taskSolutionURL.format(token), json={"answer": answer}) as response:
        return await response.json()


async def first_task(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            response = await solution_task(session, token, task.get('cookie'))
            print(response)


async def moderation_request(session: ClientSession, text):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPEN_AI_KEY')}"
    }
    await session.post(open_AI_moderation, json=text, headers=headers)


async def moderation_second_task(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            print(task)


if __name__ == '__main__':
    asyncio.run(first_task("helloapi"))
    # asyncio.run(moderation_second_task("moderation"))
