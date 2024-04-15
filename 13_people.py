import asyncio
import os
import time
import uuid
import aiohttp
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.grpc import ScoredPoint
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct

from AI_devs import authorization, get_task, solution_task
from Utlis_data import get_data

PEOPLE_COLLECTION_NAME = 'people'
CATEGORY_COLLECTION_NAME = 'category'


async def people():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "people")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            # answer = await get_url_for_question(task.get('question'))
            # solution = await solution_task(session, token, answer)
            # print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(people())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
