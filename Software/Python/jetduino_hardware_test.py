#!/usr/bin/env python
#
# Jetduino Hardware Test
#	Connect Buzzer to Port D8
#	Connect Button to Analog Port A0
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

# Connect the Grove Button to digital Port 4.
button = ARD_D4		# This is the D4 pin.
buzzer = ARD_D8		# This is the D8 pin.

jetduino.pinMode(button, INPUT_PIN)
jetduino.pinMode(buzzer, OUTPUT_PIN)

print "GrovePi Basic Hardware Test."
print "Setup:  Connect the button sensor to port D4.  Connect a Grove LED to port D8."
print "Press the button and the buzzer will buzz!"

while True:
    try:
		butt_val = jetduino.digitalRead(button)	# Each time we go through the loop, we read D4.
		print (butt_val)						# Print the value of D4.
		if butt_val > 0:
			jetduino.digitalWrite(buzzer, HIGH)
			print ('start')
			time.sleep(1)
		else:
			jetduino.digitalWrite(buzzer, LOW)
			time.sleep(.5)

    except IOError:
        print ("Error")
