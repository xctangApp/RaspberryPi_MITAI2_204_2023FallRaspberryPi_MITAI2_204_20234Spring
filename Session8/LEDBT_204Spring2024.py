#
#      LED Control Program for Android App
#
#In this program, LED will connect to GPIO2 on RPi
#The LED will be turned ON or OFF through Android app
#
#
#Program: LEDBT_204Spring2024.py
#
#Name:
#Date:
#Version: 1.0
#

import socket # import socket library
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 2

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED,0)

#
#start of the main program loop, read commands from android
#decode an control LED
#

Port = 1
MAC = 'AA:AA:AA:AA:AA:AA'
s = socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
s.bind((MAC,Port))
s.listen(1)
client, addr = s.accept()

#Decode the msg

try:
    while True:
        data = client.recv(1024)
        if data.decode('utf-8') == '1':
            GPIO.output(LED, 1)
        elif data.decode('utf-8') == '0':
            GPIO.output(LED, 0)

except KeyboardInterrupt:
    client.close()
    s.close()
    
    




