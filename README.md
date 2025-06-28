## Servidor WebSocket

Esta carpeta contiene el código fuente utilizado para las pruebas de diferentes arquitecturas.

### Carpeta [`service`](./ServidorWS/service)

Incluye el código fuente de un servidor WebSocket y su respectiva imagen de Docker para la creación de contenedores.

- En la arquitectura de microservicios se utilizó la imagen de Docker.
- En la arquitectura híbrida se empleó el archivo [`Server.py`](./ServidorWS/service/Server.py) directamente.

### Carpeta [`lambda_function`](./ServidorWS/lambda_function)

Contiene los archivos utilizados en la función [`Lambda`](./ServidorWS/lambda_function/lambda_function.py), la cual es invocada por un API Gateway de tipo WebSocket.

- Esta función fue utilizada en la arquitectura serverless.

Ambas carpetas incluyen un archivo para la conexión a una base de datos MySQL, donde se almacenan las métricas recibidas.

---

## Cliente WebSocket

Aquí se encuentra el código fuente utilizado por el prototipo IoT para el envío de datos a las distintas arquitecturas evaluadas.

- [`dht11.py`](./ClienteWS/dht11.py): Obtiene la información del sensor DHT11 y la retorna como un diccionario.
- [`savelocal.py`](./ClienteWS/savelocal.py): Registra los tiempos de inicio y fin de cada mensaje enviado al servidor WebSocket en un archivo `.csv`.
- [`cliente-hibrido-servidor.py`](./ClienteWS/cliente-hibrido-servidor.py): Utilizado para enviar datos a las arquitecturas de microservicios e híbrida.
- [`cliente-serverless.py`](./ClienteWS/cliente-serverless.py): Utilizado para enviar datos a la arquitectura serverless.