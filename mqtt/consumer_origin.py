# import paho.mqtt.client as mqtt
# import time
#
# def on_connect(client, userdata, flags, rc,properties):
#     print("Connected with result code " + str(rc))
#
#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("test/#")
#
# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic + " " + str(msg.payload))
#
# # def __init__(self):
# client = mqtt.Client("python_consumer", None, None, mqtt.MQTTv5, "tcp")
# client.username_pw_set("admin", "public")
# client.on_connect = on_connect
# client.on_message = on_message
#
# client.connect("localhost", 1883, 60)
#
# # Blocking call that processes network traffic, dispatches callbacks and
# # handles reconnecting.
# # Other loop*() functions are available that give a threaded interface and a
# # manual interface.
# client.loop_forever()
#
#     # client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#     # #client = mqtt.Client(client_id, None, None, mqtt.MQTTv311, "tcp")
#     # client = mqtt.Client(client_id)
#     # client.username_pw_set("admin", "public")
#     # client.on_connect = self.on_connect
#     # client.on_message = self.on_message
#     # client.connect("localhost", 1883, 60)
#     # client.loop_forever()
