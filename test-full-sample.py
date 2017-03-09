# test-full.py
#
# Full test of a sensor sample and MQTT publish.
#
# Normally would run with "ampy run" but if uploaded as filename main.py it'll run in production
#

import network
import time
import gc

from umqtt.robust import MQTTClient

import machine
from machine import I2C, Pin

import bme280
from bme280 import BME280

MqttClient = "name" # Perhaps "office-bme280"
MqttUrl = "mqtt.server.host.name" # Perhaps "rabbitmq.example.com"
MqttUsername = "YourLoginName" # Your MQTT login name perhaps "office-bme280"
MqttPassword = "12345678901234567890123456789012" # Your MQTT AIO key.  Perhaps 32 hexadecimal digits
location = "office" # sensor location perhaps "office"

scl = Pin(5)
sda = Pin(4)
i2c = I2C(scl=scl, sda=sda)

led = machine.Pin(16, machine.Pin.OUT)

connection = MQTTClient(MqttClient, MqttUrl, 0, MqttUsername, MqttPassword)
connection.connect()

while True:

    led.low()

    bme=BME280(i2c=i2c)
    temperature = bme.values[0]
    humidity = bme.values[2]
    pressure = bme.values[1]
    ipaddress = sta_if.ifconfig()[0]

    connection.publish("home/" + location + "/temperature", str(temperature), qos=1)
    connection.publish("home/" + location + "/humidity", str(humidity), qos=1)
    connection.publish("home/" + location + "/pressure", str(pressure), qos=1)
    connection.publish("sensor/" + MqttUsername + "/temperature", str(temperature), qos=1)
    connection.publish("sensor/" + MqttUsername + "/humidity", str(humidity), qos=1)
    connection.publish("sensor/" + MqttUsername + "/pressure", str(pressure), qos=1)
    connection.publish("sensor/" + MqttUsername + "/ipaddress", ipaddress, qos=1)

    led.high()

    time.sleep(59)

#
