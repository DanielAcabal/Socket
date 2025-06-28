import signal
from websockets.sync.client import connect
import concurrent.futures 
import json
from dht11 import getTH
from datetime import datetime
from savelocal import save_data

outputFolder = "./metricsLAN/service"
#outputFolder = "./metrics/hibrido"
workers =10 

#monitor
connection_fails = 0
before_send = datetime.now()
after_send = datetime.now()
times = []

def hello(worker):
    #with connect("ws://192.168.0.12:4000") as websocket:
    with connect("ws://3.140.249.160:4000") as websocket:
        while True:
            data = getTH()
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

# Funcion para manejar la interrupcion
def handle_interrupt(signal, frame):
    print("Interrupción detectada. Guardando datos antes de cerrar.")
    save_data(outputFolder,times)
    exit(0)

def main():
    # Configurar el manejador de señal para Ctrl + C
    signal.signal(signal.SIGINT, handle_interrupt)
    try:
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
        for i in range(workers):
            pool.submit(hello,worker=i)
    except Exception as e:
            pool.shutdown(wait=True)
            global times
            save_data(outputFolder,times)

main()
