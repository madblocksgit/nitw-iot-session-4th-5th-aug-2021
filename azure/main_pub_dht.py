import paho.mqtt.client as mqtt
from dhtarduino import read_from_arduino
client=mqtt.Client()

while True:
        h,t=read_from_arduino()
        payload={}
        payload["temperature"]=str(t)
        payload["humidity"]=str(h)
        client.connect('20.51.192.94',1883)
        client.publish('nit/azure',str(payload))
        print('Data published')
