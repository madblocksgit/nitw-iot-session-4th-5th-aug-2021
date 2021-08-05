import paho.mqtt.client as mqtt
from pymongo import MongoClient

db_client=MongoClient('127.0.0.1',27017)
db=db_client['nitw']
c=db['dht11']

client=mqtt.Client()
client.connect('10.0.0.4',1883)
print('Broker Connected')
client.subscribe('nit/azure')

def notification(client,userdata,msg):
        t=msg.payload.decode('utf-8').split(':')
        humi=t[1].split("'")
        humi=humi[1]
        temp=t[-1][:-1]
        temp=temp[2:-1]
        humi,temp=temp,humi
        print(humi,temp)
        k={}
        k['humidity']=float(humi)
        k['temperature']=float(temp)
        c.insert_one(k) # insert data into mongodb
client.on_message=notification
client.loop_forever()

