#!/usr/bin/env python
#
# Jetduino test of writing to the GPIO lines
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
 
jetduino.pinMode(JET_PU0, OUTPUT_PIN)
jetduino.pinMode(JET_PU1, OUTPUT_PIN)
jetduino.pinMode(JET_PU2, OUTPUT_PIN)
jetduino.pinMode(JET_PU3, OUTPUT_PIN)
jetduino.pinMode(JET_PU4, OUTPUT_PIN)
jetduino.pinMode(JET_PU5, OUTPUT_PIN)
jetduino.pinMode(JET_PU6, OUTPUT_PIN)

jetduino.pinMode(JET_PK1, OUTPUT_PIN)
jetduino.pinMode(JET_PK2, OUTPUT_PIN)
jetduino.pinMode(JET_PK4, OUTPUT_PIN)

jetduino.pinMode(JET_PH1, OUTPUT_PIN)

jetduino.pinMode(ARD_D2, OUTPUT_PIN)
jetduino.pinMode(ARD_D3, OUTPUT_PIN)
jetduino.pinMode(ARD_D4, OUTPUT_PIN)
jetduino.pinMode(ARD_D5, OUTPUT_PIN)
jetduino.pinMode(ARD_D6, OUTPUT_PIN)
jetduino.pinMode(ARD_D7, OUTPUT_PIN)
jetduino.pinMode(ARD_D8, OUTPUT_PIN)
jetduino.pinMode(ARD_D9, OUTPUT_PIN)
jetduino.pinMode(ARD_D10, OUTPUT_PIN)
jetduino.pinMode(ARD_D11, OUTPUT_PIN)
jetduino.pinMode(ARD_D12, OUTPUT_PIN)
jetduino.pinMode(ARD_D13, OUTPUT_PIN)

def writeDigital(val):
    jetduino.digitalWrite(JET_PU0, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PU1, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PU2, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PU3, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PU4, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PU5, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PU6, val)
    time.sleep(0.05)

    jetduino.digitalWrite(JET_PK1, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PK2, val)
    time.sleep(0.05)
    jetduino.digitalWrite(JET_PK4, val)
    time.sleep(0.05)

    jetduino.digitalWrite(JET_PH1, val)
    time.sleep(0.05)

    jetduino.digitalWrite(ARD_D2, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D3, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D4, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D5, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D6, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D7, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D8, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D9, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D10, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D11, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D12, val)
    time.sleep(0.05)
    jetduino.digitalWrite(ARD_D13, val)
    time.sleep(0.05)

while True:
    try:
        print ("High")
        writeDigital(HIGH)
        time.sleep(2)

        print ("Low")
        writeDigital(LOW)
        time.sleep(2)


    except KeyboardInterrupt:
        print("Exiting loop")
        break
    except IOError:
        print ("Error")


