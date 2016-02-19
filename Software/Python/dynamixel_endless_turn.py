#!/usr/bin/env python
#
# Jetduino Example for moving multiple dyanimxel smart servo at the same time using the Jetduino.
#
# The Jetduino connects the Jetson and Grove sensors.  You can learn more about the Jetduino here:  http://www.NeuroRoboticTech.com/Projects/Jetduino
#
# Have a question about this example?  Ask on the forums here:  http://www.NeuroRoboticTech.com/Forum
#
'''
## License

The MIT License (MIT)

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

servo = 1

print ("Setting servo 1 to be endless turns.")
jetduino.dynamixelSetEndless(servo, True)

for num in range(1,2):
    try:
        print ("Turning CW at 1000")
        jetduino.dynamixelTurnSpeed(servo, CLOCKWISE, 1000);
        time.sleep(5)

        print ("Turning CCW at 500")
        jetduino.dynamixelTurnSpeed(servo, COUNTER_CLOCKWISE, 500);
        time.sleep(5)

    except IOError:
        print ("Error")

print ("Setting servo 1 to back to regular servo.")
jetduino.dynamixelSetEndless(servo, False)
jetduino.dynamixelMove(servo, 512, 1000);


