# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import asyncio
import json
import time
from pathlib import Path

import aiohttp
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_community.document_loaders.json_loader import JSONLoader
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain_openai import OpenAI, ChatOpenAI

from AI_devs import authorization, get_task, solution_task

load_dotenv()

about_who_system_template = (
    'Odpowiedz na pytanie kogo dotyczy to zdanie {question}. Zasady###: '
    '-odpowiadaj po polsku '
    '-odpowiedz tylko iminiem osoby,'
    '-odpowiedz bez znaków nowej lini'
    '-w odpowiedzi nie mozea byc "-"'
    'Przyklad### Q:Piotrek lubi wafle A:Piotrek, Q:Czy widziałeś gdzies Marka A:Marek')

answer_question_prompt = 'using context: {context} answer question {question} '


def create_task(informations):
    chat = ChatOpenAI()
    chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(about_who_system_template))
    return [asyncio.create_task(chain.ainvoke({'question': information})) for information in informations]


async def build_data(data_input):
    if not Path('./05_data.json').is_file():
        print("robie zapytanie")
        finished_task = await asyncio.gather(*create_task(data_input))
        documents = [{'page_content': task.get('question'), 'metadata': {'name': task.get('text').strip().strip('-.')}}
                     for task in finished_task]
        with open('05_data.json', 'w') as f:
            json.dump(documents, f, )


def read_file_with_data_about(name):
    loader = json.loads(Path('./05_data.json').read_text())
    print(name)
    return list(filter(lambda o: o.get('metadata').get('name') == name, loader))


def answer_question(question):
    chat = ChatOpenAI()
    chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(about_who_system_template))
    name = chain.invoke({'question': question})
    print(name)
    fixed_name = name.get('text').strip().strip('-.')
    context = read_file_with_data_about(fixed_name)
    answer_chain = LLMChain(llm=chat, prompt=PromptTemplate.from_template(answer_question_prompt))
    answer = answer_chain.invoke({'context': context, 'question': question})
    print(answer)
    return answer.get('text')


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
