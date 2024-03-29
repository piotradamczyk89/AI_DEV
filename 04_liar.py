import asyncio
import time

import aiohttp
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from AI_devs import authorization, solution_task, post_task_liar

load_dotenv()

guard_template = ('Check if this answer: "{answer}" is correct for this question: "{question}"'
                  '. Answer with upper case YES / NO')


def guard_rail(question, answer):
    guard_prompt = PromptTemplate.from_template(guard_template)
    chat = ChatOpenAI()
    chain = LLMChain(llm=chat, prompt=guard_prompt)
    combined_input = {"answer": answer, "question": question}
    return chain.invoke(combined_input).get('text')


async def liar(question):
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "liar")
        if token is not None:
            response = await post_task_liar(session, token, question)
            print(response)
            yes_or_no = guard_rail(question, response.get('answer'))
            solution = await solution_task(session, token, yes_or_no)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(liar("Capital of Poland"))
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
