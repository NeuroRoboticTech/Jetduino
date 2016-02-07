# Tweet the temperature, light, and sound levels with the Jetduino
# http://NeuroRoboticTech/Products/GrovePi/JetduinoProjects/SensorTwitterFeed/

# Jetduino + Sound Sensor + Light Sensor + Temperature Sensor + LED
# http://www.seeedstudio.com/wiki/Grove_-_Sound_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro
# http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit

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
'''

import twitter
import time
import jetduino
from jetduino_pins import *
import math

# Connections
sound_sensor = ARD_A0        # port A0
light_sensor = ARD_A1        # port A1 
temperature_sensor = ARD_D4  # port D4
led = ARD_D3                 # port D3

# Connect to Twitter
api = twitter.Api(consumer_key='YourKey',consumer_secret='YourKey',access_token_key='YourKey',access_token_secret='YourKey')
print "Twitter Connected"

jetduino.pinMode(led,"OUTPUT")

last_sound = 0

while True:
    # Error handling in case of problems communicating with the GrovePi
    try:
        # Get value from temperature sensor
        [temp,humidity] = jetduino.dht(temperature_sensor,0)
        t=temp

        # Get value from light sensor
        light_intensity = jetduino.analogRead(light_sensor)

        # Give PWM output to LED
        jetduino.analogWrite(led,light_intensity/4)

        # Get sound level
        sound_level = jetduino.analogRead(sound_sensor)
        if sound_level > 0:
            last_sound = sound_level

        # Post a tweet
        print ("DI Lab's Temp: %.2f, Light: %d, Sound: %d" %(t,light_intensity/10,last_sound))
        api.PostUpdate("DI Lab's Temp: %.2f, Light: %d, Sound: %d" %(t,light_intensity/10,last_sound))
        time.sleep(3)
    except IOError:
        print "Error"
    except:
        print "Duplicate Tweet"
