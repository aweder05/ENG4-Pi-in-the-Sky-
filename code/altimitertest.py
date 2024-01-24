#type: ignore
import board
import adafruit_mpl3115a2
import time 

i2c = busio.I2C(scl_pin, sda_pin) ## States the pins for I2C

sda_pin = board.GP16 ## States the pin for SDA
scl_pin = board.GP17 ## States the pin for SCL

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

with open("/data.csv", "a") as datalog: #When Data Mode is Active
While True: 
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} hectopascals".format(pressure))
    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))
    temperature = sensor.temperature
    print("Temperature: {0:0.3f} Celsius".format(temperature))
    time.sleep(1.0)