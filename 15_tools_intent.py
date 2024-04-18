import asyncio
import datetime
import json
import time

import aiohttp
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from AI_devs import authorization, get_task, solution_task

putInCalendarSchema = {
    "name": "describe_intention",
    "description": "Decide if user intention is to put sth to the calendar or to to-do list.",
    "parameters": {
        "type": "object",
        "properties": {
            "tool": {
                "type": "string",
                "description": """type has to be either
                -'Calendar' - when users gives any meetings,  special events, remainders, etc. but he gives also (and this is IMPORTANT) date or date-related phrases like tomorrow, in a week, today
                -'ToDo' - when user pass any task to do without any date or date-related phrases like tomorrow, in a week, today, etc."""

            },
            "desc": {
                "type": "string",
                "description": "description of task or element to put to calendar",
            },
            "date": {
                "type": "string",
                "description": "return date only if tool='Calendar', decide about the date using context system message and input from the user. Always use YYYY-MM-DD format for date",
            },

        },
        "required": ['tool', 'desc']
    }
}


def decide_user_intention(question):
    chat = ChatOpenAI(temperature=0, model_name="gpt-4-0613").bind(functions=[putInCalendarSchema])
    system_message = SystemMessage(f"Context$$$ -today is {datetime.date.today()}")
    human_message = HumanMessage(question)
    answer = chat.invoke([human_message, system_message]).additional_kwargs.get('function_call')
    answer['arguments'] = json.loads(answer['arguments'])
    return answer.get('arguments')


async def tools():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "tools")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            print(task.get('question'))
            answer = decide_user_intention(task.get('question'))
            print(answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(tools())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
