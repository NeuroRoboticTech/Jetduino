#!/usr/bin/env python
#
# Jetduino test of analog writings
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

def writeAnalog(val):
    jetduino.analogWrite(ARD_D2, val)
    jetduino.analogWrite(ARD_D3, val)
    jetduino.analogWrite(ARD_D4, val)
    jetduino.analogWrite(ARD_D5, val)
    jetduino.analogWrite(ARD_D6, val)
    jetduino.analogWrite(ARD_D7, val)
    jetduino.analogWrite(ARD_D8, val)
    jetduino.analogWrite(ARD_D9, val)
    jetduino.analogWrite(ARD_D10, val)
    jetduino.analogWrite(ARD_D11, val)
    jetduino.analogWrite(ARD_D12, val)
    jetduino.analogWrite(ARD_D13, val)

i = 0

while True:
    try:
        # Reset
        if i > 255:
            i = 0

        # Current brightness
        print (i)

        # Give PWM output to LED
        writeAnalog(i)

        # Increment brightness for next iteration
        i = i + 10
        time.sleep(1)


    except KeyboardInterrupt:
        writeAnalog(0)
        print("Exiting loop")
        break
    except IOError:
        print ("Error")

