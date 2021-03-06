#!/usr/bin/env python
#
# Jetduino Library for using the Grove - I2C ADC(http://www.seeedstudio.com/depot/Grove-I2C-ADC-p-1580.html)
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

import time,sys
import smbus

#bus = smbus.SMBus(0) #GEN1_I2C
bus = smbus.SMBus(1) #GEN2_I2C
#bus = smbus.SMBus(4) #PWR_I2C

class ADC:
	address = None
	
	REG_ADDR_RESULT = 0x00
	REG_ADDR_ALERT  = 0x01
	REG_ADDR_CONFIG = 0x02
	REG_ADDR_LIMITL = 0x03
	REG_ADDR_LIMITH = 0x04
	REG_ADDR_HYST   = 0x05
	REG_ADDR_CONVL  = 0x06
	REG_ADDR_CONVH  = 0x07

	def __init__(self,address=0x55):
		self.address=address
		bus.write_byte_data(self.address, self.REG_ADDR_CONFIG,0x20)

	def adc_read(self):
		data=bus.read_i2c_block_data(self.address, self.REG_ADDR_RESULT, 2)
		raw_val=(data[0]&0x0f)<<8 | data[1]
		return raw_val

if __name__ == "__main__":		
	adc= ADC()
	while True:
		print adc.adc_read()
		time.sleep(.5)