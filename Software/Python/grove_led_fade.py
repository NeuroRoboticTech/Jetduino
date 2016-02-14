#!/usr/bin/env python
#
# Jetduino Example for using the Grove LED for LED Fade effect (http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit)
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

# Connect the Grove LED to digital port D4, and potentiometer to A0
# SIG,NC,VCC,GND
pot = ARD_A0
led = ARD_D4

# Digital ports that support Pulse Width Modulation (PWM)
# D2-D13, DAC1, DAC2

# Digital ports that do not support PWM
# D14-D54

jetduino.pinMode(pot, INPUT_PIN)
jetduino.pinMode(led, OUTPUT_PIN)
time.sleep(1)

oldVal = -1

while True:
    try:
        #Read in the value from the pot.
        val = jetduino.analogRead(pot)

        #convert to 8-bit
        newVal = int(jetduino.mapValue(val, 0, 1023, 0, 255))

        # Give PWM output to LED if value changed.
        if newVal <> oldVal:
            jetduino.analogWrite(led, newVal)
            oldVal = newVal
            print ("LED: %d" % newVal)

        # sleep
        time.sleep(.25)

    except KeyboardInterrupt:
        jetduino.analogWrite(led,0)
        break
    except IOError:
        print ("Error")
