# Bibliotheken laden
from machine import Pin, Timer

# Initialisierung von GPIO25 als Ausgang
led_onboard = Pin(25, Pin.OUT, value=0)

# Initialisierung von GPIO14 als Eingang
btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Taster-Funktion
def on_pressed(timer):
    led_onboard.toggle()
    print('pressed')

# Entprell-Funktion
def btn_debounce(pin):
    # Timer setzen (period in Millisekunden)
    Timer().init(mode=Timer.ONE_SHOT, period=200, callback=on_pressed)

# Taster-Auslösung
btn.irq(handler=btn_debounce, trigger=Pin.IRQ_RISING)