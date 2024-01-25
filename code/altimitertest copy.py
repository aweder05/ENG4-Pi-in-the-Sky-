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

## sensor.sealevel_pressure = 10220


with open("/data.csv", "a") as datalog:
    while True: 
        #pressure = sensor.pressure
        #print("Pressure: {0:0.3f} hectopascals".format(pressure))
        print(f"Altitude: {sensor.altitude +150}")
        Altitude = sensor.altitude +150
        ##altitude = sensor.altitude
        #print("Altitude: {0:0.3f} meters".format(altitude))
        print(f"Pressure: {sensor.pressure}")
        Pressure = sensor.pressure
        #temperature = sensor.temperature

        #print("Temperature: {0:0.3f} Celsius".format(temperature))
        #print(f"Temperature: {sensor.temperature}")
        datalog.write(f"{time_elapsed},{Altitude},{Pressure}\n") #Put the data into a chart
        
        datalog.flush() # Save the data
        time.sleep(1.0)