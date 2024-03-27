"""
OSWaLD: V02
Main Program
"""

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from picozero import Button,LED, pico_led
import framebuf
import time


# Initializing display
WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)

display = SSD1306_I2C(128, 64, i2c)

def display_clear():
    display.fill(0)
    display.show()    
# End initializing display

# Initialisierung von GPIO0 als Eingang
btn = Pin(0, Pin.IN, Pin.PULL_DOWN)

# Initialisierung von GPIO25 als Ausgang
led_onboard = Pin(25, Pin.OUT)


display.text("Starting up....",0,0)
display.show()
time.sleep(2)
display_clear()

# Funktion zur Taster-Auswertung
while True:
    if btn.value() == 0:
        led_onboard.on()
    else:
        led_onboard.off()