#!/usr/bin/env python
#
# Jetduino Example for using the Grove Chainable RGB LED (http://www.seeedstudio.com/wiki/Grove_-_Chainable_RGB_LED)
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

# Connect first LED in Chainable RGB LED chain to digital port D7
# In: CI,DI,VCC,GND
# Out: CO,DO,VCC,GND
pin = ARD_D7

# I have 10 LEDs connected in series with the first connected to the jetduino and the last not connected
# First LED input socket connected to jetduino, output socket connected to second LED input and so on
numleds = 10     #If you only plug 1 LED, change 10 to 1

jetduino.pinMode(pin, OUTPUT_PIN)
time.sleep(1)

# Chainable RGB LED methods
# jetduino.storeColor(red, green, blue)
# jetduino.chainableRgbLed_init(pin, numLeds)
# jetduino.chainableRgbLed_test(pin, numLeds, testColor)
# jetduino.chainableRgbLed_pattern(pin, pattern, whichLed)
# jetduino.chainableRgbLed_modulo(pin, offset, divisor)
# jetduino.chainableRgbLed_setLevel(pin, level, reverse)

# test colors used in jetduino.chainableRgbLed_test()
testColorBlack = 0   # 0b000 #000000
testColorBlue = 1    # 0b001 #0000FF
testColorGreen = 2   # 0b010 #00FF00
testColorCyan = 3    # 0b011 #00FFFF
testColorRed = 4     # 0b100 #FF0000
testColorMagenta = 5 # 0b101 #FF00FF
testColorYellow = 6  # 0b110 #FFFF00
testColorWhite = 7   # 0b111 #FFFFFF

# patterns used in jetduino.chainableRgbLed_pattern()
thisLedOnly = 0
allLedsExceptThis = 1
thisLedAndInwards = 2
thisLedAndOutwards = 3

try:

    print "Test 1) Initialise"

    # init chain of leds
    jetduino.chainableRgbLed_init(pin, numleds)
    time.sleep(.5)

    # change color to green
    jetduino.storeColor(0,255,0)
    time.sleep(.5)

    # set led 1 to green
    jetduino.chainableRgbLed_pattern(pin, thisLedOnly, 0)
    time.sleep(.5)

    # change color to red
    jetduino.storeColor(255,0,0)
    time.sleep(.5)

    # set led 10 to red
    jetduino.chainableRgbLed_pattern(pin, thisLedOnly, 9)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 2a) Test Patterns - black")

    # test pattern 0 - black (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(1)


    print ("Test 2b) Test Patterns - blue")

    # test pattern 1 blue
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlue)
    time.sleep(1)


    print ("Test 2c) Test Patterns - green")

    # test pattern 2 green
    jetduino.chainableRgbLed_test(pin, numleds, testColorGreen)
    time.sleep(1)


    print ("Test 2d) Test Patterns - cyan")

    # test pattern 3 cyan
    jetduino.chainableRgbLed_test(pin, numleds, testColorCyan)
    time.sleep(1)


    print ("Test 2e) Test Patterns - red")

    # test pattern 4 red
    jetduino.chainableRgbLed_test(pin, numleds, testColorRed)
    time.sleep(1)


    print ("Test 2f) Test Patterns - magenta")

    # test pattern 5 magenta
    jetduino.chainableRgbLed_test(pin, numleds, testColorMagenta)
    time.sleep(1)


    print ("Test 2g) Test Patterns - yellow")

    # test pattern 6 yellow
    jetduino.chainableRgbLed_test(pin, numleds, testColorYellow)
    time.sleep(1)


    print ("Test 2h) Test Patterns - white")

    # test pattern 7 white
    jetduino.chainableRgbLed_test(pin, numleds, testColorWhite)
    time.sleep(1)


    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 3a) Set using pattern - this led only")

    # change color to red
    jetduino.storeColor(255,0,0)
    time.sleep(.5)

    # set led 3 to red
    jetduino.chainableRgbLed_pattern(pin, thisLedOnly, 2)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 3b) Set using pattern - all leds except this")

    # change color to blue
    jetduino.storeColor(0,0,255)
    time.sleep(.5)

    # set all leds except for 3 to blue
    jetduino.chainableRgbLed_pattern(pin, allLedsExceptThis, 3)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 3c) Set using pattern - this led and inwards")

    # change color to green
    jetduino.storeColor(0,255,0)
    time.sleep(.5)

    # set leds 1-3 to green
    jetduino.chainableRgbLed_pattern(pin, thisLedAndInwards, 2)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 3d) Set using pattern - this led and outwards")

    # change color to green
    jetduino.storeColor(0,255,0)
    time.sleep(.5)

    # set leds 7-10 to green
    jetduino.chainableRgbLed_pattern(pin, thisLedAndOutwards, 6)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 4a) Set using modulo - all leds")

    # change color to black (fully off)
    jetduino.storeColor(0,0,0)
    time.sleep(.5)

    # set all leds black
    # offset 0 means start at first led
    # divisor 1 means every led
    jetduino.chainableRgbLed_modulo(pin, 0, 1)
    time.sleep(.5)

    # change color to white (fully on)
    jetduino.storeColor(255,255,255)
    time.sleep(.5)

    # set all leds white
    jetduino.chainableRgbLed_modulo(pin, 0, 1)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 4b) Set using modulo - every 2")

    # change color to red
    jetduino.storeColor(255,0,0)
    time.sleep(.5)

    # set every 2nd led to red
    jetduino.chainableRgbLed_modulo(pin, 0, 2)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)


    print ("Test 4c) Set using modulo - every 2, offset 1")

    # change color to green
    jetduino.storeColor(0,255,0)
    time.sleep(.5)

    # set every 2nd led to green, offset 1
    jetduino.chainableRgbLed_modulo(pin, 1, 2)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 4d) Set using modulo - every 3, offset 0")

    # change color to red
    jetduino.storeColor(255,0,0)
    time.sleep(.5)

    # set every 3nd led to red
    jetduino.chainableRgbLed_modulo(pin, 0, 3)
    time.sleep(.5)

    # change color to green
    jetduino.storeColor(0,255,0)
    time.sleep(.5)

    # set every 3nd led to green, offset 1
    jetduino.chainableRgbLed_modulo(pin, 1, 3)
    time.sleep(.5)

    # change color to blue
    jetduino.storeColor(0,0,255)
    time.sleep(.5)

    # set every 3nd led to blue, offset 2
    jetduino.chainableRgbLed_modulo(pin, 2, 3)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 4e) Set using modulo - every 3, offset 1")

    # change color to yellow
    jetduino.storeColor(255,255,0)
    time.sleep(.5)

    # set every 4nd led to yellow
    jetduino.chainableRgbLed_modulo(pin, 1, 3)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)


    print ("Test 4f) Set using modulo - every 3, offset 2")

    # change color to magenta
    jetduino.storeColor(255,0,255)
    time.sleep(.5)

    # set every 4nd led to magenta
    jetduino.chainableRgbLed_modulo(pin, 2, 3)
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 5a) Set level 6")

    # change color to green
    jetduino.storeColor(0,255,0)
    time.sleep(.5)

    # set leds 1-6 to green
    jetduino.write_i2c_block(0x04,[95,pin,6,0])
    time.sleep(.5)

    # pause so you can see what happened
    time.sleep(2)

    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


    print ("Test 5b) Set level 7 - reverse")

    # change color to red
    jetduino.storeColor(255,0,0)
    time.sleep(.5)

    # set leds 4-10 to red
    jetduino.write_i2c_block(0x04,[95,pin,7,1])
    time.sleep(.5)


except KeyboardInterrupt:
    # reset (all off)
    jetduino.chainableRgbLed_test(pin, numleds, testColorBlack)
except IOError:
    print ("Error")
