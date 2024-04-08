from __future__ import unicode_literals

import asyncio
import time

import aiohttp

from AI_devs import authorization, solution_task, get_task

add_user ={
    "name": "addUser",
    "description": "Add users ",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "User name",
            },
            "surname": {
                "type": "string",
                "description": "User surname",
            },
            "year": {
                "type": "integer",
                "description": "How many years has the user",
            }
        }
    }
}


async def function_calling():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "functions")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            solution = await solution_task(session, token, add_user)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(function_calling())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
