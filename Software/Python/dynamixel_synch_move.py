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

servo_a = 1
servo_b = 2

#set the dynamixels so they only returns back data for read commands.
print ("setting return status level to 1")
jetduino.dynamixel_set_register(servo_a, jetduino.AX_RETURN_LEVEL, 1, 1)
jetduino.dynamixel_set_register(servo_b, jetduino.AX_RETURN_LEVEL, 1, 1)

while True:
    try:

        jetduino.dynamixel_start_synch_move()
        print ("Moving 1 to 1023 at 100")
        print ("Moving 2 to 10 at 1000")
        jetduino.dynamixel_add_synch_move(servo_a, 1023, 100)
        jetduino.dynamixel_add_synch_move(servo_b, 10, 100)
        jetduino.dynamixel_execute_synch_move()
        time.sleep(4)

        jetduino.dynamixel_start_synch_move()
        print ("Moving 1 to 10 at 1000")
        print ("Moving 2 to 1023 at 100")
        jetduino.dynamixel_add_synch_move(servo_a, 10, 100)
        jetduino.dynamixel_add_synch_move(servo_b, 1023, 100)
        jetduino.dynamixel_execute_synch_move()
        time.sleep(4)

    except IOError:
        print ("Error")
