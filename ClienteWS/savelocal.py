import csv
from datetime import datetime

format = '%Y%m%d%H%M%S'
def save_data(folder,datos):
    # Abrir o crear un archivo CSV
    with open(f'{folder}/datos_metricas_{datetime.now().strftime(format)}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["worker","Send_time", "Reponse_time", "time(ms)"])
        # Escribir los datos
        writer.writerows(datos)
    print("Cantidad de registros:",len(datos))
    print("Datos guardados exitosamente en datos_pruebas.csv")
