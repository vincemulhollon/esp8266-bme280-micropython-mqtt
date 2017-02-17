# test-mqtt-sample.py
#
# copy to test-mqtt.py and edit the variables below
#
# Assumes your mqtt account, perhaps io.adafruit.com is set up and boot.py has
# working wifi
# This assumes your boot.py sets up wifi using object named sta_if
#
# This script is a good way to test the mqtt server and wifi connectivity
# It doesn't require working sensor or I2C or wiring or any of that.

import network
import time
import machine
import gc

from umqtt.robust import MQTTClient

# EDIT STARTING HERE

MqttClient = "name" # Perhaps "office-weather-sensor"
MqttUrl = "mqtt.server.host.name" # Perhaps "io.adafruit.com"
MqttUsername = "YourLoginName" # Your MQTT login name
MqttAioKey = "ba11dc82629b469e9f73246c7e8ca2e4" # Your MQTT AIO key.  Perhaps 32 hexadecimal digits
MqttGroupName = "your-group-name" # Your MQTT group name.   Perhaps the same as client name.

temperature = 72.1 # F
humidity =  51.1 # percent
pressure = 29.5 # inches of mercury

# EDIT STOPPING HERE

ipaddress = sta_if.ifconfig()[0]

connection = MQTTClient(MqttClient, MqttUrl, 0, MqttUsername, MqttAioKey)

connection.connect()

connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "temperature", str(temperature))
connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "humidity", str(humidity))
connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "pressure", str(pressure))
connection.publish(MqttUsername + "/" + "feeds/" + MqttGroupName + "." + "ipaddress", ipaddress)

time.sleep(1)

connection.disconnect()

#
