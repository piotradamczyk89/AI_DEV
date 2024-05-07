import json
import os
import asyncio
import time
import aiohttp
from openapi_client import RenderRequest

from AI_devs import authorization, get_task, solution_task
import openapi_client
from dotenv.main import load_dotenv
from openapi_client.rest import ApiException
from pprint import pprint

load_dotenv()

json_data = """
{
  "template": "evil-geese-scratch-blindly-1221",
  "data": {
    "TEXT": {
      "text": "Gdy koledzy z pracy mówią, że ta cała automatyzacja to tylko chwilowa moda, a Ty właśnie zastąpiłeś ich jednym, prostym skryptem"
    },
    "IMAGE": {
      "src": "https://tasks.aidevs.pl/data/monkey.png"
    }
  }
}
"""


def generate_meme(image, text):
    configuration = openapi_client.Configuration(
        host="https://api.renderform.io"
    )
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.RenderAPIApi(api_client)
        try:
            api_response = api_instance.render_v2(x_api_key=os.getenv('RENDERFORM_API'),
                                                  render_request=RenderRequest.parse_raw(json_data))
            return api_response.to_dict().get('href')
        except ApiException as e:
            print("Exception when calling RenderAPI: %s\n" % e)


async def meme():
    async with aiohttp.ClientSession() as session:
        token = await authorization(session, "meme")
        if token is not None:
            task = await get_task(session, token)
            print(task)
            answer = generate_meme(task['image'], task['text'])
            print(answer)
            solution = await solution_task(session, token, answer)
            print(solution)


if __name__ == '__main__':
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(meme())
    end = time.time()
    total_time = end - start
    print(f"total time {total_time}")
