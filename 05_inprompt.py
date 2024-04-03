# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import asyncio
import json
import time
from pathlib import Path

import aiohttp
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
)
from langchain_openai import ChatOpenAI

from AI_devs import authorization, get_task, solution_task

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
        documents = [{'page_content': task.get('data'), 'metadata': {'name': task.get('text')}}
                     for task in finished_task]
        with open('05_data.json', 'w') as f:
            json.dump(documents, f, )


def read_file_with_data_about(name):
    loader = json.loads(Path('./05_data.json').read_text())
    return list(filter(lambda o: o.get('metadata').get('name') == name, loader))


def answer_question(question):
    chat = ChatOpenAI()
    name = chat.invoke(
        ChatPromptTemplate.from_messages([("system", system_template), ("human", human_template)]).format_messages(
            data=question))
    context = read_file_with_data_about(name.content)
    answer = chat.invoke(
        ChatPromptTemplate.from_messages([("system", system_template_2), ("human", human_template_2)]).format_messages(
            context=[singleContext.get('page_content') for singleContext in context],
            question=question))
    return answer.content


async def inprompt(name):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, name)
        if token is not None:
            task = await get_task(session, token)
            await build_data(task.get('input'))
            answer = answer_question(task.get('question'))
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(inprompt("inprompt"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
