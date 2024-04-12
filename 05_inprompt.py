# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import asyncio
import json
import time
from pathlib import Path

import aiohttp
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.documents import Document
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from AI_devs import authorization, get_task, solution_task
from Utlis_data import document_from_json
from langchain_community.vectorstores import Chroma

load_dotenv()

system_template = """Return name from the input
Rules###
-Return only name
-Do not put any special characters like "-" or new line sign 

Examples###
Q:Piotrek lubi wafle
A:Piotrek
 
Q:Czy widziałeś gdzies Marka?
A:Marek

Q:Ulubion zajęcie Karola to bieganie
A:Karol
"""

human_template = "{data}"

system_template_2 = 'using only context: {context} answer question '
human_template_2 = "{question}"


def create_task(informations):
    chat = ChatOpenAI()
    chain = LLMChain(llm=chat,
                     prompt=ChatPromptTemplate.from_messages([("system", system_template), ("human", human_template)]))
    return [asyncio.create_task(chain.ainvoke({'data': information})) for information in informations]


async def build_data(data_input):
    if not Path('./05_data.json').is_file():
        finished_task = await asyncio.gather(*create_task(data_input))

        # {'page_content': task.get('data'), 'metadata': }{'name': task.get('text')}
        documents = [Document(page_content=task.get('data'), metadata={'name': task.get('text')})
                     for task in finished_task]

        with open('05_data.json', 'w') as f:
            json.dump([doc.to_json() for doc in documents], f, )


def read_file_with_data():
    return [document_from_json(json_object) for json_object in json.loads(Path('./05_data.json').read_text())]


def filer_data_with_metadata(data, name):
    return list(filter(lambda o: o.metadata.get('name') == name, data))


def similarity_search_from_data(data, question):
    db = Chroma.from_documents(data, OpenAIEmbeddings())
    doc = db.similarity_search(question, 1)
    return doc


def answer_question_with_metadata_approach(question):
    chat = ChatOpenAI()
    name = chat.invoke(
        ChatPromptTemplate.from_messages([("system", system_template), ("human", human_template)]).format_messages(
            data=question))

    data = read_file_with_data()
    context = filer_data_with_metadata(data, name.content)
    answer = chat.invoke(
        ChatPromptTemplate.from_messages([("system", system_template_2), ("human", human_template_2)]).format_messages(
            context=[singleContext.page_content for singleContext in context],
            question=question))
    return answer.content


def answer_question_with_vector_base(question):
    chat = ChatOpenAI()
    data = read_file_with_data()
    context = similarity_search_from_data(data, question)
    answer = chat.invoke(
        ChatPromptTemplate.from_messages([("system", system_template_2), ("human", human_template_2)]).format_messages(
            context=[singleContext.page_content for singleContext in context],
            question=question))
    return answer.content


async def inprompt(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            await build_data(task.get('input'))
            # answer = answer_question_with_metadata_approach(task.get('question'))
            answer2 = answer_question_with_vector_base(task.get('question'))
            # solution = await solution_task(session, token, answer)
            solution2 = await solution_task(session, token, answer2)
            print(solution2)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(inprompt("inprompt"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
