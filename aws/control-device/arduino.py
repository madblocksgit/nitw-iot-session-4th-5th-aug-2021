import serial

ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

def send_to_arduino(k):
  print ('Sending Data to Arduino')
  ser.write(k)
