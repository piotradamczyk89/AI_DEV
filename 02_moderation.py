import asyncio
import os
import time
import aiohttp
from dotenv import load_dotenv
from AI_devs import authorization, get_task, solution_task

load_dotenv()
open_AI_moderation = "https://api.openai.com/v1/moderations"


async def moderation_request(session, text):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
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
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            text_list = task.get('input')
            moderation_tasks = get_moderation_task(session, text_list)
            moderation_responses = await asyncio.gather(*moderation_tasks)
            solution = await solution_task(session, token, moderation_responses)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(moderation_second_task("moderation"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
