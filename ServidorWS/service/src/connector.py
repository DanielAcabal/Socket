import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()
host = os.getenv("HOST")
db = os.getenv("DB")
user = os.getenv("USER")
password = os.getenv("PASSWORD")


def insertar_datos(mac,temperatura, humedad,fecha):
    try:
        # Conectar a la base de datos MySQL
        conexion = mysql.connector.connect(
            host=host,  
            database=db,
            user=user,  
            password=password  
        )

        if conexion.is_connected():
            cursor = conexion.cursor()

            sql_insert_query = """ INSERT INTO temp_hum (MAC,temperature,humidity,read_date)
                                   VALUES (%s, %s,%s,%s)"""

            # Valores a insertar
            valores = (mac,temperatura, humedad,fecha)

            # Ejecutar consulta
            cursor.execute(sql_insert_query, valores)

            # Confirmar cambios en la base de datos
            conexion.commit()

            print("Datos insertados correctamente.")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")
