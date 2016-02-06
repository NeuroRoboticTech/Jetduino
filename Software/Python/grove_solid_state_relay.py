#!/usr/bin/env python
#
# Jetduino Example for using the Grove Solid State Relay (http://www.seeedstudio.com/wiki/Grove_-_Solid_State_Relay)
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

# WARNING:
# 	If the output voltage is higher than 36V, ensure the relay is in the off state before you operate with the terminal screws.
# 	The heatsink can get very hot during use.

import time
import jetduino
cCopyright (C) 2016  NeuroRobotic Technologies

# Connect the Grove Solid State Relay to digital port D4
# CTR,NC,VCC,GND
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
