#!/usr/bin/env python
#
# Jetduino Python library
# v1.0.0
#
# This file provides the basic functions for using the Jetduino
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

# Karan Nayan
# Initial Date: 13 Feb 2014
# Last Updated: 01 June 2015
# http://www.dexterindustries.com/
# David Cofer
# Last Updated: 31 Jan 2016
# http://www.NeuroRoboticTech.com/

import smbus
import time
import math
import struct
import sys
from jetduino_pins import *
from sysfs.gpio import Controller, OUTPUT, INPUT, RISING

debug =0

#The Jetduino should always use SMBus 1 for GEN2_I2C
p_version=3
bus = smbus.SMBus(1) #GEN2_I2C

# I2C Address of Arduino
ard_address = 0x04

# I2C Address of Jetduino ADC
#adc_address = 0x

#Make the jetson pins available for use.
Controller.available_pins = [JET_PH1, 
	JET_PK1, 
	JET_PK2, 
	JET_PK4, 
	JET_PU0, 
	JET_PU1, 
	JET_PU2, 
	JET_PU3, 
	JET_PU4, 
	JET_PU5, 
	JET_PU6]

# Command Format
# digitalRead() command format header
dRead_cmd = [1]
# digitalWrite() command format header
dWrite_cmd = [2]
# analogRead() command format header
aRead_cmd = [3]
# analogWrite() command format header
aWrite_cmd = [4]
# pinMode() command format header
pMode_cmd = [5]
# Ultrasonic read
uRead_cmd = [7]
# Get firmware version
version_cmd = [8]
# Accelerometer (+/- 1.5g) read
acc_xyz_cmd = [20]
# RTC get time
rtc_getTime_cmd = [30]

# analog precision
analog_read_prec_cmd = [31]
analog_write_prec_cmd = [32]

# servo attach
servo_attach_cmd = [35]
# servo detach
servo_detach_cmd = [36]
# servo write
servo_write_cmd = [37]
# servo read
servo_read_cmd = [38]

# DHT Pro sensor temperature
dht_temp_cmd = [40]

# Grove LED Bar commands
# Initialise
ledBarInit_cmd = [50]
# Set orientation
ledBarOrient_cmd = [51]
# Set level
ledBarLevel_cmd = [52]
# Set single LED
ledBarSetOne_cmd = [53]
# Toggle single LED
ledBarToggleOne_cmd = [54]
# Set all LEDs
ledBarSet_cmd = [55]
# Get current state
ledBarGet_cmd = [56]

# Grove 4 Digit Display commands
# Initialise
fourDigitInit_cmd = [70]
# Set brightness, not visible until next cmd
fourDigitBrightness_cmd = [71]
# Set numeric value without leading zeros
fourDigitValue_cmd = [72]
# Set numeric value with leading zeros
fourDigitValueZeros_cmd = [73]
# Set individual digit
fourDigitIndividualDigit_cmd = [74]
# Set individual leds of a segment
fourDigitIndividualLeds_cmd = [75]
# Set left and right values with colon
fourDigitScore_cmd = [76]
# Analog read for n seconds
fourDigitAnalogRead_cmd = [77]
# Entire display on
fourDigitAllOn_cmd = [78]
# Entire display off
fourDigitAllOff_cmd = [79]

# Grove Chainable RGB LED commands
# Store color for later use
storeColor_cmd = [90]
# Initialise
chainableRgbLedInit_cmd = [91]
# Initialise and test with a simple color
chainableRgbLedTest_cmd = [92]
# Set one or more leds to the stored color by pattern
chainableRgbLedSetPattern_cmd = [93]
# set one or more leds to the stored color by modulo
chainableRgbLedSetModulo_cmd = [94]
# sets leds similar to a bar graph, reversible
chainableRgbLedSetLevel_cmd = [95]

# Dynamixel servo controls
dyn_set_register_cmd = [100]
dyn_get_register_cmd = [101]
dyn_move_cmd  = [102]
dyn_stop_cmd  = [103]
dyn_set_endless_cmd  = [104]
dyn_set_turn_speed_cmd  = [105]
dyn_start_synch_move_cmd  = [106]
dyn_add_servo_synch_cmd  = [107]
dyn_exec_synch_move_cmd  = [108]

# Read the button from IR sensor
ir_read_cmd=[21]
# Set pin for the IR reciever
ir_recv_pin_cmd=[22]

dus_sensor_read_cmd=[10]
dust_sensor_en_cmd=[14]
dust_sensor_dis_cmd=[15]
encoder_read_cmd=[11] 
encoder_en_cmd=[16]
encoder_dis_cmd=[17]
flow_read_cmd=[12]
flow_disable_cmd=[13]
flow_en_cmd=[18]
# This allows us to be more specific about which commands contain unused bytes
unused = 0


#Dynamixel AX12/18 register values.
#EEPROM AREA  ///////////////////////////////////////////////////////////
AX_MODEL_NUMBER_L           = 0
AX_MODEL_NUMBER_H           = 1
AX_VERSION                  = 2
AX_ID                       = 3
AX_BAUD_RATE                = 4
AX_RETURN_DELAY_TIME        = 5 
AX_CW_ANGLE_LIMIT_L         = 6
AX_CW_ANGLE_LIMIT_H         = 7
AX_CCW_ANGLE_LIMIT_L        = 8
AX_CCW_ANGLE_LIMIT_H        = 9
AX_SYSTEM_DATA2             = 10
AX_LIMIT_TEMPERATURE        = 11
AX_DOWN_LIMIT_VOLTAGE       = 12
AX_UP_LIMIT_VOLTAGE         = 13
AX_MAX_TORQUE_L             = 14
AX_MAX_TORQUE_H             = 15
AX_RETURN_LEVEL             = 16
AX_ALARM_LED                = 17
AX_ALARM_SHUTDOWN           = 18
AX_OPERATING_MODE           = 19
AX_DOWN_CALIBRATION_L       = 20
AX_DOWN_CALIBRATION_H       = 21
AX_UP_CALIBRATION_L         = 22
AX_UP_CALIBRATION_H         = 23

# RAM AREA  //////////////////////////////////////////////////////////////
AX_TORQUE_ENABLE            = 24
AX_LED                      = 25
AX_CW_COMPLIANCE_MARGIN     = 26
AX_CCW_COMPLIANCE_MARGIN    = 27
AX_CW_COMPLIANCE_SLOPE      = 28
AX_CCW_COMPLIANCE_SLOPE     = 29
AX_GOAL_POSITION_L          = 30
AX_GOAL_POSITION_H          = 31
AX_GOAL_SPEED_L             = 32
AX_GOAL_SPEED_H             = 33
AX_TORQUE_LIMIT_L           = 34
AX_TORQUE_LIMIT_H           = 35
AX_PRESENT_POSITION_L       = 36
AX_PRESENT_POSITION_H       = 37
AX_PRESENT_SPEED_L          = 38
AX_PRESENT_SPEED_H          = 39
AX_PRESENT_LOAD_L           = 40
AX_PRESENT_LOAD_H           = 41
AX_PRESENT_VOLTAGE          = 42
AX_PRESENT_TEMPERATURE      = 43
AX_REGISTERED_INSTRUCTION   = 44
AX_PAUSE_TIME               = 45
AX_MOVING                   = 46
AX_LOCK                     = 47
AX_PUNCH_L                  = 48
AX_PUNCH_H                  = 49


# Function declarations of the various functions used for encoding and sending
# data from RPi to Arduino

# Write I2C block
def write_i2c_block(ard_address, block):
	try:
		return bus.write_i2c_block_data(ard_address, 1, block)
	except IOError:
		if debug:
			print ("IOError")
		return -1

# Read I2C byte
def read_i2c_byte(ard_address):
	try:
		return bus.read_byte(ard_address)
	except IOError:
		if debug:
			print ("IOError")
		return -1


# Read I2C block
def read_i2c_block(ard_address):
	try:
		return bus.read_i2c_block_data(ard_address, 1)
	except IOError:
		if debug:
			print ("IOError")
		return -1

# Arduino Digital Read
def digitalRead(pin):
	if pin < 54:
		write_i2c_block(ard_address, dRead_cmd + [pin, unused, unused, unused, unused])
		time.sleep(.1)
		n = read_i2c_byte(ard_address)
		return n
	else:
		#reset the PH1 pin to the correct value.
		if pin == JET_PH1:
			pin = pin - 100

		pin_name = "JET_" + str(pin)
		if globals()[pin_name] is not None:
			n = globals()[pin_name].read()		
			return n
		else:
			print ("You must first set the pinmode for a jetson GPIO pin.")
			return -1

# Arduino Digital Write
def digitalWrite(pin, value):
	if pin < 54:
		write_i2c_block(ard_address, dWrite_cmd + [pin, value, unused, unused, unused])
		return 1
	else:
		#reset the PH1 pin to the correct value.
		if pin == JET_PH1:
			pin = pin - 100

		pin_name = "JET_" + str(pin)
		if globals()[pin_name] is not None:
			if value > 0:
				globals()[pin_name].set()
			else:
				globals()[pin_name].reset()		
		else:
			print ("You must first set the pinmode for a jetson GPIO pin.")

# Setting Up Pin mode on Arduino
def pinMode(pin, mode):
	if pin < JET_PK1:
		#Set pin mode for Arduino pins
		if mode == OUTPUT_PIN:
			write_i2c_block(ard_address, pMode_cmd + [pin, 1, unused, unused, unused])
		elif mode == INPUT_PIN:
			write_i2c_block(ard_address, pMode_cmd + [pin, 0, unused, unused, unused])
		return 1
	else:
		#reset the PH1 pin to the correct value.
		if pin == JET_PH1:
			pin = pin - 100

		pin_name = "JET_" + str(pin)
		#Set pin mode for Jetson GPIO pins
		if mode == OUTPUT_PIN:
			globals()[pin_name] = Controller.alloc_pin(pin, OUTPUT)
		elif mode == INPUT_PIN:
			if (pin == JET_PH1 or pin == JET_PK1 or 
				pin == JET_PK2 or pin == JET_PK4):
				print ("You cannot set the output only jetson pins to inputs.")
				return -1

			globals()[pin_name] = Controller.alloc_pin(pin, INPUT)
		return 1	

# Read analog value from Pin
def analogRead(pin):
	bus.write_i2c_block_data(ard_address, 1, aRead_cmd + [pin, unused, unused, unused, unused])
	time.sleep(.1)
	bus.read_byte(ard_address)
	number = bus.read_i2c_block_data(ard_address, 1)
	time.sleep(.1)
	return number[1] * 256 + number[2]


# Write PWM
def analogWrite(pin, value):
	#print aWrite_cmd + [pin, value, unused, unused, unused]
	write_i2c_block(ard_address, aWrite_cmd + [pin, value, unused, unused, unused])
	return 1


# Servo attach
def servoAttach(pin):
	write_i2c_block(ard_address, servo_attach_cmd + [pin, unused, unused, unused, unused])
	return 1


# Servo detach
def servoDetach(pin):
	write_i2c_block(ard_address, servo_detach_cmd + [pin, unused, unused, unused, unused])
	return 1


# Servo write
def servoWrite(pin, angle):
	if angle <= 360:
		byte1 = angle & 255
		byte2 = angle >> 8
		write_i2c_block(ard_address, servo_write_cmd + [pin, byte1, byte2, unused, unused])
		return 1
	else:
		print("Invalid servo value: %d" % angle)
		return -1


# Servo read
def servoRead(pin):
	bus.write_i2c_block_data(ard_address, 1, servo_read_cmd + [pin, unused, unused, unused, unused])
	time.sleep(.1)
	bus.read_byte(ard_address)
	number = bus.read_i2c_block_data(ard_address, 1)
	time.sleep(.1)
	return number[1] * 256 + number[2]


# Read temp in Celsius from Grove Temperature Sensor
def temp(pin, model = '1.0'):
	# each of the sensor revisions use different thermistors, each with their own B value constant
	if model == '1.2':
		bValue = 4250  # sensor v1.2 uses thermistor ??? (assuming NCP18WF104F03RC until SeeedStudio clarifies)
	elif model == '1.1':
		bValue = 4250  # sensor v1.1 uses thermistor NCP18WF104F03RC
	else:
		bValue = 3975  # sensor v1.0 uses thermistor TTC3A103*39H
	a = analogRead(pin)
	resistance = (float)(1023 - a) * 10000 / a
	t = (float)(1 / (math.log(resistance / 10000) / bValue + 1 / 298.15) - 273.15)
	return t


# Read value from Grove Ultrasonic
def ultrasonicRead(pin):
	write_i2c_block(ard_address, uRead_cmd + [pin, unused, unused, unused, unused])
	time.sleep(.2)
	read_i2c_byte(ard_address)
	number = read_i2c_block(ard_address)
	return (number[1] * 256 + number[2])

# Write analog read resolution
def setAnalogReadResolution(bits):
	if bits <= 0 or bits > 12:
		print( "invalid bits specified for analog read resolution.")
		return -1

	write_i2c_block(ard_address, analog_read_prec_cmd + [bits, unused, unused, unused, unused])
	return 1

# Write analog write resolution
def setAnalogWriteResolution(bits):
	if bits <= 0 or bits > 12:
		print( "invalid bits specified for analog write resolution.")
		return -1

        write_i2c_block(ard_address, analog_write_prec_cmd + [bits, unused, unused, unused, unused])
	return 1

# Read the firmware version
def version():
	write_i2c_block(ard_address, version_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.1)
	read_i2c_byte(ard_address)
	number = read_i2c_block(ard_address)
	return "%s.%s.%s" % (number[1], number[2], number[3])


# Read Grove Accelerometer (+/- 1.5g) XYZ value
def acc_xyz():
	write_i2c_block(ard_address, acc_xyz_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.1)
	read_i2c_byte(ard_address)
	number = read_i2c_block(ard_address)
	if number[1] > 32:
		number[1] = - (number[1] - 224)
	if number[2] > 32:
		number[2] = - (number[2] - 224)
	if number[3] > 32:
		number[3] = - (number[3] - 224)
	return (number[1], number[2], number[3])


# Read from Grove RTC
def rtc_getTime():
	write_i2c_block(ard_address, rtc_getTime_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.1)
	read_i2c_byte(ard_address)
	number = read_i2c_block(ard_address)
	return number


# Read and return temperature and humidity from Grove DHT Pro
def dht(pin, module_type):
	write_i2c_block(ard_address, dht_temp_cmd + [pin, module_type, unused, unused, unused])

	# Delay necessary for proper reading fron DHT sensor
	time.sleep(.6)
	try:
		read_i2c_byte(ard_address)
		number = read_i2c_block(ard_address)
		time.sleep(.1)
		if number == -1:
			return -1
	except (TypeError, IndexError):
		return -1
	# data returned in IEEE format as a float in 4 bytes
	
	if p_version==2:
		h=''
		for element in (number[1:5]):
			h+=chr(element)
			
		t_val=struct.unpack('f', h)
		t = round(t_val[0], 2)

		h = ''
		for element in (number[5:9]):
			h+=chr(element)
		
		hum_val=struct.unpack('f',h)
		hum = round(hum_val[0], 2)
	else:
		t_val=bytearray(number[1:5])
		h_val=bytearray(number[5:9])
		t=round(struct.unpack('f',t_val)[0],2)
		hum=round(struct.unpack('f',h_val)[0],2)
	return [t, hum]

# Grove LED Bar - initialise
# orientation: (0 = red to green, 1 = green to red)
def ledBar_init(pin, orientation):
	write_i2c_block(ard_address, ledBarInit_cmd + [pin, orientation, unused, unused, unused])
	return 1

# Grove LED Bar - set orientation
# orientation: (0 = red to green,  1 = green to red)
def ledBar_orientation(pin, orientation):
	write_i2c_block(ard_address, ledBarOrient_cmd + [pin, orientation, unused, unused, unused])
	return 1

# Grove LED Bar - set level
# level: (0-10)
def ledBar_setLevel(pin, level):
	write_i2c_block(ard_address, ledBarLevel_cmd + [pin, level, unused, unused, unused])
	return 1

# Grove LED Bar - set single led
# led: which led (1-10)
# state: off or on (0-1)
def ledBar_setLed(pin, led, state):
	write_i2c_block(ard_address, ledBarSetOne_cmd + [pin, led, state, unused, unused])
	return 1

# Grove LED Bar - toggle single led
# led: which led (1-10)
def ledBar_toggleLed(pin, led):
	write_i2c_block(ard_address, ledBarToggleOne_cmd + [pin, led, unused])
	return 1

# Grove LED Bar - set all leds
# state: (0-1023) or (0x00-0x3FF) or (0b0000000000-0b1111111111) or (int('0000000000',2)-int('1111111111',2))
def ledBar_setBits(pin, state):
	byte1 = state & 255
	byte2 = state >> 8
	write_i2c_block(ard_address, ledBarSet_cmd + [pin, byte1, byte2, unused, unused])
	return 1

# Grove LED Bar - get current state
# state: (0-1023) a bit for each of the 10 LEDs
def ledBar_getBits(pin):
	write_i2c_block(ard_address, ledBarGet_cmd + [pin, unused, unused, unused, unused])
	time.sleep(.2)
	read_i2c_byte(0x04)
	block = read_i2c_block(0x04)
	return block[1] ^ (block[2] << 8)


# Grove 4 Digit Display - initialise
def fourDigit_init(pin):
	write_i2c_block(ard_address, fourDigitInit_cmd + [pin, unused, unused, unused, unused])
	return 1

# Grove 4 Digit Display - set numeric value with or without leading zeros
# value: (0-65535) or (0000-FFFF)
def fourDigit_number(pin, value, leading_zero):
	# split the value into two bytes so we can render 0000-FFFF on the display
	byte1 = value & 255
	byte2 = value >> 8
	# separate commands to overcome current 4 bytes per command limitation
	if (leading_zero):
		write_i2c_block(ard_address, fourDigitValue_cmd + [pin, byte1, byte2, unused, unused])
	else:
		write_i2c_block(ard_address, fourDigitValueZeros_cmd + [pin, byte1, byte2, unused, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set brightness
# brightness: (0-7)
def fourDigit_brightness(pin, brightness):
	# not actually visible until next command is executed
	write_i2c_block(ard_address, fourDigitBrightness_cmd + [pin, brightness, unused, unused, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set individual segment (0-9,A-F)
# segment: (0-3)
# value: (0-15) or (0-F)
def fourDigit_digit(pin, segment, value):
	write_i2c_block(ard_address, fourDigitIndividualDigit_cmd + [pin, segment, value, unused, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set 7 individual leds of a segment
# segment: (0-3)
# leds: (0-255) or (0-0xFF) one bit per led, segment 2 is special, 8th bit is the colon
def fourDigit_segment(pin, segment, leds):
	write_i2c_block(ard_address, fourDigitIndividualLeds_cmd + [pin, segment, leds, unused, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set left and right values (0-99), with leading zeros and a colon
# left: (0-255) or (0-FF)
# right: (0-255) or (0-FF)
# colon will be lit
def fourDigit_score(pin, left, right):
	write_i2c_block(ard_address, fourDigitScore_cmd + [pin, left, right, unused, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - display analogRead value for n seconds, 4 samples per second
# analog: analog pin to read
# duration: analog read for this many seconds
def fourDigit_monitor(pin, analog, duration):
	write_i2c_block(ard_address, fourDigitAnalogRead_cmd + [pin, analog, duration, unused, unused])
	time.sleep(duration + .05)
	return 1

# Grove 4 Digit Display - turn entire display on (88:88)
def fourDigit_on(pin):
	write_i2c_block(ard_address, fourDigitAllOn_cmd + [pin, unused, unused, unused, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - turn entire display off
def fourDigit_off(pin):
	write_i2c_block(ard_address, fourDigitAllOff_cmd + [pin, unused, unused, unused, unused])
	time.sleep(.05)
	return 1

# Grove Chainable RGB LED - store a color for later use
# red: 0-255
# green: 0-255
# blue: 0-255
def storeColor(red, green, blue):
	write_i2c_block(ard_address, storeColor_cmd + [red, green, blue, unused, unused])
	time.sleep(.05)
	return 1

# Grove Chainable RGB LED - initialise
# numLeds: how many leds do you have in the chain
def chainableRgbLed_init(pin, numLeds):
	write_i2c_block(ard_address, chainableRgbLedInit_cmd + [pin, numLeds, unused, unused, unused])
	time.sleep(.05)
	return 1

# Grove Chainable RGB LED - initialise and test with a simple color
# numLeds: how many leds do you have in the chain
# testColor: (0-7) 3 bits in total - a bit for red, green and blue, eg. 0x04 == 0b100 (0bRGB) == rgb(255, 0, 0) == #FF0000 == red
#            ie. 0 black, 1 blue, 2 green, 3 cyan, 4 red, 5 magenta, 6 yellow, 7 white
def chainableRgbLed_test(pin, numLeds, testColor):
	write_i2c_block(ard_address, chainableRgbLedTest_cmd + [pin, numLeds, testColor, unused, unused])
	time.sleep(.05)
	return 1

# Grove Chainable RGB LED - set one or more leds to the stored color by pattern
# pattern: (0-3) 0 = this led only, 1 all leds except this led, 2 this led and all leds inwards, 3 this led and all leds outwards
# whichLed: index of led you wish to set counting outwards from the jetduino, 0 = led closest to the jetduino
def chainableRgbLed_pattern(pin, pattern, whichLed):
	write_i2c_block(ard_address, chainableRgbLedSetPattern_cmd + [pin, pattern, whichLed, unused, unused])
	time.sleep(.05)
	return 1

# Grove Chainable RGB LED - set one or more leds to the stored color by modulo
# offset: index of led you wish to start at, 0 = led closest to the jetduino, counting outwards
# divisor: when 1 (default) sets stored color on all leds >= offset, when 2 sets every 2nd led >= offset and so on
def chainableRgbLed_modulo(pin, offset, divisor):
	write_i2c_block(ard_address, chainableRgbLedSetModulo_cmd + [pin, offset, divisor, unused, unused])
	time.sleep(.05)
	return 1

# Grove Chainable RGB LED - sets leds similar to a bar graph, reversible
# level: (0-10) the number of leds you wish to set to the stored color
# reversible (0-1) when 0 counting outwards from jetduino, 0 = led closest to the jetduino, otherwise counting inwards
def chainableRgbLed_setLevel(pin, level, reverse):
	write_i2c_block(ard_address, chainableRgbLedSetLevel_cmd + [pin, level, reverse, unused, unused])
	time.sleep(.05)
	return 1

# Grove - Infrared Receiver- get the commands received from the Grove IR sensor
def ir_read_signal():
	try:
		write_i2c_block(ard_address,ir_read_cmd+[unused,unused,unused, unused, unused])
		time.sleep(.1)
		data_back= bus.read_i2c_block_data(ard_address, 1)[0:21]
		if (data_back[1]!=255):
			return data_back
		return [-1]*21
	except IOError:
		return [-1]*21
		
# Grove - Infrared Receiver- set the pin on which the Grove IR sensor is connected
def ir_recv_pin(pin):
	write_i2c_block(ard_address,ir_recv_pin_cmd+[pin,unused,unused, unused, unused])
	
def dust_sensor_en():
	write_i2c_block(ard_address, dust_sensor_en_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	
def dust_sensor_dis():
	write_i2c_block(ard_address, dust_sensor_dis_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	
def dustSensorRead():
	write_i2c_block(ard_address, dus_sensor_read_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	#read_i2c_byte(ard_address)
	#number = read_i2c_block(ard_address)
	#return (number[1] * 256 + number[2])
	data_back= bus.read_i2c_block_data(ard_address, 1)[0:4]
	#print data_back[:4]
	if data_back[0]!=255:
		lowpulseoccupancy=(data_back[3]*256*256+data_back[2]*256+data_back[1])
		#print [data_back[0],lowpulseoccupancy]
		return [data_back[0],lowpulseoccupancy]
	else:
		return [-1,-1]
	print data_back
	
def encoder_en():
	write_i2c_block(ard_address, encoder_en_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	
def encoder_dis():
	write_i2c_block(ard_address, encoder_dis_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	
def encoderRead():
	write_i2c_block(ard_address, encoder_read_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	data_back= bus.read_i2c_block_data(ard_address, 1)[0:2]
	#print data_back
	if data_back[0]!=255:
		return [data_back[0],data_back[1]]
	else:
		return [-1,-1]
		
def flowDisable():
	write_i2c_block(ard_address, flow_disable_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	
def flowEnable():
	write_i2c_block(ard_address, flow_en_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	
def flowRead():
	write_i2c_block(ard_address, flow_read_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.2)
	data_back= bus.read_i2c_block_data(ard_address, 1)[0:3]
	#print data_back
	if data_back[0]!=255:
		return [data_back[0],data_back[2]*256+data_back[1]]
	else:
		return [-1,-1]

# Dynamixel set register. Sets a register on a Dynamixel smart servo.
def dynamixel_set_register(servo, reg, length, value):
	val0 = value & 255
	val1 = value >> 8

	write_i2c_block(ard_address, dyn_set_register_cmd + [servo, reg, length, val0, val1])
	time.sleep(.05)
	return 1

# Dynamixel get register. Gets a register on a Dynamixel smart servo.
def dynamixel_get_register(servo, reg, length):
	write_i2c_block(ard_address, dyn_get_register_cmd + [servo, reg, length, unused, unused])
	time.sleep(.1)
	bus.read_byte(ard_address)
	number = bus.read_i2c_block_data(ard_address, 1)
	#print ("number[0]: %d, number[1]: %d, number[2]: %d" % (number[0], number[1], number[2]))
	time.sleep(.1)
	return number[2] * 256 + number[1]

# Dynamixel move command. Moves a smart servo to a given position at a specified speed.
def dynamixel_move(servo, pos, speed):
	pos0 = pos & 255
	pos1 = pos >> 8

	speed0 = speed & 255
	speed1 = speed >> 8

	write_i2c_block(ard_address, dyn_move_cmd + [servo, pos0, pos1, speed0, speed1])
	time.sleep(.05)
	return 1

# Dynamixel stop synch move. Stops the servo from moving and maintains its current position.
def dynamixel_stop(servo):
	write_i2c_block(ard_address, dyn_stop_cmd + [servo, unused, unused, unused, unused])
	time.sleep(.01)
	return 1

# Dynamixel start synch move. Starts a multiple servo move sequence.
def dynamixel_start_synch_move():
	write_i2c_block(ard_address, dyn_start_synch_move_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.01)
	return 1

# Dynamixel add servo to synch move. Adds a servo movement to a synch move command
def dynamixel_add_synch_move(servo, pos, speed):
	pos0 = pos & 255
	pos1 = pos >> 8

	speed0 = speed & 255
	speed1 = speed >> 8

	write_i2c_block(ard_address, dyn_add_servo_synch_cmd + [servo, pos0, pos1, speed0, speed1])
	time.sleep(.01)
	return 1

# Dynamixel execute synch move. Signals the start of a multiple servo move sequence.
def dynamixel_execute_synch_move():
	write_i2c_block(ard_address, dyn_exec_synch_move_cmd + [unused, unused, unused, unused, unused])
	time.sleep(.01)
	return 1

# Dynamixel set endless. Turns on/off the full rotation mode or servo mode
def dynamixel_set_endless(servo, endless_on):
	write_i2c_block(ard_address, dyn_set_endless_cmd + [servo, endless_on, unused, unused, unused])
	time.sleep(.01)
	return 1

# Dynamixel turn speed.
def dynamixel_turn_speed(servo, direction, speed):
	speed0 = speed & 255
	speed1 = speed >> 8

	write_i2c_block(ard_address, dyn_set_turn_speed_cmd + [servo, direction, speed0, speed1, unused])
	time.sleep(.01)
	return 1

def mapValue(value, leftMin, leftMax, rightMin, rightMax):
	# Figure out how 'wide' each range is
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin

	# Convert the left range into a 0-1 range (float)
	valueScaled = float(value - leftMin) / float(leftSpan)

	# Convert the 0-1 range into a value in the right range.
	return rightMin + (valueScaled * rightSpan)


