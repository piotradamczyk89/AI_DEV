import asyncio
import time

import aiohttp

from AI_devs import authorization, get_task, solution_task



async def proapi():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "ownapipro")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            solution = await solution_task(session, token,
                                           "https://d9nmk18nvb.execute-api.eu-central-1.amazonaws.com/dev/interaction")
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(proapi())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
