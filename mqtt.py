import time
import random
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "sensor"
AIO_USERNAME = "Afihu"
AIO_KEY = ""


def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

while True:
    print("Updating...")
    usage = random.randint(0,100)
    if usage >= 80: 
        temp = random.randint(70, 90)
        client.publish("sensor.sensor1", temp)
        client.publish("sensor.sensor2", usage)
        client.publish("sensor.sensor3", random.randint(1400,1805))
        time.sleep(15)
    elif (usage < 80) and (usage >= 60): 
        temp = random.randint(40, 68)
        client.publish("sensor.sensor1", temp)
        client.publish("sensor.sensor2", usage)
        client.publish("sensor.sensor3", random.randint(1000,1400))
        time.sleep(8)
    else: 
        temp = random.randint(30, 40)
        client.publish("sensor.sensor1", temp)
        client.publish("sensor.sensor2", usage)
        client.publish("sensor.sensor3", random.randint(300,1000))
        time.sleep(5)
    
while True:
    pass
