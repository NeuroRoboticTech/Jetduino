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

extern int fd;
extern char *fileName;
extern int  address;
extern unsigned char w_buf[5],r_buf[32];
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

//Initialize
int init(void);
//Write a register
int write_block(char cmd,char v1,char v2,char v3);
//Read 1 byte of data
char read_byte(void);

void pi_sleep(int); 
int analogRead(int pin);
int digitalWrite(int pin,int value);
int pinMode(int pin,int mode);
int digitalRead(int pin);
int analogWrite(int pin,int value);
float temperatureRead(int pin, int model);
int ultrasonicRead(int pin);
#endif /*GROVEPI_H */
