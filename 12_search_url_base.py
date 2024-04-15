import asyncio
import os
import time
import uuid

import aiohttp
import requests
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.grpc import ScoredPoint
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct

from AI_devs import authorization, get_task, solution_task

URL_COLLECTION_NAME = 'url'
load_dotenv()
qdrant_client = QdrantClient(url=os.getenv('QDRANT_URL'))
embeddings = OpenAIEmbeddings()


def get_url_archive():
    try:
        response = requests.get("https://unknow.news/archiwum_aidevs.json")
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")


def prepare_documents(data):
    return [Document(page_content='\n'.join([el.get('title'), el.get('info')]),
                     metadata={'id': uuid.uuid4(),
                               'title': el.get('title'),
                               'url': el.get('url'),
                               'info': el.get('info'),
                               'date': el.get('date'),
                               'collection': URL_COLLECTION_NAME}) for el in data]


def check_collection_exist(collection_name):
    collections = qdrant_client.get_collections().collections
    collection = next((collection for collection in collections if collection.name == collection_name), None)
    return collection is not None


def check_collection_is_empty():
    if not check_collection_exist(URL_COLLECTION_NAME):
        print("collection not exist")
        qdrant_client.create_collection(collection_name=URL_COLLECTION_NAME,
                                        vectors_config=VectorParams(size=1536, distance=Distance.COSINE, on_disk=True)
                                        )
    return qdrant_client.get_collection(URL_COLLECTION_NAME).points_count == 0


def upload_vectors():
    if check_collection_is_empty():
        rough_data = get_url_archive()
        documents = prepare_documents(rough_data)
        points = [PointStruct(id=str(doc.metadata.get('id')),
                              vector=embeddings.embed_query(doc.page_content),
                              payload=doc.metadata) for doc in documents]
        qdrant_client.upload_points(URL_COLLECTION_NAME, points)


async def get_url_for_question(question):
    query = await embeddings.aembed_query(question)
    result: ScoredPoint = qdrant_client.search(collection_name=URL_COLLECTION_NAME, query_vector=query, limit=1)[0]
    return result.payload.get('url')


async def search():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "search")
        if token is not None:
            task = await get_task(session, token)
            upload_vectors()
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
