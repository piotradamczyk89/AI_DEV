import asyncio
import time
import aiohttp
from dotenv import load_dotenv

from AI_devs import authorization, get_task, solution_task

load_dotenv()


async def first_task(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            response = await solution_task(session, token, task.get('cookie'))
            print(response)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(first_task("helloapi"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
