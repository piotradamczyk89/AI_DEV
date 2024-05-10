import asyncio
import json
import time

import aiohttp
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from AI_devs import authorization, get_task, solution_task
from Utlis_data import get_data

system_template = """
Rules###
Transform human input into string that contains the same information, but around 80% less words. Focus on facts. 
IMPORTNAT all informations are about {name} so do not mention this person in your response use subjectless sentences

ommit interpunction

Examples###
Q:Piotrek w wolnej chwili lubi chodzić z psem 
A:chodzi z psem

Q: Ulubinym instrumentem Piotra jest ukolelea oraz piekny gramfon
A: ulubiony instrument: gramfon ukulele
 
Q:Marek mieszka głównie w  pięknym Krakowie ale czasmi tez w pobliskiej Łodzi a nie rzadko w zielonych Katowicach do których mimio wszysko ma najdalej. W katowicach mieksza dlatego ze odnajduje tam spokój
A:mieszka w Krakowie Łodzi Katowicach

Q:Pawel wygral konkurs na najlepszego java developera 
A:wygrał konkurs java developera

Q:Ulubiona aplikacja Zygfryda to Clash of the titans
A:ulubiona aplikacja Clash of the titans

Q:Aplikacja mobilna "don't" Zykfryda wygrywa konkursy
A:don't wygrywa konkursy

Q: andrzej potrafi wycisnąć sztangę o masie równającej się jego ciężarowi
A: wyciska swoja mase na sztandze



"""

human_template = "{data}"


def create_task(person_information, person):
    chat = ChatOpenAI()
    concatenated_groups = [", ".join(person_information[i:i + 8]) for i in range(0, len(person_information), 8)]

    return [asyncio.create_task(chat.ainvoke(
        ChatPromptTemplate.from_messages([("system", system_template), ("human", human_template)]).format_prompt(
            data=information, name=person))) for information in concatenated_groups]


async def create_optimized_database(data_base):
    new_db = {}
    for name in data_base.keys():
        records = [answer.content for answer in await asyncio.gather(*create_task(data_base.get(name), name))]
        print(records)
        new_db[name] = records
    return json.dumps(new_db)


async def optimaldb():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "optimaldb")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            answer = await create_optimized_database(get_data(task.get('database')))
            print(answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(optimaldb())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
