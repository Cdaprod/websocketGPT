import asyncio
import websockets
import openai
import os

openai.api_key = os.environ["API_KEY"]

async def handler(websocket, path):
    data = await websocket.recv()
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=data,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    chat_output = response.choices[0].text.strip()
    await websocket.send(chat_output)

start_server = websockets.serve(handler, "0.0.0.0", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
