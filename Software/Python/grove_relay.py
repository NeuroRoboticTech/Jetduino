#!/usr/bin/env python
#
# Jetduino Example for using the Grove Relay (http://www.seeedstudio.com/wiki/Grove_-_Relay)
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
# NOTE: Relay is normally open. LED will illuminate when closed and you will hear a definitive click sound
import time
import jetduino
from jetduino_pins import *

# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND
relay = ARD_D4

jetduino.pinMode(relay, OUTPUT_PIN)

while True:
    try:
        # switch on for 5 seconds
        jetduino.digitalWrite(relay, HIGH)
        print ("on")
        time.sleep(5)

        # switch off for 5 seconds
        jetduino.digitalWrite(relay, LOW)
        print ("off")
        time.sleep(5)

    except KeyboardInterrupt:
        jetduino.digitalWrite(relay, LOW)
        break
    except IOError:
        print ("Error")
