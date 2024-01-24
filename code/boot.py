# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# Modified by Matthew Miller, Charlottesville High School

# SPDX-License-Identifier: MIT

"""
boot.py file for Pico data logging example. If pin GP0 is connected to GND when
the pico starts up, make the filesystem writeable by CircuitPython.
"""
import board
import digitalio
import storage
import time

write_pin = digitalio.DigitalInOut(board.GP1)
write_pin.direction = digitalio.Direction.INPUT
write_pin.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
time.sleep(2)

# If write pin is connected to ground on start-up, CircuitPython can write to CIRCUITPY filesystem.
if not write_pin.value: # Data Mode, shown by 10 short blinks
    storage.remount("/", readonly=False)
    for i in range(10):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)
        i = i+1

else: # Code Mode, shown by three long blinks
    for i in range(3):
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)
        i = i+1

