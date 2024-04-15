from langchain_core.documents import Document
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
from qdrant_client.models import Distance, VectorParams, PointStruct
from langchain_openai import OpenAIEmbeddings


class VectorBase:

    def __init__(self, collection_name):
        load_dotenv()
        self.qdrant_client = QdrantClient(url=os.getenv('QDRANT_URL'))
        self.collection_name = collection_name
        self.embeddings = OpenAIEmbeddings()

    def check_collection_exist(self):
        collections = self.qdrant_client.get_collections().collections
        collection = next((collection for collection in collections if collection.name == self.collection_name), None)
        return collection is not None

    def check_collection_is_empty(self):
        if not self.check_collection_exist():
            print("collection not exist")
            self.qdrant_client.create_collection(collection_name=self.collection_name,
                                                 vectors_config=VectorParams(size=1536, distance=Distance.COSINE,
                                                                             on_disk=True)
                                                 )
        return self.qdrant_client.get_collection(self.collection_name).points_count == 0

    def upload_vectors(self, documents: list[Document]):
        if self.check_collection_is_empty():
            points = [PointStruct(id=str(doc.metadata.get('id')),
                                  vector=self.embeddings.embed_query(doc.page_content),
                                  payload=doc.metadata) for doc in documents]
            self.qdrant_client.upload_points(self.collection_name, points)
