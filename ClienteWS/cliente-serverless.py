import signal
from websockets.sync.client import connect
import concurrent.futures 
import json
from dht11 import getTH
from datetime import datetime
from savelocal import save_data

#outputFolder = "./metrics/Serverless"
outputFolder = "./metricsLAN/serverless"
workers =10 

#monitor
connection_fails = 0
before_send = datetime.now()
after_send = datetime.now()
times = []

def runClient(worker):
    with connect("wss://01edbb4rx0.execute-api.us-east-2.amazonaws.com/production/") as websocket:
        while True:
            data = getTH()
            data["action"] = "sendData"
            before_send = datetime.now()
            websocket.send(json.dumps(data))
            after_send = datetime.now()
            response =  websocket.recv()
            print(worker,response)
            global times
            times.append((worker,str(before_send),str(after_send),(after_send-before_send).microseconds))
            if len(times) == 500:
                save_data(outputFolder,times)
                times.clear()

def handle_interrupt(signal, frame):
    print("Interrupción detectada. Guardando datos antes de cerrar.")
    save_data(outputFolder,times)
    exit(0)

def main():
    signal.signal(signal.SIGINT, handle_interrupt)
    try:
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
        for i in range(workers):
            pool.submit(runClient,worker=i)
    except Exception as e:
            pool.shutdown(wait=True)
            global times
            save_data(outputFolder,times)

main()
