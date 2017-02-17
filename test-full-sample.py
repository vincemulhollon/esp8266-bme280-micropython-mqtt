# test-full-sample.py
#
# copy to test-full.py and edit the variables below
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

MqttClient = "name" # Perhaps "office-weather-sensor"
MqttUrl = "mqtt.server.host.name" # Perhaps "io.adafruit.com"
MqttUsername = "YourLoginName" # Your MQTT login name
MqttAioKey = "12345678901234567890123456789012" # Your MQTT AIO key.  Perhaps 32 hexadecimal digits
MqttGroupName = "your-group-name" # Your MQTT group name.   Perhaps the same as client name.

scl = Pin(5)
sda = Pin(4)
i2c = I2C(scl=scl, sda=sda)

connection = MQTTClient(MqttClient, MqttUrl, 0, MqttUsername, MqttAioKey)

connection.connect()

while True:

    bme=BME280(i2c=i2c)
    temperature = bme.values[0]
    humidity = bme.values[2]
    pressure = bme.values[1]
    ipaddress = sta_if.ifconfig()[0]

    connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "temperature", str(temperature))
    connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "humidity", str(humidity))
    connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "pressure", str(pressure))
    connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "ipaddress", ipaddress)

    time.sleep(120)

#
