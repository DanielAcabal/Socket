import websockets
import json
import os
import asyncio
import threading
from src.connector import insertar_datos
from dotenv import load_dotenv

load_dotenv()
ip = os.getenv("IP")
port = os.getenv("PORT")

async def handler(websocket, path):
    data = await websocket.recv()
    content = json.loads(data)
    insertar_datos(content["mac"],content["temp"],content["humidity"],content["time"])
    print(data)
    reply = f"Data recieved!"+data
    await websocket.send(reply)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    ws_server = websockets.serve(handler, ip, port)

    loop.run_until_complete(ws_server)
    loop.run_forever() 
    loop.close()

if __name__ == "__main__":
    _thread = threading.Thread(target=main)
    _thread.start()