import asyncio
import websockets
import json
import os
from src.connector import insertar_datos
from dotenv import load_dotenv

load_dotenv()
ip = os.getenv("IP")
port = os.getenv("PORT")


# create handler for each connection
async def handler(websocket, path):
    data = await websocket.recv()
    content = json.loads(data)
    insertar_datos(content["mac"],content["temp"],content["humidity"],content["time"])
    reply = f"Data recieved!"
    #print(ServerConnection.latency)
    await websocket.send(reply)

start_server = websockets.serve(handler, ip, port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()