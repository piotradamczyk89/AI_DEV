from dotenv import load_dotenv
import os

authorizationURL = "https://tasks.aidevs.pl/token/{}"
taskURL = "https://tasks.aidevs.pl/task/{}"
taskSolutionURL = "https://tasks.aidevs.pl/answer/{}"

load_dotenv()


async def authorization(session, task_name):
    response = await session.post(authorizationURL.format(task_name), json={"apikey": os.getenv('KEY_APP')})
    json_object = await response.json()
    return json_object.get('token')


async def get_task(session, token):
    response = await session.get(taskURL.format(token))
    return await response.json()


async def post_task_liar(session, token, question):
    response = await session.post(taskURL.format(token), data={"question": question})
    return await response.json()


async def solution_task(session, token, answer):
    response = await session.post(taskSolutionURL.format(token), json={"answer": answer})
    return await response.json()
