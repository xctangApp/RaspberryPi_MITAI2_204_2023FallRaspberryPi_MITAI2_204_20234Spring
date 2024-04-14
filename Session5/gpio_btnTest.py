#test my music box button

from gpiozero import Button

btn = Button(10)

def hello():
    print('hello')
    
btn.when_pressed = hello
