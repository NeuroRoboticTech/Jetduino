#!/usr/bin/env python
#
# Jetduino Example for setting/getting the registers of a dyanimxel smart servo using the Jetduino.
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

print ("setting return status level to 1")
jetduino.dynamixel_set_register(servo, jetduino.AX_RETURN_LEVEL, 1, 1)

ret_level = jetduino.dynamixel_get_register(servo, jetduino.AX_RETURN_LEVEL, 1)
print ("return status level: %d" % (ret_level))

#first get the angle limits
cw_limit_orig = jetduino.dynamixel_get_register(servo, jetduino.AX_CW_ANGLE_LIMIT_L, 2)
ccw_limit_orig = jetduino.dynamixel_get_register(servo, jetduino.AX_CCW_ANGLE_LIMIT_L, 2)
print ("Before: CW Limit: %d, CCW Limit: %d" % (cw_limit_orig, ccw_limit_orig))

#now set them to something else
print ("Setting cw=130, ccw=180")
jetduino.dynamixel_set_register(servo, jetduino.AX_CW_ANGLE_LIMIT_L, 2, 130)
jetduino.dynamixel_set_register(servo, jetduino.AX_CCW_ANGLE_LIMIT_L, 2, 800)

#get the angle limits again to check
cw_limit = jetduino.dynamixel_get_register(servo, jetduino.AX_CW_ANGLE_LIMIT_L, 2)
ccw_limit = jetduino.dynamixel_get_register(servo, jetduino.AX_CCW_ANGLE_LIMIT_L, 2)
print ("After: CW Limit: %d, CCW Limit: %d" % (cw_limit, ccw_limit))

#now reset them back to the original values
print ("Resetting angle limits to original values")
jetduino.dynamixel_set_register(servo, jetduino.AX_CW_ANGLE_LIMIT_L, 2, 0)
jetduino.dynamixel_set_register(servo, jetduino.AX_CCW_ANGLE_LIMIT_L, 2, 1023)

#get the angle limits again to check
cw_limit = jetduino.dynamixel_get_register(servo, jetduino.AX_CW_ANGLE_LIMIT_L, 2)
ccw_limit = jetduino.dynamixel_get_register(servo, jetduino.AX_CCW_ANGLE_LIMIT_L, 2)
print ("Reset: CW Limit: %d, CCW Limit: %d" % (cw_limit, ccw_limit))


