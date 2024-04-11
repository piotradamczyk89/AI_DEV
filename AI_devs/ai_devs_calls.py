import asyncio
import time

import aiohttp
from aiohttp import ClientSession
from dotenv import load_dotenv
import os
from retry import retry

authorizationURL = "https://tasks.aidevs.pl/token/{}"
taskURL = "https://tasks.aidevs.pl/task/{}"
taskSolutionURL = "https://tasks.aidevs.pl/answer/{}"
import requests

load_dotenv()


async def authorization(session, task_name):
    response = await session.post(authorizationURL.format(task_name), json={"apikey": os.getenv('KEY_APP')})
    json_object = await response.json()
    return json_object.get('token')


async def get_task(session: ClientSession, token):
    response = None
    try:
        response = await session.get(taskURL.format(token))
        response.raise_for_status()
        return await response.json()
    except aiohttp.ClientResponseError as error:
        if error.status == 429:
            print("error 429 raised")
            await asyncio.sleep(int(response.headers.get('Retry-After')) + 1)
            return await get_task(session, token)
        else:
            return f"Other error occurred: {error}"


async def post_task_liar(session, token, question):
    response = await session.post(taskURL.format(token), data={"question": question})
    return await response.json()


async def solution_task(session, token, answer):
    response = await session.post(taskSolutionURL.format(token), json={"answer": answer})
    return await response.json()
