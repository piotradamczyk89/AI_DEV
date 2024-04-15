import asyncio
import time
import uuid

import aiohttp
from langchain_core.documents import Document
from qdrant_client.grpc import ScoredPoint

from AI_devs import authorization, get_task, solution_task
from Utils_vector_base import VectorBase
from Utlis_data import get_data

URL_COLLECTION_NAME = 'url'
base = VectorBase(URL_COLLECTION_NAME)


def prepare_documents(data):
    return [Document(page_content='\n'.join([el.get('title'), el.get('info')]),
                     metadata={'id': uuid.uuid4(),
                               'title': el.get('title'),
                               'url': el.get('url'),
                               'info': el.get('info'),
                               'date': el.get('date'),
                               'collection': URL_COLLECTION_NAME}) for el in data]


async def get_url_for_question(question):
    query = await base.embeddings.aembed_query(question)
    result: ScoredPoint = base.qdrant_client.search(collection_name=URL_COLLECTION_NAME, query_vector=query, limit=1)[0]
    return result.payload.get('url')


async def search():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "search")
        if token is not None:
            task = await get_task(session, token)
            base.upload_vectors(prepare_documents(get_data("https://unknow.news/archiwum_aidevs.json")))
            answer = await get_url_for_question(task.get('question'))
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(search())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
