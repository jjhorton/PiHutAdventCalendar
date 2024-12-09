# Imports
from machine import Pin
import time

# Set up out button name and GPIIO pin Number
redbutton = Pin(3,Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)

#LED setup
redled = Pin(14, Pin.OUT)

while True:
    time.sleep(0.2) #short delay
    
    if redbutton.value() == 1:
        print("Light OFF")
        redled.value(0)
        
    if greenbutton.value() == 1:
        print("Light ON")
        redled.value(1)
        