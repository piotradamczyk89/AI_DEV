import asyncio
import json
import time

import aiohttp
import requests
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from AI_devs import authorization, get_task, solution_task

getExchangeRateSchema = {
    "name": "getExchangeRate",
    "description": "Get exchange rate for the given currency",
    "parameters": {
        "type": "object",
        "properties": {
            "argument": {
                "type": "string",
                "description": "Currency code in ISO 4217 standard for the exchange rate",
            }
        },
        "required": [
            "argument"
        ]
    }
}

getCurrentPopulationSchema = {
    "name": "getCurrentPopulation",
    "description": "Get the current population for the given country",
    "parameters": {
        "type": "object",
        "properties": {
            "argument": {
                "type": "string",
                "description": "Country name",
            }
        },
        "required": [
            "argument"
        ]
    }
}

answerWithGeneralKnowledge = {
    "name": "generalKnowledge",
    "description": "General knowledge question",
    "parameters": {
        "type": "object",
        "properties": {
            "argument": {
                "type": "string",
                "description": "human input without any modification or translation",
            }
        },
        "required": [
            "argument"
        ]
    }
}


def define_acton(question):
    chat = ChatOpenAI(temperature=0).bind(
        functions=[getCurrentPopulationSchema, getExchangeRateSchema, answerWithGeneralKnowledge])
    answer = chat.invoke([HumanMessage(question)])
    data = answer.additional_kwargs.get('function_call')
    data['arguments'] = json.loads(data['arguments'])
    return data


def call_make_com_scenario(data):
    try:
        response = requests.post("https://hook.eu2.make.com/x7m4ctjdrj2gqyqooiv2ul2xxlv42krf", json=data)
        response.raise_for_status()
        return response.json().get('answer')
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")


async def knowledge():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "knowledge")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            print(task.get('question'))
            data = define_acton(task.get('question'))
            answer = call_make_com_scenario(data)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(knowledge())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
