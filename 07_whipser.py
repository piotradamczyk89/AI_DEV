from __future__ import unicode_literals
import asyncio
import time

import aiohttp
from openai import OpenAI

from AI_devs import authorization, solution_task


def convert_to_text():
    file = open("./mateusz.mp3", "rb")
    client = OpenAI()
    result = client.audio.transcriptions.create(model="whisper-1", file=file, response_format="text")
    return result


async def whisper():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "whisper")
        if token is not None:
            answer = convert_to_text()
            print(answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(whisper())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
