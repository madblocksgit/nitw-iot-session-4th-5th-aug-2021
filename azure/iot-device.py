import threading
import time
from azure.iot.device import IoTHubDeviceClient
from arduino import send_to_arduino

RECEIVED_MESSAGES = 0

CONNECTION_STRING="" # Device Connection String

def message_listener(client):
    global RECEIVED_MESSAGES
    while True:
        message = client.receive_message()
        RECEIVED_MESSAGES += 1
        print("\nMessage received:")
        send_to_arduino(message)

        print( "Total calls received: {}".format(RECEIVED_MESSAGES))
        print()

def iothub_client_sample_run():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        message_listener_thread = threading.Thread(target=message_listener, args=(client,))
        message_listener_thread.daemon = True
        message_listener_thread.start()

        while True:
            time.sleep(1000)

    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging device sample stopped" )

if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging device sample..." )
    print ( "Waiting for C2D messages, press Ctrl-C to exit" )

    iothub_client_sample_run()
