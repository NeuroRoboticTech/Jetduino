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
 * SimpleGPIO.cpp
 *
 * Modifications by Derek Molloy, School of Electronic Engineering, DCU
 * www.eeng.dcu.ie/~molloyd/
 * Almost entirely based on Software by RidgeRun:
 *
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

#ifndef GROVEPI_H
#define GROVEPI_H

#include <stdio.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <fcntl.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdbool.h>

extern int fd;
extern char *fileName;
extern int  address;
extern unsigned char w_buf[6],r_buf[32];
extern unsigned long reg_addr;

#define dRead_cmd 	1
#define dWrite_cmd 	2
#define aRead_cmd 	3
#define aWrite_cmd 	4
#define pMode_cmd	5
#define ultrasonic_read_cmd      7

#define servo_attach_cmd    35
#define servo_detach_cmd    36
#define servo_write_cmd     37
#define servo_read_cmd      38

#define dyn_set_register_cmd     100
#define dyn_get_register_cmd     101
#define dyn_move_cmd             102
#define dyn_stop_cmd             103
#define dyn_set_endless_cmd      104
#define dyn_set_turn_speed_cmd   105
#define dyn_start_synch_move_cmd 106
#define dyn_add_servo_synch_cmd  107
#define dyn_exec_synch_move_cmd  108

#define SYSFS_GPIO_DIR "/sys/class/gpio"
#define POLL_TIMEOUT (3 * 1000) /* 3 seconds */
#define MAX_BUF 64
#define SYSFS_OMAP_MUX_DIR "/sys/kernel/debug/omap_mux/"

#define ARD_D0 0
#define ARD_D1 1
#define ARD_D2 2
#define ARD_D3 3
#define ARD_D4 4
#define ARD_D5 5
#define ARD_D6 6
#define ARD_D7 7
#define ARD_D8 8
#define ARD_D9 9

#define ARD_D10 10
#define ARD_D11 11
#define ARD_D12 12
#define ARD_D13 13
#define ARD_D14 14
#define ARD_D15 15
#define ARD_D16 16
#define ARD_D17 17
#define ARD_D18 18
#define ARD_D19 19

#define ARD_D20 20
#define ARD_D21 21
#define ARD_D22 22
#define ARD_D23 23
#define ARD_D24 24
#define ARD_D25 25
#define ARD_D26 26
#define ARD_D27 27
#define ARD_D28 28
#define ARD_D29 29

#define ARD_D30 30
#define ARD_D31 31
#define ARD_D32 32
#define ARD_D33 33
#define ARD_D34 34
#define ARD_D35 35
#define ARD_D36 36
#define ARD_D37 37
#define ARD_D38 38
#define ARD_D39 39

#define ARD_D40 40
#define ARD_D41 41
#define ARD_D42 42
#define ARD_D43 43
#define ARD_D44 44
#define ARD_D45 45
#define ARD_D46 46
#define ARD_D47 47
#define ARD_D48 48
#define ARD_D49 49

#define ARD_D50 50
#define ARD_D51 51
#define ARD_D52 52
#define ARD_D53 53

#define ARD_A0 54
#define ARD_A1 55
#define ARD_A2 56
#define ARD_A3 57
#define ARD_A4 58
#define ARD_A5 59
#define ARD_A6 60
#define ARD_A7 61
#define ARD_A8 62
#define ARD_A9 63
#define ARD_A10 64
#define ARD_A11 65

#define JET_A0 100
#define JET_A1 101
#define JET_A2 102
#define JET_A3 103

// This one is really 57, but I had to increase it to get it
// out of the range of the other digital lines.
#define JET_PH1 157

#define JET_PK1 81
#define JET_PK2 82
#define JET_PK4 84

#define JET_PU0 160
#define JET_PU1 161
#define JET_PU2 162
#define JET_PU3 163
#define JET_PU4 164
#define JET_PU5 165
#define JET_PU6 166

typedef enum {
	INPUT_PIN=0,
	OUTPUT_PIN=1
} PIN_DIRECTION;

typedef enum {
	LOW=0,
	HIGH=1
} PIN_VALUE;


//Initialize
int openJetduino(void);
int closeJetduino(void);

//Write a register
int write_block(char cmd,char v1,char v2,char v3,char v4,char v5);
//Read 1 byte of data
char read_byte(void);

void pi_sleep(int);
int analogRead(int pin);
int digitalWrite(int pin, PIN_VALUE value);
int pinMode(int pin, PIN_DIRECTION mode);
int digitalRead(int pin);
int analogWrite(int pin,int value);
float temperatureRead(int pin, int model);
int ultrasonicRead(int pin);

int dynamixelMove(int servo, int pos, int speed);

//Simple GPIO code
int gpio_export(unsigned int gpio);
int gpio_unexport(unsigned int gpio);
int gpio_set_dir(unsigned int gpio, PIN_DIRECTION out_flag);
int gpio_set_value(unsigned int gpio, bool value);
int gpio_get_value(unsigned int gpio, unsigned int *value);
int gpio_set_edge(unsigned int gpio, char *edge);
int gpio_fd_open(unsigned int gpio);
int gpio_fd_close(int fd);
int gpio_omap_mux_setup(const char *omap_pin0_name, const char *mode);

#endif /*GROVEPI_H */


