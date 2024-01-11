#type: ignore
import board
import adafruit_mpl3115a2
i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

While True: 
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} hectopascals".format(pressure))
    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))
    temperature = sensor.temperature
    print("Temperature: {0:0.3f} Celsius".format(temperature))
    time.sleep(1.0)