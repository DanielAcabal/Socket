#!/usr/bin/env python

import os
import asyncio
import json
from websockets.asyncio.server import serve
from src.connector import insertar_datos
from dotenv import load_dotenv

load_dotenv()
ip = os.getenv("IP")
port = os.getenv("PORT")

async def echo(websocket):
    async for message in websocket:
        try:
            content = json.loads(message)
            insertar_datos(content["mac"],content["temp"],content["humidity"],content["time"])
            await websocket.send(f"Saved{content["time"]}")
        except :
            print("Error")
        #await websocket.send(str(time))

async def main():
    async with serve(echo, ip, port):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())


#uvicorn --workers 5 --ws websockets --host 0.0.0.0 --port 4000 Server2:main