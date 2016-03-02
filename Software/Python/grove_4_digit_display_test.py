#!/usr/bin/env python

import time
import jetduino
from jetduino_pins import *

display = ARD_D4

jetduino.fourDigit_init(display)
time.sleep(0.1)

jetduino.fourDigit_number(display,1234, 1)
time.sleep(1)
jetduino.fourDigit_number(display,11, 1)
time.sleep(1)
jetduino.fourDigit_number(display,55, 0)
time.sleep(1)
jetduino.fourDigit_brightness(display,7)
time.sleep(1)
jetduino.fourDigit_brightness(display,0)
time.sleep(1)
jetduino.fourDigit_brightness(display,2)
time.sleep(1)
jetduino.fourDigit_off(display)

