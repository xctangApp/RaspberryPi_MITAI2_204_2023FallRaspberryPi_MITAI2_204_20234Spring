import RPi.GPIO as GPIO #Import GPIO library
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10,GPIO.OUT)

try:
    while True:
        GPIO.output(10, 1) #turn on the LED
        time.sleep(1)
        GPIO.output(10, 0) #turn off the LED
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
