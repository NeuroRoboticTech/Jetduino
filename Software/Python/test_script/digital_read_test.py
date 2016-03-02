#!/usr/bin/env python
#
# Jetduino test of reading from the GPIO lines
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
 
jetduino.pinMode(JET_PU0, INPUT_PIN)
jetduino.pinMode(JET_PU1, INPUT_PIN)
jetduino.pinMode(JET_PU2, INPUT_PIN)
jetduino.pinMode(JET_PU3, INPUT_PIN)
jetduino.pinMode(JET_PU4, INPUT_PIN)
jetduino.pinMode(JET_PU5, INPUT_PIN)
jetduino.pinMode(JET_PU6, INPUT_PIN)

def readDigital():
    pu0 = jetduino.digitalRead(JET_PU0)
    pu1 = jetduino.digitalRead(JET_PU1)
    pu2 = jetduino.digitalRead(JET_PU2)
    pu3 = jetduino.digitalRead(JET_PU3)
    pu4 = jetduino.digitalRead(JET_PU4)
    pu5 = jetduino.digitalRead(JET_PU5)
    pu6 = jetduino.digitalRead(JET_PU6)

    print("%d, %d, %d, %d, %d, %d, %d" % (pu0, pu1, pu2, pu3, pu4, pu5, pu6)) 

while True:
    try:
        readDigital()
        time.sleep(2)

    except KeyboardInterrupt:
        print("Exiting loop")
        break
    except IOError:
        print ("Error")


