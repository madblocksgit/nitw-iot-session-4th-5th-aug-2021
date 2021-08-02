import serial

ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

def read_from_arduino():
 while True:
  if(ser.inWaiting()>0):
   t=ser.readline().decode('utf-8')
   if(t.startswith('#')):
    t=t.split(',')
    hum=t[1]
    temp=t[2]
    return(hum,temp)
