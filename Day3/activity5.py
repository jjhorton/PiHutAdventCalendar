# Imports
from machine import Pin
import time

# Set up out button name and GPIIO pin Number
redbutton = Pin(3,Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)

#counter setup
count = 0 #start at zero

while True:
    time.sleep(0.2) #short delay
    
    if redbutton.value() == 1:
        count = count -1 
        print(count)
        
    if greenbutton.value() == 1:
        count = count + 1
        print(count)
        