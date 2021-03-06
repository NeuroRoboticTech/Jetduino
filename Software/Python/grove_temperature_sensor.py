#!/usr/bin/env python
#
# Jetduino Example for using the Grove Temperature Sensor (http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor)
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
# NOTE: 
# 	The sensor uses a thermistor to detect ambient temperature.
# 	The resistance of a thermistor will increase when the ambient temperature decreases.
#	
# 	There are 3 revisions 1.0, 1.1 and 1.2, each using a different model thermistor.
# 	Each thermistor datasheet specifies a unique Nominal B-Constant which is used in the calculation forumla.
#	
# 	The second argument in the jetduino.temp() method defines which board version you have connected.
# 	Defaults to '1.0'. eg.
# 		temp = jetduino.temp(sensor)        # B value = 3975
# 		temp = jetduino.temp(sensor,'1.1')  # B value = 4250
# 		temp = jetduino.temp(sensor,'1.2')  # B value = 4250

import time
import jetduino
from jetduino_pins import *

# Connect the Grove Temperature Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = ARD_A0

while True:
    try:
        temp = jetduino.temp(sensor,'1.2')
        print ("temp =", temp)
        time.sleep(.5)

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")
