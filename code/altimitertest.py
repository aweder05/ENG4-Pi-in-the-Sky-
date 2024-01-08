#type: ignore
import board
import adafruit_mpl3115a2
i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)