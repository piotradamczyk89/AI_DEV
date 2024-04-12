from __future__ import unicode_literals
from langchain_core.prompts import ChatPromptTemplate
import asyncio
import time

import aiohttp
import requests
from langchain_openai import ChatOpenAI
from retry import retry

from AI_devs import authorization, solution_task, get_task


@retry(exceptions=requests.exceptions.HTTPError, delay=0.5, tries=100)
def read_html_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, timeout=35)

    response.raise_for_status()

    return response.text


def answer_question(context, question):
    system_prompt = """Using only context: {context} Answer user question in Polisch language.
     -Always skip any additional comments
     -give possible short answer"""
    human_prompt = "{question}"
    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", human_prompt)]).format_prompt(
        context=context, question=question)
    chat = ChatOpenAI()
    return chat.invoke(prompt).content


async def scraper():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "scraper")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            text = read_html_page(task.get('input'))
            answer = answer_question(text, task.get('question'))
            print(answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(scraper())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
