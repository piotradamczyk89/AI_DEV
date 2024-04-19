import asyncio
import time

import aiohttp

from AI_devs import authorization, get_task, solution_task

from openai import OpenAI


def explain_image(image):
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": """I will give you a drawing of a gnome with a hat on his head. Return ONLY the color of the hat in POLISH. If there will be no gnome hat on the image return 'ERROR'"""},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content


async def gnome():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "gnome")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            answer = explain_image(task.get('url'))
            print(answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(gnome())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
