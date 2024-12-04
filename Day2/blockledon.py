from machine import Pin

red = Pin(14, Pin.OUT)

red.value(1)

print("Block LED ON!")