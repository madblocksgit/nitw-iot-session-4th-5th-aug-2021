# read data from arduino
# send that data to aws iot, public

import serial

# create a serial object
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

def read_from_arduino():
        while True:
                if(ser.inWaiting()>0):
                        t=ser.readline().decode('utf-8')
                        if t.startswith('#'): # t is started with '#' - SOF
                                t=t.split(',')
                                hum=t[1]
                                temp=t[2]
                                return (hum,temp)
