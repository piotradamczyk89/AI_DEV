import asyncio
import os
import uuid

from dotenv import load_dotenv
from langchain_community.document_loaders.text import TextLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import MatchValue
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import Filter, FieldCondition
from qdrant_client.models import PointStruct

COLLECTION_NAME = "AI-dev"
load_dotenv()


async def main():
    qdrant = QdrantClient(url=os.getenv('QDRANT_URL'))
    embeddings = OpenAIEmbeddings()
    query = "Do you know the name of Adam's dog?"
    query_embedded = await embeddings.aembed_query(query)
    collections = qdrant.get_collections().collections
    collection = next((collection for collection in collections if collection.name == COLLECTION_NAME), None)
    print(collection)
    if collection is None:
        qdrant.create_collection(collection_name=COLLECTION_NAME,
                                 vectors_config=VectorParams(size=1536, distance=Distance.COSINE, on_disk=True)
                                 )
    collection_info = qdrant.get_collection(COLLECTION_NAME)

    print("points count: ")
    print(collection_info.points_count)

    if not collection_info.points_count:
        loader = TextLoader("./12_memory.md")
        memory = loader.load()[0]
        documents = [
            Document(page_content=el, metadata={'source': COLLECTION_NAME, 'content': el, 'uuid': uuid.uuid4()}) for el
            in
            memory.page_content.split('\n\n')]
        print('jest uuid: ')
        print(documents[0].metadata.get('uuid'))

        points = [PointStruct(id=str(doc.metadata.get('uuid')),
                              vector=embeddings.embed_documents([doc.page_content])[0],
                              payload=doc.metadata) for doc in documents]

        qdrant.upload_points(COLLECTION_NAME, points=points)

    search = qdrant.search(collection_name=COLLECTION_NAME, query_vector=query_embedded,
                           query_filter=Filter(
                               must=[FieldCondition(key='source', match=MatchValue(value=COLLECTION_NAME))]))
    print(search)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
