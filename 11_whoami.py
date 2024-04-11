# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import asyncio
import time

import aiohttp
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
)
from langchain_openai import ChatOpenAI

from AI_devs import authorization, get_task, solution_task

system_message = """"
Role$$$
you have to tell me if you know the person base of the hints from contex

Contex$$$
{hints}

Rules$$$
- if you certain that you know the person return only person name if not return only 0 and nothing more
- using your best guess to be sure you've got the right answer.
- IMPORTANT: you are allowed to return 0 only or person name only
- IMPORTANT: if more than one person fit to the hints return 0

Examples$$$
Hints:like honey
A:0

Hints: like honey, is a bear
A:0

Hints: like honey, is a bear, have a pig as a friend
A:Winnie The Pooh

"""

system_check_messages = """
Role$$$
You are a veryfier and you have to tell me if hints from the cotext pass to the person from human querry
"""
hints = []


def guess_person():
    chat = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([("system", system_message)])
    answer = chat.invoke(prompt.format_prompt(hints="".join(hints)))
    return answer.content


async def whoami():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "whoami")
        if token is not None:
            while True:
                task = await get_task(session, token)
                hints.append(task.get('hint'))
                print("hint is --->>>> " + ', '.join(hints))
                answer = guess_person()
                if "0" not in answer:
                    break
            print("Answer is--->>>>  " + answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(whoami())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
