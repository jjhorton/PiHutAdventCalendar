from machine import ADC, Pin
import time

potentiometer = ADC(Pin(28))

while True:
    print(potentiometer.read_u16())
    time.sleep(0.3)