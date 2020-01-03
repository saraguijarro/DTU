# -*- coding: utf-8 -*-
import machine
import time
green = machine.Pin(13, machine.Pin.OUT)
orange = machine.Pin(12, machine.Pin.OUT)
red = machine.Pin(27, machine.Pin.OUT)
button = machine.Pin(39, machine.Pin.IN, machine.Pin.PULL_UP)
            
i = 0
while 1==1:
    if button.value() :
        i = (i+1)%3
    if i==0:
        green.value(1)
        orange.value(0)
        red.value(0)
    elif i==1:
        green.value(0)
        orange.value(1)
        red.value(0)
    elif i==2:
        green.value(0)
        orange.value(0)
        red.value(1)
    time.sleep(0.2)