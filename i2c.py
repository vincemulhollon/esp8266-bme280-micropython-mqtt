# i2c.py
# Assumes the catdog2 BME driver has been uploaded via ./ampy
# This script is a good way to test the wiring and I2C operation

import machine
from machine import I2C, Pin

import bme280
from bme280 import BME280

scl = Pin(5)
sda = Pin(4)
i2c = I2C(scl=scl, sda=sda)

bme=BME280(i2c=i2c)
print(bme.values)
print(bme.values[0])
print(bme.values[1])
print(bme.values[2])
