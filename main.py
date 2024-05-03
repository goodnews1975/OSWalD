"""
OSWaLD: V02
Main Program
"""

# Load Settings
from settings import wlan_name, wlan_secret, COUNTRY
 

# Load Library
import network
from ssd1306 import SSD1306_I2C
import machine
import time 

network.country(COUNTRY)

# Initializing display
WIDTH = 128
HEIGHT = 64

i2c = machine.I2C(0, scl = machine.Pin(17), sda = machine.Pin(16), freq=400000)

display = SSD1306_I2C(128, 64, i2c)

def display_clear():
    display.fill(0)
    display.show()    
# End initializing display

# Status-LED
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)

# Funktion: WLAN-Verbindung
def wlanConnect(wlanSSID, wlanPW):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('WLAN-Verbindung herstellen:', wlanSSID)
        wlan.active(True)
        wlan.connect(wlanSSID, wlanPW)
        for i in range(10):
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            led_onboard.toggle()
            print('.', wlan.status())
            time.sleep(1)
    if wlan.isconnected():
        print('WLAN-Verbindung hergestellt')
        led_onboard.on()
        print('WLAN-Status:', wlan.status())
        netConfig = wlan.ifconfig()
        print('IPv4-Adresse:', netConfig[0], '/', netConfig[1])
        print('Standard-Gateway:', netConfig[2])
        print('DNS-Server:', netConfig[3])
    else:
        print('Keine WLAN-Verbindung')
        led_onboard.off()
        print('WLAN-Status:', wlan.status())


# WLAN-Verbindung herstellen
wlanConnect(wlan_name, wlan_secret)
