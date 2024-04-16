import asyncio
import time
import uuid
from enum import Enum

import aiohttp
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from AI_devs import authorization, get_task, solution_task
from Utils_vector_base import VectorBase
from Utlis_data import get_data

PEOPLE_COLLECTION_NAME = 'people'
CATEGORY_COLLECTION_NAME = 'category'
base = VectorBase()


class Category(Enum):
    kolor = 1
    jedzenie = 2
    mieszkanie = 3


def prepare_documents(data):
    doc = [Document(page_content=' '.join([el.get('imie'), el.get('nazwisko')]),
                    metadata={'id': uuid.uuid4(),
                              'imie': el.get('imie'),
                              'nazwisko': el.get('nazwisko'),
                              'wiek': el.get('wiek'),
                              'o_mnie': el.get('o_mnie'),
                              'ulubiona_postac_z_kapitana_bomby': el.get('ulubiona_postac_z_kapitana_bomby'),
                              'ulubiony_serial': el.get('ulubiony_serial'),
                              'ulubiony_film': el.get('ulubiony_film'),
                              'ulubiony_kolor': el.get('ulubiony_kolor'),
                              'collection': PEOPLE_COLLECTION_NAME}) for el in data]
    return doc


def prepare_category():
    return [Document(page_content=el.name, metadata={'id': uuid.uuid4(),
                                                     'kategoria': el.name}) for el in Category]


def answer_question(context, question):
    system_message = """Using only context, with your best guess, as short as possible answer user question
    Context$$$: {context}"""
    human_message = "{question}"
    chat = ChatOpenAI()
    answer = chat.invoke(
        ChatPromptTemplate.from_messages([("system", system_message), ("human", human_message)]).format_prompt(
            context=context, question=question))
    return answer.content


def create_context(human_data, category):
    if category == Category.kolor.name:
        return "ulubiony kolor to " + human_data.payload.get('ulubiony_kolor')
    else:
        return human_data.payload.get('o_mnie')


async def people():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "people")
        if token is not None:
            task = await get_task(session, token)
            print(task.get('question'))
            documents = prepare_documents(get_data("https://tasks.aidevs.pl/data/people.json"))
            await base.upload_vectors(PEOPLE_COLLECTION_NAME, documents)
            await base.upload_vectors(CATEGORY_COLLECTION_NAME, prepare_category())
            embedded_question = base.embeddings.embed_query(task.get('question'))
            human = base.qdrant_client.search(collection_name=PEOPLE_COLLECTION_NAME, query_vector=embedded_question,
                                              limit=1)[0]
            category = base.qdrant_client.search(collection_name=CATEGORY_COLLECTION_NAME,
                                                 query_vector=embedded_question, limit=1)[0]
            print(category)
            answer = answer_question(create_context(human, category.payload.get('kategoria')), task.get('question'))
            print(answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(people())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
