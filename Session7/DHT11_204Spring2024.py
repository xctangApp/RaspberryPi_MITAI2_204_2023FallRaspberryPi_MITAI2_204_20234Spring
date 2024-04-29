#sudo pip3 install adafruit-circuitpython-dht

import time
from flask import Flask, render_template
import RPi.GPIO as GPIO
import adafruit_dht
from board import *

# GPIO17
SENSOR_PIN = D17


app = Flask(__name__)

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

@app.route('/', methods=['GET','POST'])
def get_data():
    
    dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)
    temp = dht11.temperature
    hum = dht11.humidity
    tempint = int(temp)
    humint = int(hum)
    if tempint < 10:
        datat = "0" + str(tempint)
    else:
        datat = str(tempint)
    datath = datat + "," + str(humint)
    return(datath)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0',use_reloader=False)
