import paho.mqtt.client as mqtt

client=mqtt.Client()

while True:
        print('Type On to on the relay')
        print('Type Off to off the relay')
        n=input('Enter Choice: ')
        if (n=="on"):
                client.connect('10.0.0.4',1883)
                client.publish('nit/azure','on')
                print('Data Published')
        elif (n=="off"):
                client.connect('10.0.0.4',1883)
                client.publish('nit/azure','off')
                print('Data Published')
