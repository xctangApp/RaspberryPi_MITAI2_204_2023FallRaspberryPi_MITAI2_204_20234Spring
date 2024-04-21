from flask import Flask,render_template
import RPi.GPIO as GPIO

app=Flask(__name__)

GPIO.setwarnings(False)     #
GPIO.setmode(GPIO.BCM)      #

LED = 10    # LED input from GPIO2

GPIO.setup(LED, GPIO.OUT)   #configure LED as output
GPIO.output(LED, 0)         #turn off LED to start with


@app.route("/<device>/<action>")
def action(device, action):
    actuator = LED
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)    #LED on
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)     #LED off
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0', use_reloader=False)
