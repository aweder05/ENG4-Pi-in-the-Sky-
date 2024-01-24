#type: ignore
 

# SPDX-FileCopyrightText: 2019 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the MPL3115A2 sensor.
# Will read the pressure and temperature and print them out every second.

import board
import adafruit_mpl3115a2
import time 
import busio

sda_pin = board.GP20 ## States the pin for SDA
scl_pin = board.GP21 ## States the pin for SCL

i2c = busio.I2C(scl_pin, sda_pin) ## States the pins for I2C

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
<<<<<<< HEAD
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

with open("/data.csv", "a") as datalog: #When Data Mode is Active
While True:
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} hectopascals".format(pressure))
    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))
    temperature = sensor.temperature
    print("Temperature: {0:0.3f} Celsius".format(temperature))


## sensor.sealevel_pressure = 10220


 
while True: 
    #pressure = sensor.pressure
    #print("Pressure: {0:0.3f} hectopascals".format(pressure))
    print(f"Altitude: {sensor.altitude +150}")
    ##altitude = sensor.altitude
    #print("Altitude: {0:0.3f} meters".format(altitude))
    print(f"Pressure: {sensor.pressure}")
    #temperature = sensor.temperature

    #print("Temperature: {0:0.3f} Celsius".format(temperature))
    #print(f"Temperature: {sensor.temperature}")
    
    time.sleep(1.0)