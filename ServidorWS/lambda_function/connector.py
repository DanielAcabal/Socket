import pymysql
import os

# Configuración de la base de datos
user_name = os.environ['USER_NAME']
password = os.environ['PASSWORD']
rds_host = os.environ['RDS_HOST']
db_name = os.environ['DB_NAME']

def insertar_datos(mac, temperatura, humedad, fecha):
    try:
        # Conectar a la base de datos MySQL usando pymysql
        conexion = pymysql.connect(
            host=rds_host,
            user=user_name,
            password=password,
            database=db_name,
            charset='utf8mb4'  
        )
        
        with conexion.cursor() as cursor:
            # Consulta para insertar datos
            sql_insert_query = """INSERT INTO temp_hum (MAC, temperature, humidity, read_date)
                                  VALUES (%s, %s, %s, %s)"""
            valores = (mac, temperatura, humedad, fecha)
            
            # Ejecutar consulta
            cursor.execute(sql_insert_query, valores)
            conexion.commit()  # Confirmar cambios

            print("Datos insertados correctamente.")

    except pymysql.MySQLError as e:
        print(f"Error al conectar a MySQL: {e}")
    
    finally:
        conexion.close()  # Cerrar conexión
        print("Conexión cerrada.")
