import Adafruit_DHT
from datetime import datetime

from getmac import get_mac_address as gma
mac = gma()
# Set the sensor type and GPIO pin
sensor = Adafruit_DHT.DHT11
pin = 2  # Change this to the GPIO pin you used for DATA

def getTH():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    data = {"mac":mac,"temp":temperature,"humidity":humidity,"time":datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}
    return data
