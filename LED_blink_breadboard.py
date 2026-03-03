"""
Created by: Ian Smith-Chao
Created on: Mar 2026
This module will send repeated pulses with a delay to a breadboard LED.
"""

import board
import digitalio
import time

# Assign pin 5 to LED_pin and initialize it as an output.
LED_pin = digitalio.DigitalInOut(board.D5)
LED_pin.direction = digitalio.Direction.OUTPUT

# Main loop.
while True:
  # Turn pin 5 ON for 1 s.
  LED_pin.value = True
  time.sleep(1.0)

  # Turn pin 5 OFF for 1 s.
  LED_pin.value = False
  time.sleep(1.0)
