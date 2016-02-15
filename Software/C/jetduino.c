// jetduino C library
// v0.1
//
// This library provides the basic functions for using the jetduino in C
//
// The Jetduino connects the Jetson and Grove sensors.  You can learn more about the Jetduino here:  http://www.NeuroRoboticTech.com/Projects/Jetduino
//
// Have a question about this example?  Ask on the forums here:  http://www.NeuroRoboticTech.com/Forum
//
// 	History
// 	------------------------------------------------
// 	Author		Date      		Comments
//	Karan		28 Dec 15		Initial Authoring
//	David COfer	31 Jan 16		Converted to use for Jetduino

/*
License

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
*/

/*
 * SimpleGPIO.h
 *
 * Copyright Derek Molloy, School of Electronic Engineering, Dublin City University
 * www.eeng.dcu.ie/~molloyd/
 *
 * Based on Software by RidgeRun
 * Copyright (c) 2011, RidgeRun
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *    This product includes software developed by the RidgeRun.
 * 4. Neither the name of the RidgeRun nor the
 *    names of its contributors may be used to endorse or promote products
 *    derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY RIDGERUN ''AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL RIDGERUN BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include "jetduino.h"
#include <math.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <poll.h>

int fd;
char *fileName = "/dev/i2c-1";
int  address = 0x04;
unsigned char w_buf[6],ptr,r_buf[32];
unsigned long reg_addr=0;

#define dbg 0
int openJetduino(void)
{
	if ((fd = open(fileName, O_RDWR)) < 0)
	{					// Open port for reading and writing
		printf("Failed to open i2c port\n");
		return -1;
	}

	if (ioctl(fd, I2C_SLAVE, address) < 0)
	{					// Set the port options and set the address of the device
		printf("Unable to get bus access to talk to slave\n");
		return -1;
	}

	if(gpio_export((unsigned int) (JET_PH1-100)) != 0) {
		printf("Error exporting PH1\n");
		return -1;
    }
    else {
        if(gpio_set_dir((unsigned int) (JET_PH1-100),
                        OUTPUT_PIN) != 0) {
            printf("Error setting pin mode of PH1\n");
        }
    }

	if(gpio_export(JET_PK1) != 0) {
		printf("Error exporting PK1\n");
		return -1;
    }
    else {
        if(gpio_set_dir(JET_PK1, OUTPUT_PIN) != 0) {
            printf("Error setting pin mode of PH1\n");
        }
    }

	if(gpio_export(JET_PK2) != 0) {
		printf("Error exporting PK2\n");
		return -1;
    }
    else {
        if(gpio_set_dir(JET_PK1, OUTPUT_PIN) != 0) {
            printf("Error setting pin mode of PK2\n");
        }
    }

	if(gpio_export(JET_PK4) != 0) {
		printf("Error exporting PK4\n");
		return -1;
    }
    else {
        if(gpio_set_dir(JET_PK1, OUTPUT_PIN) != 0) {
            printf("Error setting pin mode of PK4\n");
        }
    }

	if(gpio_export(JET_PU0) != 0) {
		printf("Error exporting PU0\n");
		return -1;
    }

	if(gpio_export(JET_PU1) != 0) {
		printf("Error exporting PU1\n");
		return -1;
    }

	if(gpio_export(JET_PU2) != 0) {
		printf("Error exporting PU2\n");
		return -1;
    }

	if(gpio_export(JET_PU3) != 0) {
		printf("Error exporting PU3\n");
		return -1;
    }

	if(gpio_export(JET_PU4) != 0) {
		printf("Error exporting PU4\n");
		return -1;
    }

	if(gpio_export(JET_PU5) != 0) {
		printf("Error exporting PU5\n");
		return -1;
    }

	if(gpio_export(JET_PU6) != 0) {
		printf("Error exporting PU6\n");
		return -1;
    }

	return 1;
}

int closeJetduino()
{
    int ret = 0;

    if(close(fd) != 0) {
		printf("Error closing I2C line.\n");
		ret = -1;
    }

	if(gpio_unexport((unsigned int) (JET_PH1-100)) != 0) {
		printf("Error unexporting PH1\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PK1) != 0) {
		printf("Error unexporting PK1\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PK2) != 0) {
		printf("Error unexporting PK2\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PK4) != 0) {
		printf("Error unexporting PK4\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PU0) != 0) {
		printf("Error unexporting PU0\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PU1) != 0) {
		printf("Error unexporting PU1\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PU2) != 0) {
		printf("Error unexporting PU2\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PU3) != 0) {
		printf("Error unexporting PU3\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PU4) != 0) {
		printf("Error unexporting PU4\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PU5) != 0) {
		printf("Error unexporting PU5\n");
		ret = -1;
    }

	if(gpio_unexport(JET_PU6) != 0) {
		printf("Error unexporting PU6\n");
		ret = -1;
    }

	return ret;
}

//Write a register
int write_block(char cmd,char v1,char v2,char v3,char v4,char v5)
{
	int dg;
	w_buf[0]=cmd;
    w_buf[1]=v1;
    w_buf[2]=v2;
    w_buf[3]=v3;
    w_buf[4]=v4;
    w_buf[5]=v5;

    dg=i2c_smbus_write_i2c_block_data(fd,1,6,w_buf);

	if (dbg)
		printf("wbk: %d\n",dg);

    // if (i2c_smbus_write_i2c_block_data(fd,1,6,w_buf) != 7)
    // {
        // printf("Error writing to Jetduino\n");
        // return -1;
    // }
    return 1;
}

//write a byte to the Jetduino
int write_byte(char b)
{
    w_buf[0]=b;
    if ((write(fd, w_buf, 1)) != 1)
    {
        printf("Error writing to Jetduino\n");
        return -1;
    }
    return 1;
}

//Read 1 byte of data
char read_byte(void)
{
    //read(fd, r_buf, 1);

	r_buf[0]=i2c_smbus_read_byte(fd);
	if (dbg)
		printf("rbt: %d\n",r_buf[0]);
	// if (read(fd, r_buf, reg_size) != reg_size) {
		// printf("Unable to read from Jetduino\n");
		// //exit(1);
        // return -1;
	// }

    return r_buf[0];
}

//Read a block of data from the Jetduino
char read_block(int size)
{
    int ret;
    ret=i2c_smbus_read_i2c_block_data(fd,1,size,&r_buf[0]);

	if(dbg) {
		printf("rbk: %d\n",ret);
	}

	 if (ret != size) {
		 printf("Unable to read from Jetduino\n");
         return -1;
	 }

    return 1;
}

void jet_sleep(int t)
{
	usleep(t*1000);
}

// Read analog value from Pin
int analogRead(int pin)
{
	int data;
	write_block(aRead_cmd,pin,0,0,0,0);
	usleep(1000);
	read_block(3);
	data=r_buf[1]* 256 + r_buf[2];
	if (data==65535)
		return -1;
	return data;
}

//Write a digital value to a pin
int digitalWrite(int pin, PIN_VALUE value)
{
    if(pin < JET_PK1) {
        return write_block(dWrite_cmd,pin,value,0,0,0);
    }
    else {
        //If it is the PH1 pin then make it the correct value.
        if(pin == JET_PH1) {
            pin -= 100;
        }

        return gpio_set_value((unsigned int) pin, value);
    }
}

//Set the mode of a pin
//mode
//	1: 	output
//	0:	input
int pinMode(int pin, PIN_DIRECTION mode)
{
    if(pin < JET_PK1) {
        return write_block(pMode_cmd,pin,mode,0,0,0);
    }
    else {
        if(pin == JET_PH1 || pin == JET_PK1 ||
           pin == JET_PK2 || pin == JET_PK4) {
            printf("Cannot set the pin mode for output only jetson GPIO lines.");
            return -1;
        }
        else {
            return gpio_set_dir((unsigned int) pin, mode);
        }
    }
}

//Read a digital value from a pin
int digitalRead(int pin)
{
    if(pin < JET_PK1) {
        write_block(dRead_cmd,pin,0,0,0,0);
        usleep(10000);
        return read_byte();
    }
    else {
        //If it is the PH1 pin then make it the correct value.
        if(pin == JET_PH1) {
            pin -= 100;
        }

        unsigned int val=0;
        gpio_get_value((unsigned int) pin, &val);
        return val;
    }
}

//Write a PWM value to a pin
int analogWrite(int pin,int value)
{
	return write_block(aWrite_cmd,pin,value,0,0,0);
}

int servoAttach(int pin)
{
	return write_block(servo_attach_cmd,pin,0,0,0,0);
}

int servoDetach(int pin)
{
	return write_block(servo_detach_cmd,pin,0,0,0,0);
}

int servoWrite(int pin, int angle)
{
     if (angle < 0 || angle > 360) {
		 printf("Invalid angle specified  %d\\n", angle);
         return -1;
	 }

    int byte1 = angle & 255;
    int byte2 = angle >> 8;
	return write_block(servo_write_cmd,pin,byte1,byte2,0,0);
}

// Read servo value from Pin
int servoRead(int pin)
{
	int data;
	write_block(servo_read_cmd,pin,0,0,0,0);
	usleep(1000);
	read_block(3);
	data=r_buf[1]* 256 + r_buf[2];
	if (data==65535)
		return -1;
	return data;
}

float temperatureRead(int pin, int model)
{
    float bValue;
	if(model == 2) {
		bValue = 4250.0f;  // sensor v1.2 uses thermistor ??? (assuming NCP18WF104F03RC until SeeedStudio clarifies)
	}
	else if(model == 1) {
		bValue = 4250.0f;  // sensor v1.1 uses thermistor NCP18WF104F03RC
	}
	else {
		bValue = 3975.0f;  // sensor v1.0 uses thermistor TTC3A103*39H
	}
	int a = analogRead(pin);
	float resistance = (float)(1023 - a) * 10000.0f / a;
	float t = (float)(1 / (log(resistance / 10000) / bValue + 1 / 298.15) - 273.15);
	return t;
}

int ultrasonicRead(int pin)
{
	int data;
	write_block(ultrasonic_read_cmd,pin,0,0,0,0);
	usleep(1000);
	read_block(3);
	data=r_buf[1]* 256 + r_buf[2];
	if (data==65535)
		return -1;
	return data;
}

int setAnlogReadResolution(int bits)
{
	return write_block(analog_read_prec_cmd,bits,0,0,0,0);
}

int setAnlogWriteResolution(int bits)
{
	return write_block(analog_write_prec_cmd,bits,0,0,0,0);
}

int dynamixelSetRegister(int servo, int reg, int length, int value)
{
    int val0 = value & 255;
    int val1 = value >> 8;

	int ret = write_block(dyn_set_register_cmd,servo,reg,length,val0,val1);
	jet_sleep(50);
	return ret;
}

int dynamixelGetRegister(int servo, int reg, int length)
{
	int data;
	write_block(dyn_get_register_cmd,servo,reg,length,0,0);
	usleep(1000);
	read_block(3);
	data=r_buf[2]* 256 + r_buf[1];
	if (data==65535)
		return -1;

	jet_sleep(50);
	return data;
}

int dynamixelMove(int servo, int pos, int speed)
{
    int pos0 = pos & 255;
    int pos1 = pos >> 8;

    int speed0 = speed & 255;
    int speed1 = speed >> 8;

	int ret = write_block(dyn_move_cmd,servo,pos0,pos1,speed0,speed1);
	jet_sleep(50);
	return ret;
}

int dynamixelStop(int servo)
{
	int ret = write_block(dyn_stop_cmd,servo,0,0,0,0);
	jet_sleep(50);
	return ret;
}

int dynamixelStartSynchMove()
{
	int ret = write_block(dyn_start_synch_move_cmd,0,0,0,0,0);
	jet_sleep(50);
	return ret;
}

int dynamixelAddSynchMove(int servo, int pos, int speed)
{
    int pos0 = pos & 255;
    int pos1 = pos >> 8;

    int speed0 = speed & 255;
    int speed1 = speed >> 8;

	int ret = write_block(dyn_add_servo_synch_cmd,servo,pos0,pos1,speed0,speed1);
	jet_sleep(50);
	return ret;
}

int dynamixelExecuteSynchMove()
{
	int ret = write_block(dyn_exec_synch_move_cmd,0,0,0,0,0);
	jet_sleep(50);
	return ret;
}

int dynamixelsetEndless(int servo, int status)
{
	int ret = write_block(dyn_set_endless_cmd,servo,status,0,0,0);
	jet_sleep(50);
	return ret;
}

int dynamixelSetTurnSpeed(int servo, int direction, int speed)
{
    int speed0 = speed & 255;
    int speed1 = speed >> 8;

	int ret = write_block(dyn_set_turn_speed_cmd,servo,direction,speed0,speed1,0);
	jet_sleep(50);
	return ret;
}


/****************************************************************
 * gpio_export
 ****************************************************************/
int gpio_export(unsigned int gpio)
{
	int fd, len;
	char buf[MAX_BUF];

	fd = open(SYSFS_GPIO_DIR "/export", O_WRONLY);
	if (fd < 0) {
		perror("gpio/export");
		return fd;
	}

	len = snprintf(buf, sizeof(buf), "%d", gpio);
	write(fd, buf, len);
	close(fd);

	return 0;
}

/****************************************************************
 * gpio_unexport
 ****************************************************************/
int gpio_unexport(unsigned int gpio)
{
	int fd, len;
	char buf[MAX_BUF];

	fd = open(SYSFS_GPIO_DIR "/unexport", O_WRONLY);
	if (fd < 0) {
		perror("gpio/export");
		return fd;
	}

	len = snprintf(buf, sizeof(buf), "%d", gpio);
	write(fd, buf, len);
	close(fd);
	return 0;
}

/****************************************************************
 * gpio_set_dir
 ****************************************************************/
int gpio_set_dir(unsigned int gpio, PIN_DIRECTION out_flag)
{
	int fd;
	char buf[MAX_BUF];

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR  "/gpio%d/direction", gpio);

	fd = open(buf, O_WRONLY);
	if (fd < 0) {
		perror("gpio/direction");
		return fd;
	}

	if (out_flag == OUTPUT_PIN)
		write(fd, "out", 4);
	else
		write(fd, "in", 3);

	close(fd);
	return 0;
}

/****************************************************************
 * gpio_set_value
 ****************************************************************/
int gpio_set_value(unsigned int gpio, bool value)
{
	int fd;
	char buf[MAX_BUF];

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/value", gpio);

	fd = open(buf, O_WRONLY);
	if (fd < 0) {
		perror("gpio/set-value");
		return fd;
	}

	if (value==false)
		write(fd, "0", 2);
	else
		write(fd, "1", 2);

	close(fd);
	return 0;
}

/****************************************************************
 * gpio_get_value
 ****************************************************************/
int gpio_get_value(unsigned int gpio, unsigned int *value)
{
	int fd;
	char buf[MAX_BUF];
	char ch;

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/value", gpio);

	fd = open(buf, O_RDONLY);
	if (fd < 0) {
		perror("gpio/get-value");
		return fd;
	}

	read(fd, &ch, 1);

	if (ch != '0') {
		*value = 1;
	} else {
		*value = 0;
	}

	close(fd);
	return 0;
}


/****************************************************************
 * gpio_set_edge
 ****************************************************************/

int gpio_set_edge(unsigned int gpio, char *edge)
{
	int fd;
	char buf[MAX_BUF];

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/edge", gpio);

	fd = open(buf, O_WRONLY);
	if (fd < 0) {
		perror("gpio/set-edge");
		return fd;
	}

	write(fd, edge, strlen(edge) + 1);
	close(fd);
	return 0;
}

/****************************************************************
 * gpio_fd_open
 ****************************************************************/

int gpio_fd_open(unsigned int gpio)
{
	int fd;
	char buf[MAX_BUF];

	snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/value", gpio);

	fd = open(buf, O_RDONLY | O_NONBLOCK );
	if (fd < 0) {
		perror("gpio/fd_open");
	}
	return fd;
}

/****************************************************************
 * gpio_fd_close
 ****************************************************************/

int gpio_fd_close(int fd)
{
	return close(fd);
}


/****************************************************************
 * gpio_omap_mux_setup - Allow us to setup the omap mux mode for a pin
 ****************************************************************/
int gpio_omap_mux_setup(const char *omap_pin0_name, const char *mode)
{
	int fd;
	char buf[MAX_BUF];
	snprintf(buf, sizeof(buf), SYSFS_OMAP_MUX_DIR "%s", omap_pin0_name);
	fd = open(buf, O_WRONLY);
	if (fd < 0) {
		perror("failed to open OMAP_MUX");
		return fd;
	}
	write(fd, mode, strlen(mode) + 1);
	close(fd);
	return 0;
}
