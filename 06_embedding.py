from __future__ import unicode_literals

import asyncio
import time

import aiohttp
from langchain_openai import OpenAIEmbeddings

from AI_devs import authorization, solution_task


async def call_embedding():
    embeddings_model = OpenAIEmbeddings()
    result = await embeddings_model.aembed_query("Hawaiian pizza")
    return result


async def embedding():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "embedding")
        if token is not None:
            result = await call_embedding()
            solution = await solution_task(session, token, result[:1536])
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(embedding())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
