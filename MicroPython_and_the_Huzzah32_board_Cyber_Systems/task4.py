# -*- coding: utf-8 -*-

import machine
import time
import neopixel
address = 24
temp_reg = 5
res_reg = 8

i2c = machine.I2C(scl = machine.Pin(22),sda = machine.Pin(23))
off = machine.Pin(39,machine.Pin.IN)
np = neopixel.NeoPixel(machine.Pin(27),3)

def green(neopixel):
    neopixel[0] = (255,0,0)
    neopixel[1] = (255,0,0)
    neopixel[2] = (255,0,0)
    np.write()
def yellow(neopixel):
    neopixel[0] = (255,255,0)
    neopixel[1] = (255,255,0)
    neopixel[2] = (255,255,0)
    np.write()
def red(neopixel):
    neopixel[0] = (0,255,0)
    neopixel[1] = (0,255,0)
    neopixel[2] = (0,255,0)
    np.write()

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

while not off.value():
    temperature = temp_c(i2c.readfrom_mem(address,temp_reg,2))
    if temperature < 26:
        green(np)
    elif temperature < 27:
        yellow(np)
    else:
        red(np)
    time.sleep(0.1)
    print(temperature)