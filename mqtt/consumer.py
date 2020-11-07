import atexit

import paho.mqtt.client as mqtt
from action import car
import json


class Consumer:

    def on_connect(client, userdata, flags, rc, properties):
        print("Connected with result code " + str(rc))
        client.subscribe("car")

    def on_message(client, userdata, msg):

        d = car.Car
        body = msg.payload.decode()
        topic = msg.topic
        print(topic + ":" + body)
        j = json.loads(body)
        if "forward" == j['action']:
            d.forward(d)
        if "backward" == j['action']:
            d.backward(d)
        if "left" == j['action']:
            d.left(d)
        if "right" == j['action']:
            d.right(d)
        if "clockwise" == j['action']:
            d.clockwise(d)
        if "anticlockwise" == j['action']:
            d.anticlockwise(d)
        if "stop" == j['action']:
            d.stop(d)

    client = mqtt.Client("consumer", None, None, mqtt.MQTTv5, "tcp")
    # client.username_pw_set("admin", "public")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_forever()
