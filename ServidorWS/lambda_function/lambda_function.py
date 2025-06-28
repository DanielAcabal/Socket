import json
import urllib3
import boto3
import os

from connector import insertar_datos

api_gateway = os.environ['API_GATEWAY']
client = boto3.client('apigatewaymanagementapi', endpoint_url=api_gateway)


def lambda_handler(event, context):
    connectionId = event['requestContext']['connectionId']
    print(event)
    try:
        body = json.loads(event["body"])
        mac = body['mac']
        temp = body['temp']
        humidity = body['humidity']
        time = body['time']
        insertar_datos(mac,temp,humidity,time)

        client.post_to_connection(ConnectionId=connectionId, Data=json.dumps("DataSaved").encode('utf-8'))
    except Exception as e:
        print(e)
        client.post_to_connection(ConnectionId=connectionId, Data=json.dumps("Error:"+str(e)).encode('utf-8'))
   
    return { "statusCode": 200  }
