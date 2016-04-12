#!/usr/bin/env python
#
# Jetduino test of reading from the analog lines
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
 
jetduino.pinMode(ARD_A0, INPUT_PIN)
jetduino.pinMode(ARD_A1, INPUT_PIN)
jetduino.pinMode(ARD_A2, INPUT_PIN)
jetduino.pinMode(ARD_A3, INPUT_PIN)
jetduino.pinMode(ARD_A4, INPUT_PIN)
jetduino.pinMode(ARD_A5, INPUT_PIN)
jetduino.pinMode(ARD_A6, INPUT_PIN)
jetduino.pinMode(ARD_A7, INPUT_PIN)
jetduino.pinMode(ARD_A8, INPUT_PIN)
jetduino.pinMode(ARD_A9, INPUT_PIN)
jetduino.pinMode(ARD_A10, INPUT_PIN)
jetduino.pinMode(ARD_A11, INPUT_PIN)

jetduino.setAnalogReadResolution(10)

def readDigital():
    ar0 = jetduino.analogRead(ARD_A0)
    ar1 = jetduino.analogRead(ARD_A1)
    ar2 = jetduino.analogRead(ARD_A2)
    ar3 = jetduino.analogRead(ARD_A3)
    ar4 = jetduino.analogRead(ARD_A4)
    ar5 = jetduino.analogRead(ARD_A5)
    ar6 = jetduino.analogRead(ARD_A6)
    ar7 = jetduino.analogRead(ARD_A7)
    ar8 = jetduino.analogRead(ARD_A8)
    ar9 = jetduino.analogRead(ARD_A9)
    ar10 = jetduino.analogRead(ARD_A10)
    ar11 = jetduino.analogRead(ARD_A11)

    #print("%f, %f, %f, %f, %f, %f" % (ar0, ar1, ar2, ar3, ar4, ar5)) 

    print("%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f" % (ar0, ar1, ar2, ar3, ar4, ar5, ar6, ar7, ar8, ar9, ar10, ar11)) 
    print("")

while True:
    try:
        readDigital()
        time.sleep(0.5)

    except KeyboardInterrupt:
        print("Exiting loop")
        break
    except IOError:
        print ("Error")


