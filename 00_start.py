import asyncio
import time

import aiohttp

from AI_devs import authorization, get_task, solution_task


async def example():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "example")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            print(task.get('question'))
            answer = "sth"
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(example())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
