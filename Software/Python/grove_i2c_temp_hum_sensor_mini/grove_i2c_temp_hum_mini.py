#!/usr/bin/env python
#
# Jetduino Library for using the Grove - Temperature&Humidity Sensor (http://www.seeedstudio.com/depot/Grove-TemperatureHumidity-Sensor-HighAccuracy-Mini-p-1921.html)
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
#################################################################################################################################################
# NOTE:
# The software for this sensor is still in development and might make your GrovePi unuable as long as this sensor is connected with the GrovePi
#################################################################################################################################################
import time,sys
import smbus

debug = 0
bus = smbus.SMBus(0) #GEN1_I2C
#bus = smbus.SMBus(1) #GEN2_I2C
#bus = smbus.SMBus(4) #PWR_I2C

class th02:
	
	ADDRESS = 0x40

	TH02_REG_STATUS = 0x00
	TH02_REG_DATA_H = 0x01
	TH02_REG_DATA_L = 0x02
	TH02_REG_CONFIG = 0x03
	TH02_REG_ID = 0x11

	TH02_STATUS_RDY_MASK = 0x01

	TH02_CMD_MEASURE_HUMI = [0x01]
	TH02_CMD_MEASURE_TEMP = [0x11]

	SUCCESS = 0
	
	def getTemperature(self):
		bus.write_i2c_block_data(self.ADDRESS, self.TH02_REG_CONFIG, self.TH02_CMD_MEASURE_TEMP)
		
		while 1:
			status=self.getStatus()
			if debug:
				print "st:",status
			if status:
				break
		t_raw=bus.read_i2c_block_data(self.ADDRESS, self.TH02_REG_DATA_H,3)
		if debug:
			print t_raw
		temperature = (t_raw[1]<<8|t_raw[2])>>2
		return (temperature/32.0)-50.0
		
	def getHumidity(self):
		bus.write_i2c_block_data(self.ADDRESS, self.TH02_REG_CONFIG, self.TH02_CMD_MEASURE_HUMI)
		
		while 1:
			status=self.getStatus()
			if debug:
				print "st:",status
			if status:
				break
		t_raw=bus.read_i2c_block_data(self.ADDRESS, self.TH02_REG_DATA_H,3)
		if debug:
			print t_raw
		temperature = (t_raw[1]<<8|t_raw[2])>>4
		return (temperature/16.0)-24.0
		
	def getStatus(self):
		status=bus.read_i2c_block_data(self.ADDRESS, self.TH02_REG_STATUS,1)
		if debug:
			print status
		if status[0] & self.TH02_STATUS_RDY_MASK <> 1:
			return 1
		else:
			return 0

if __name__ == "__main__":		
	t= th02()
	while True:
		print t.getTemperature(),t.getHumidity()
		time.sleep(.5)