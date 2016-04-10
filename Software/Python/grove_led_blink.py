#!/usr/bin/env python

# Jetduino LED blink Example for the Grove LED Socket (http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit)
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
from jetduino import *

# Connect the Grove LED to digital port D4
led = ARD_D11

pinMode(led, OUTPUT_PIN)
time.sleep(1)

print "This example will blink a Grove LED connected to the GrovePi+ on the port labeled D4.  If you're having trouble seeing the LED blink, be sure to check the LED connection and the port number.  You may also try reversing the direction of the LED on the sensor."
print " "
print "Connect the LED to the port labele D4!" 

while True:
    try:
        #Blink the LED
        digitalWrite(led, HIGH)		# Send HIGH to switch on LED
        print "LED ON!"
        time.sleep(2)

        digitalWrite(led, LOW)		# Send LOW to switch off LED
        print "LED OFF!"
        time.sleep(2)

    except KeyboardInterrupt:	# Turn LED off before stopping
        digitalWrite(led, LOW)
        break
    except IOError:				# Print "Error" if communication error encountered
        print ("Error")
