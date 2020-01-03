# -*- coding: utf-8 -*-

import machine
import time

button = machine.Pin(39, machine.Pin.IN)
led = machine.Pin(13, machine.Pin.OUT)
while True:
    if button.value():
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
    else:
        led.value(0)