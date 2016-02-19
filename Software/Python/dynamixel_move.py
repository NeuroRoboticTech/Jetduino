#!/usr/bin/env python
#
# Jetduino Example for moving a dyanimxel smart servo using the Jetduino.
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

#set the dynamixel so it only returns back data for read commands.
print ("setting return status level to 1")
jetduino.dynamixelSetRegister(servo, jetduino.AX_RETURN_LEVEL, 1, 1)
jetduino.dynamixelSetRegister(servo, jetduino.AX_CW_ANGLE_LIMIT_L, 2, 0)
jetduino.dynamixelSetRegister(servo, jetduino.AX_CCW_ANGLE_LIMIT_L, 2, 1023)
jetduino.dynamixelSetEndless(servo, 0) 

print ("Move to 0 at fastest speed")
jetduino.dynamixelMove(servo, 0, 0)
time.sleep(2)

print ("Move to 1023 slowly")
jetduino.dynamixelMove(servo, 1023, 200)
time.sleep(1)

print ("stop the servo at its current position.")
jetduino.dynamixelStop(servo)
time.sleep(1)

while True:
    try:
        print ("Moving to 1023 at 100")
        jetduino.dynamixelMove(servo, 1023, 100)
        
        for num in range(1, 30):
            pos = jetduino.dynamixelGetRegister(servo, jetduino.AX_PRESENT_POSITION_L, 2)
            print ("Pos: %d" % pos)

        print ("Moving to 10 at 1000")
        jetduino.dynamixelMove(servo, 10, 1000)

        for num in range(1, 30):
            pos = jetduino.dynamixelGetRegister(servo, jetduino.AX_PRESENT_POSITION_L, 2)
            print ("Pos: %d" % pos)

    except KeyboardInterrupt:
        print("Exiting loop")
        break
    except IOError:
        print ("Error")

print ("stopping servo.")
jetduino.dynamixelStop(servo)

