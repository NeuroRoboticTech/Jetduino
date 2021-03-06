#!/usr/bin/env python
#
# Jetduino Example for using the Grove Electricity Sensor (http://www.seeedstudio.com/wiki/Grove_-_Electricity_Sensor)
#
# The Jetduino connects the Jetson and Grove sensors.  You can learn more about the Jetduino here:  http://www.NeuroRoboticTech.com/Projects/Jetduino
#
# Have a question about this example?  Ask on the forums here:  http://www.NeuroRoboticTech.com/Forum
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Jetduino for the Jetson TK1/TX1: an open source platform for connecting 
Grove Sensors to the Jetson embedded supercomputers.
Copyright (C) 2016  NeuroRobotic Technologies

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time
import jetduino
from jetduino_pins import *

# Connect the Grove Electricity Sensor to analog port A0
# SIG,NC,NC,GND

sensor = ARD_A0

jetduino.pinMode(sensor, INPUT_PIN)

# Vcc of the grove interface is normally 5v
grove_vcc = 5

while True:
    try:
        # Get sensor value
        sensor_value = jetduino.analogRead(sensor)

        # Calculate amplitude current (mA)
        amplitude_current = (float)(sensor_value / 1024 * grove_vcc / 800 * 2000000)

        # Calculate effective value (mA)
        effective_value = amplitude_current / 1.414

        # minimum_current = 1 / 1024 * grove_vcc / 800 * 2000000 / 1.414 = 8.6(mA)
        # Only for sinusoidal alternating current

        print ("sensor_value", sensor_value)
        print ("The amplitude of the current is", amplitude_current, "mA")
        print ("The effective value of the current is", effective_value, "mA")
        time.sleep(1)

    except IOError:
        print ("Error")
