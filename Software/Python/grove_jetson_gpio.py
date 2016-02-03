#!/usr/bin/env python
#
# Jetduino Example for using the Grove touch sensor and LED with the Jetson GPIO lines 
#  (http://www.seeedstudio.com/wiki/Grove_-_Touch_Sensor)
#  (http://www.seeedstudio.com/depot/Grove-LED-p-767.html)
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
import pins

# Connect the Grove Touch sensor to PU0
# Connect the Grove LED to PU2
# SIG,NC,VCC,GND
button = pins.JET_PU1
led = pins.JET_PU2

jetduino.pinMode(button,"INPUT")
jetduino.pinMode(led,"OUTPUT")

while True:
    try:
        button_val = jetduino.digitalRead(button)
        print ("Button value is %d" % button_val)
        jetduino.digitalWrite(led, button_val)
        time.sleep(.5)

    except IOError:
        print ("Error")