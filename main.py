import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_LED_FEED_ID = "dotq-bbc-led"
AIO_TEMP_FEED_ID = "dotq-bbc-temp"
ADAFRUIT_IO_USERNAME = "trangia61"
ADAFRUIT_IO_KEY = "aio_BLbo045OzG8b6QA9MDoMmnsew3Aj"


def connected(client):
    print("Ket noi thanh cong...")
    client.subscribe(AIO_LED_FEED_ID)


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong...")


def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("~~~~~~ Nhan du lieu den LED: " + payload)


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    value = random.randint(0, 100)
    print("Cap nhat nhiet do: ", value)
    client.publish(AIO_TEMP_FEED_ID, value)
    time.sleep(2)
