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
    print(data)
    reply = f"Data recieved!"+data
    #print(ServerConnection.latency)
    #await asyncio.sleep(2)
    await websocket.send(reply)

def main():
    #asyncio.get_event_loop().run_until_complete(start_server)
    start_server = websockets.serve(handler, ip, port)
    #asyncio.get_event_loop().run_forever()