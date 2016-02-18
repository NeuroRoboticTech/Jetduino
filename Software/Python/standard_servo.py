#!/usr/bin/env python
#
# Jetduino Example for using controlling and reading a standard servo.
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

servo_pin = ARD_D4

print("attaching to servo.")
jetduino.servoAttach(servo_pin)
time.sleep(.1)

print("Moving servo to angle 0.")
jetduino.servoWrite(servo_pin, 0)
time.sleep(0.3)

print("Reading servo angle.")
cur_angle = jetduino.servoRead(servo_pin)
print ("angle =", cur_angle)
time.sleep(1)

print("Moving servo to angle 180.")
jetduino.servoWrite(servo_pin, 180)
time.sleep(0.3)

print("Reading servo angle.")
cur_angle = jetduino.servoRead(servo_pin)
print ("angle =", cur_angle)
time.sleep(1)

for num in range(1,5):
    print("Moving servo cycle %d." % num)
    for angle in range(0,180):
        #print("    angle %d" % angle)
        jetduino.servoWrite(servo_pin, angle)
        time.sleep(0.05)
    
    time.sleep(1)

print("detaching from servo")
jetduino.servoDetach(servo_pin)

