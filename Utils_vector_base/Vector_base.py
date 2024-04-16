import asyncio

from langchain_core.documents import Document
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
from qdrant_client.models import Distance, VectorParams, PointStruct
from langchain_openai import OpenAIEmbeddings


class VectorBase:

    def __init__(self, model="text-embedding-ada-002"):
        load_dotenv()
        self.qdrant_client = QdrantClient(url=os.getenv('QDRANT_URL'))
        self.embeddings = OpenAIEmbeddings(model=model)

    def check_collection_exist(self, collection_name):
        collections = self.qdrant_client.get_collections().collections
        collection = next((collection for collection in collections if collection.name == collection_name), None)
        return collection is not None

    def check_collection_is_empty(self, collection_name):
        if not self.check_collection_exist(collection_name):
            self.qdrant_client.create_collection(collection_name=collection_name,
                                                 vectors_config=VectorParams(size=1536, distance=Distance.COSINE,
                                                                             on_disk=True)
                                                 )
        return self.qdrant_client.get_collection(collection_name).points_count == 0

    def create_embeddings_task(self, documents):
        return [asyncio.create_task(self.embeddings.aembed_query(doc.page_content)) for doc in documents]

    async def upload_vectors(self, collection_name, documents: list[Document]):
        if self.check_collection_is_empty(collection_name):
            vectors = await asyncio.gather(*self.create_embeddings_task(documents))
            points = [PointStruct(id=str(doc.metadata.get('id')),
                                  vector=vectors[idx],
                                  payload=doc.metadata) for idx, doc in enumerate(documents)]
            self.qdrant_client.upload_points(collection_name, points)
