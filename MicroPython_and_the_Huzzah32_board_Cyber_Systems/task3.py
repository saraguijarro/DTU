# -*- coding: utf-8 -*-
address = 24
temp_reg = 5
res_reg = 8

import machine
import time
i2c = machine.I2C(scl = machine.Pin(22),sda = machine.Pin(23))
off = machine.Pin(39,machine.Pin.IN)
green = machine.Pin(27, machine.Pin.OUT)
orange = machine.Pin(12, machine.Pin.OUT)
red = machine.Pin(13, machine.Pin.OUT)

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

while not off.value():
    temperature = temp_c(i2c.readfrom_mem(address,temp_reg,2))
    if temperature < 26:
        red.value(0)
        orange.value(0)
        green.value(1)
    elif temperature < 27:
        red.value(0)
        orange.value(1)
        green.value(0)
    else:
        red.value(1)
        orange.value(0)
        green.value(0)
    time.sleep(0.1)
    print(temperature)