import paho.mqtt.client as mqtt
from action import demo
import json


class Consumer:

    def on_connect(client, userdata, flags, rc, properties):
        print("Connected with result code " + str(rc))
        client.subscribe("car")

    def on_message(client, userdata, msg):

        d = demo.Demo
        body = msg.payload.decode()
        topic = msg.topic
        print(topic + ":" + body)
        j = json.loads(body)
        if "forward" == j['action']:
            d.forward(d)
        if "backward" == j['action']:
            d.backward(d)
        if "leftward" == j['action']:
            d.leftward(d)
        if "rightward" == j['action']:
            d.rightward(d)
        if "stop" == j['action']:
            d.stop(d)

    client = mqtt.Client("consumer", None, None, mqtt.MQTTv5, "tcp")
    # client.username_pw_set("admin", "public")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_forever()
