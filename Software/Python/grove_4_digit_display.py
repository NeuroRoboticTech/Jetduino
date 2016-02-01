#!/usr/bin/env python
#
# Jetduino Example for using the Grove 4 Digit Display ( http://www.seeedstudio.com/wiki/Grove_-_4-Digit_Display)
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

# NOTE: 4x red 7 segment display with colon and 8 luminance levels, but no decimal points

import time
import jetduino

# Connect the Grove 4 Digit Display to digital port D5
# CLK,DIO,VCC,GND
display = 5
jetduino.pinMode(display,"OUTPUT")

# If you have an analog sensor connect it to A0 so you can monitor it below
sensor = 0
jetduino.pinMode(sensor,"INPUT")

time.sleep(.5)

# 4 Digit Display methods
# jetduino.fourDigit_init(pin)
# jetduino.fourDigit_number(pin,value,leading_zero)
# jetduino.fourDigit_brightness(pin,brightness)
# jetduino.fourDigit_digit(pin,segment,value)
# jetduino.fourDigit_segment(pin,segment,leds)
# jetduino.fourDigit_score(pin,left,right)
# jetduino.fourDigit_monitor(pin,analog,duration)
# jetduino.fourDigit_on(pin)
# jetduino.fourDigit_off(pin)

while True:
    try:
        print ("Test 1) Initialise")
        jetduino.fourDigit_init(display)
        time.sleep(.5)

        print ("Test 2) Set brightness")
        for i in range(0,8):
            jetduino.fourDigit_brightness(display,i)
            time.sleep(.2)
        time.sleep(.3)

        # set to lowest brightness level
        jetduino.fourDigit_brightness(display,0)
        time.sleep(.5)

        print ("Test 3) Set number without leading zeros")
        leading_zero = 0
        jetduino.fourDigit_number(display,1,leading_zero)
        time.sleep(.5)
        jetduino.fourDigit_number(display,12,leading_zero)
        time.sleep(.5)
        jetduino.fourDigit_number(display,123,leading_zero)
        time.sleep(.5)
        jetduino.fourDigit_number(display,1234,leading_zero)
        time.sleep(.5)

        print ("Test 4) Set number with leading zeros")
        leading_zero = 1
        jetduino.fourDigit_number(display,5,leading_zero)
        time.sleep(.5)
        jetduino.fourDigit_number(display,56,leading_zero)
        time.sleep(.5)
        jetduino.fourDigit_number(display,567,leading_zero)
        time.sleep(.5)
        jetduino.fourDigit_number(display,5678,leading_zero)
        time.sleep(.5)

        print ("Test 5) Set individual digit")
        jetduino.fourDigit_digit(display,0,2)
        jetduino.fourDigit_digit(display,1,6)
        jetduino.fourDigit_digit(display,2,9)
        jetduino.fourDigit_digit(display,3,15) # 15 = F
        time.sleep(.5)

        print ("Test 6) Set individual segment")
        jetduino.fourDigit_segment(display,0,118) # 118 = H
        jetduino.fourDigit_segment(display,1,121) # 121 = E
        jetduino.fourDigit_segment(display,2,118) # 118 = H
        jetduino.fourDigit_segment(display,3,121) # 121 = E
        time.sleep(.5)

        jetduino.fourDigit_segment(display,0,57) # 57 = C
        jetduino.fourDigit_segment(display,1,63) # 63 = O
        jetduino.fourDigit_segment(display,2,63) # 63 = O
        jetduino.fourDigit_segment(display,3,56) # 56 = L
        time.sleep(.5)

        print ("Test 7) Set score")
        jetduino.fourDigit_score(display,0,0)
        time.sleep(.2)
        jetduino.fourDigit_score(display,1,0)
        time.sleep(.2)
        jetduino.fourDigit_score(display,1,1)
        time.sleep(.2)
        jetduino.fourDigit_score(display,1,2)
        time.sleep(.2)
        jetduino.fourDigit_score(display,1,3)
        time.sleep(.2)
        jetduino.fourDigit_score(display,1,4)
        time.sleep(.2)
        jetduino.fourDigit_score(display,1,5)
        time.sleep(.5)

        print ("Test 8) Set time")
        jetduino.fourDigit_score(display,12,59)
        time.sleep(.5)

        print ("Test 9) Monitor analog pin")
        seconds = 10
        jetduino.fourDigit_monitor(display,sensor,seconds)
        time.sleep(.5)

        print ("Test 10) Switch all on")
        jetduino.fourDigit_on(display)
        time.sleep(.5)

        print ("Test 11) Switch all off")
        jetduino.fourDigit_off(display)
        time.sleep(.5)

    except KeyboardInterrupt:
        jetduino.fourDigit_off(display)
        break
    except IOError:
        print ("Error")
