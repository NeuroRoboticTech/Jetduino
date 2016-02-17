#include <Wire.h>
#include "MMA7660.h"
#include "DS1307.h"
#include "DHT.h"
#include "Grove_LED_Bar.h"
#include "TM1637.h"
#include "ChainableLED.h"
//#include "IRSendRev.h"
//#include "Encoder.h"
//#include "TimerOne.h"
#include <Servo.h> 

#define INCLUDE_DYNAMIXEL

#ifdef INCLUDE_DYNAMIXEL
  #include "DynamixelSerial.h"
  DynamixelSerial dynamixel;
#endif

MMA7660 acc;
DS1307 ds_clock;
DHT dht;
Grove_LED_Bar ledbar[6];  // 7 instances for D2-D8, however, max 4 bars, you can't use adjacent sockets, 4 pin display
TM1637 fourdigit[6];      // 7 instances for D2-D8, however, max 4 displays, you can't use adjacent sockets, 4 pin display
ChainableLED rgbled[6];   // 7 instances for D2-D8

#define SLAVE_ADDRESS 0x04

//Command Values
#define CMD_DIGITAL_READ         1
#define CMD_DIGITAL_WRITE        2
#define CMD_ANALOG_READ          3
#define CMD_ANALOG_WRITE         4
#define CMD_PIN_MODE             5

#define CMD_ULTRASONIC_READ      7
#define CMD_FIRMWARE_VERSION     8

#define CMD_DUST_SENSOR_READ     10
#define CMD_ENCODER_READ         11
#define CMD_FLOW_READ            12
#define CMD_FLOW_DIS             13
#define CMD_DUST_SENSOR_EN       14
#define CMD_DUST_SENSOR_DIS      15
#define CMD_ENCODER_EN           16
#define CMD_ENCODER_DIS          17
#define CMD_FLOW_EN              18

#define CMD_ACCEl_XYZ_READ       20
#define CMD_IR_RECV              21
#define CMD_IR_RECV_PIN_SET      22

#define CMD_RTC_TIME_READ        30
#define CMD_ANALOG_READ_RES      31
#define CMD_ANALOG_WRITE_RES     32

#define CMD_SERVO_ATTACH         35
#define CMD_SERVO_DETACH         36
#define CMD_SERVO_WRITE          37
#define CMD_SERVO_READ           38

#define CMD_TEMP_HUMIDITY_READ   40

#define CMD_LED_BAR_INIT         50
#define CMD_LED_BAR_SET_GTOR     51
#define CMD_LED_BAR_SET_LEVEL    52
#define CMD_LED_BAR_SET_LED      53
#define CMD_LED_BAR_TOGGLE_LED   54
#define CMD_LED_BAR_SET_STATE    55
#define CMD_LED_BAR_RET_STATE    56

#define CMD_4D_INIT              70
#define CMD_4D_SET_BRIGHT        71
#define CMD_4D_VAL_W_ZERO        72
#define CMD_4D_VAL_WO_ZERO       73
#define CMD_4D_SET_DIGIT         74
#define CMD_4D_SET_SEGMENT       75
#define CMD_4D_SET_COLON         76
#define CMD_4D_ANALOG_READ       77
#define CMD_4D_DISPLAY_ON        78
#define CMD_4D_DISPLAY_OFF       79

#define CMD_CLED_STORE_COLOR     90
#define CMD_CLED_INIT_CHAIN      91
#define CMD_CLED_INIT_SET_TEST   92
#define CMD_CLED_SET_PATTERN     93
#define CMD_CLED_SET_MODULO      94
#define CMD_CLED_SET_lEVEL       95

#define CMD_DYN_SET_REGISTER     100
#define CMD_DYN_GET_REGISTER     101
#define CMD_DYN_MOVE             102
#define CMD_DYN_STOP             103
#define CMD_DYN_SET_ENDLESS      104
#define CMD_DYN_SET_TURN_SPEED   105
#define CMD_DYN_START_SYNCH_MOVE 106
#define CMD_DYN_ADD_SERVO_SYNCH  107
#define CMD_DYN_EXEC_SYNCH_MOVE  108

//Servo pin numbers start at 2, but array starts at 0
#define SERVO_PIN_OFFSET 2

//Array of pointers to servos 
//used for attaching with and controlling servos.
Servo *servos[11];
int servoRead = 0;

int cmd[6];
int idx=0;
int flag=0;
int i;
byte val=0,b[21],float_array[4],dht_b[21];
unsigned char dta[21];
int length;
int aRead=0;
byte accFlag=0,clkFlag=0;
int8_t accv[3];
byte rgb[] = { 0, 0, 0 };
int run_once;

//Dust sensor variables:
unsigned long starttime;
unsigned long sampletime_ms = 30000;//sample 30s ;
unsigned long lowpulseoccupancy = 0, latest_dust_val=0;
unsigned long t, pulse_end,pulse_start,duration;
int dust_run_bk=0;
int dust_latest=0;
int l_status;

//Encoder variable
int index_LED;
byte enc_val[2];        //Given it's own I2C buffer so that it does not corrupt the data from other sensors when running in background 
int enc_run_bk=0;   //Flag for first time setup

//Flow sensor variables
volatile int NbTopsFan; //measuring the rising edges of the signal
int Calc;                               
int hallsensor = 2;    //The pin location of the sensor
int flow_run_bk=0;
long flow_read_start;
byte flow_val[3];        //Given it's own I2C buffer so that it does not corrupt the data from other sensors when running in background 

#ifdef INCLUDE_DYNAMIXEL

void dynamixelSetRegister()
{
  byte servo = cmd[1];
  byte reg = cmd[2];
  byte length = cmd[3];
  byte value0 = cmd[4];
  byte value1 = cmd[5];

  //Serial.print("Set Dynamixel register");
  //Serial.print(", servo: "); Serial.print(servo);
  //Serial.print(", reg: "); Serial.print(reg);
  //Serial.print(", length: "); Serial.print(length);
  //Serial.print(", val0: "); Serial.print(value0);
  //Serial.print(", val1: "); Serial.print(value1);

  if(length == 1) {
    dynamixel.setRegister(servo, reg, value0);
    //Serial.println("");
  }
  else {
    int value = dynamixel.makeWord(value0, value1);
    dynamixel.setRegister2(servo, reg, value);

    //Serial.print(", val: "); Serial.println(value);
  }
}

void dynamixelGetRegister()
{
  byte servo = cmd[1];
  byte reg = cmd[2];
  byte length = cmd[3];
  int regVal = dynamixel.readRegister(servo, reg, length);

  //Serial.print("Get Dynamixel register");
  //Serial.print(", servo: "); Serial.print(servo);
  //Serial.print(", reg: "); Serial.print(reg);
  //Serial.print(", length: "); Serial.print(length);
  //Serial.print(", value: "); Serial.print(regVal);

  if(length == 1) {
    b[1] = regVal;
    b[2] = 0;
  }
  else {
    b[1] = dynamixel.getLowByte(regVal);
    b[2] = dynamixel.getHighByte(regVal);
  }

  //Serial.print(", b0: "); Serial.print(b[0]);
  //Serial.print(", b1: "); Serial.print(b[1]);
  //Serial.print(", b2: "); Serial.println(b[2]);
}

void dynamixelMove()
{
  byte servo = cmd[1];
  byte pos0 = cmd[2];
  byte pos1 = cmd[3];
  byte speed0 = cmd[4];
  byte speed1 = cmd[5];

  int pos = dynamixel.makeWord(pos0, pos1);
  int speed = dynamixel.makeWord(speed0, speed1);

  //Serial.print("Dynamixel Move");
  //Serial.print(", servo: "); Serial.print(servo);
  //Serial.print(", pos: "); Serial.print(pos);
  //Serial.print(", speed: "); Serial.println(speed);
  
  dynamixel.moveSpeed(servo, pos, speed);
}

void dynamixelStop()
{
  byte servo = cmd[1];

  //Serial.print("Dynamixel Stop");
  //Serial.print(", servo: "); Serial.println(servo);
  
  dynamixel.stop(servo);
}

void dynamixelSetEndless()
{
  byte servo = cmd[1];
  byte status = cmd[2];

  //Serial.print("Dynamixel Set Endless");
  //Serial.print(", servo: "); Serial.print(servo);
  //Serial.print(", status: "); Serial.println(status);

  dynamixel.setEndless(servo, status);
}

void dynamixelSetTurnSpeed()
{
  byte servo = cmd[1];
  byte side = cmd[2];
  byte speed0 = cmd[3];
  byte speed1 = cmd[4];

  int speed = dynamixel.makeWord(speed0, speed1);

  //Serial.print("Dynamixel Set turn speed");
  //Serial.print(", servo: "); Serial.print(servo);
  //Serial.print(", side: "); Serial.print(side);
  //Serial.print(", speed: "); Serial.println(speed);

  dynamixel.turn(servo, side, speed);
}

void dynamixelStartSynchMove()
{
  //Serial.println("Dynamixel Start Synch Move");

  dynamixel.startSyncWrite(true);
}

void dynamixelAddToSynchMove()
{
  byte servo = cmd[1];
  byte pos0 = cmd[2];
  byte pos1 = cmd[3];
  byte speed0 = cmd[4];
  byte speed1 = cmd[5];

  int pos = dynamixel.makeWord(pos0, pos1);
  int speed = dynamixel.makeWord(speed0, speed1);

  //Serial.print("Dynamixel Add To Synch Move");
  //Serial.print(", servo: "); Serial.print(servo);
  //Serial.print(", pos: "); Serial.print(pos);
  //Serial.print(", speed: "); Serial.println(speed);
  
  dynamixel.addServoToSync(servo, pos, speed);
}

void dynamixelExecuteSynchMove()
{
  //Serial.println("Dynamixel Execute Synch Move");

  dynamixel.writeSyncData();
}
#endif

void setup()
{
    Serial.begin(57600);         // start serial for output
    
    Wire.begin(SLAVE_ADDRESS);

    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);
	  attachInterrupt(0,readPulseDust,CHANGE);

    Serial.println("Finished Setup");

#ifdef INCLUDE_DYNAMIXEL
    dynamixel.begin(); 
#endif    
}


int pin;
int j;
void loop()
{
  long dur,RangeCm;
  if(idx==6)
  {
    flag=1;
    //IR reciever pin set command
    if(cmd[0]==CMD_IR_RECV_PIN_SET) 
    {
       //IR.Init(cmd[1]);
    }    
    //Grove IR recieve command
    else if(cmd[0]==CMD_IR_RECV)
    {/*
        if(IR.IsDta())
        {
            int length= IR.Recv(dta);
            b[0]=1;
            for(i=0;i<20;i++) 
                b[i+1]=dta[i];
        }
        */
    }
    
    //Digital Read
    else if(cmd[0]==CMD_DIGITAL_READ)
    {
      val=digitalRead(cmd[1]);

      //Serial.print("Digital Read. Pin: ");
      //Serial.print(cmd[1]);
      //Serial.print(", Value: ");
      //Serial.println(val);
    }
    //Digital Write
    else if(cmd[0]==CMD_DIGITAL_WRITE)
      digitalWrite(cmd[1],cmd[2]);

    //Analog Read
    else if(cmd[0]==CMD_ANALOG_READ)
    {
      aRead=analogRead(cmd[1]);
      b[1]=aRead/256;
      b[2]=aRead%256;

      //Serial.print("Analog Read. Pin: ");
      //Serial.print(cmd[1]);
      //Serial.print(", Value: ");
      //Serial.println(aRead);
      //run_once = false;
    }

    //Set up Analog Write
    else if(cmd[0]==CMD_ANALOG_WRITE && run_once)
    {
      analogWrite(cmd[1],cmd[2]);

      //Serial.print("Analog Write. Pin: ");
      //Serial.print(cmd[1]);
      //Serial.print(", Value: ");
      //Serial.println(cmd[2]);
      run_once = false;
    }
    //Set up pinMode
    else if(cmd[0]==CMD_PIN_MODE)
    {
      pinMode(cmd[1],cmd[2]);
      
      //Serial.print("Set pin mode. Pin: ");
      //Serial.print(cmd[1]);
      //Serial.print(", Mode: ");
      //Serial.println(cmd[2]);
    }
    //Ultrasonic Read
    else if(cmd[0]==CMD_ULTRASONIC_READ)
    {
      pin=cmd[1];
      pinMode(pin, OUTPUT);
      digitalWrite(pin, LOW);
      delayMicroseconds(2);
      digitalWrite(pin, HIGH);
      delayMicroseconds(5);
      digitalWrite(pin,LOW);
      pinMode(pin,INPUT);
      dur = pulseIn(pin,HIGH);
      RangeCm = dur/29/2;
      b[1]=RangeCm/256;
      b[2]=RangeCm%256;
      //Serial.println(b[1]);
      //Serial.println(b[2]);
    }
    //Firmware version
    else if(cmd[0]==CMD_FIRMWARE_VERSION)
    {
      b[1] = 1;
      b[2] = 2;
      b[3] = 6;
    }
    //Accelerometer x,y,z, read
    else if(cmd[0]==CMD_ACCEl_XYZ_READ)
    {
      if(accFlag==0)
      {
        acc.init();
        accFlag=1;
      }
      acc.getXYZ(&accv[0],&accv[1],&accv[2]);
      b[1]=accv[0];
      b[2]=accv[1];
      b[3]=accv[2];
    }
    //RTC tine read
    else if(cmd[0]==CMD_RTC_TIME_READ)
    {
      if(clkFlag==0)
      {
        ds_clock.begin();
        //Set time the first time
        //ds_clock.fillByYMD(2013,1,19);
        //ds_clock.fillByHMS(15,28,30);//15:28 30"
        //ds_clock.fillDayOfWeek(SAT);//Saturday
        //ds_clock.setTime();//write time to the RTC chip
        clkFlag=1;
      }
      ds_clock.getTime();
      b[1]=ds_clock.hour;
      b[2]=ds_clock.minute;
      b[3]=ds_clock.second;
      b[4]=ds_clock.month;
      b[5]=ds_clock.dayOfMonth;
      b[6]=ds_clock.year;
      b[7]=ds_clock.dayOfMonth;
      b[8]=ds_clock.dayOfWeek;
    }
    else if(cmd[0]==CMD_ANALOG_READ_RES && run_once)
    {
      int bits = cmd[1];

      Serial.print("Analog Read Res. Bits: ");
      Serial.println(bits);

      if(bits > 0 && bits <= 12) {
        analogReadResolution(bits);              
      }
      else {
        Serial.print("Invalid bits set for analog read resolution. Bits: ");
        Serial.println(bits);
      }
      run_once = false;
    }
    else if(cmd[0]==CMD_ANALOG_WRITE_RES && run_once)
    {
      int bits = cmd[1];

      Serial.print("Analog Write Res. Bits: ");
      Serial.println(bits);

      if(bits > 0 && bits <=12) {
        analogWriteResolution(bits);              
      }
      else {
        Serial.print("Invalid bits set for analog write resolution. Bits: ");
        Serial.println(bits);
      }
      run_once = false;
    }
    else if(cmd[0]==CMD_SERVO_ATTACH && run_once)
    {
      //Servo pins on Due are offset by 2
      int pin = cmd[1];
      int pin_idx = pin-SERVO_PIN_OFFSET; 

      //Serial.print("Servo Attach. Pin: ");
      //Serial.println(pin);

      if(servos[pin_idx] == nullptr) {
        servos[pin_idx] = new Servo;
      }

      servos[pin_idx]->attach(pin);
      run_once = false;
    }
    else if(cmd[0]==CMD_SERVO_DETACH && run_once)
    {
      //Servo pins on Due are offset by 2
      int pin = cmd[1];
      int pin_idx = pin-SERVO_PIN_OFFSET; 

      //Serial.print("Servo Detach. Pin: ");
      //Serial.println(pin);
      
      if(servos[pin_idx] != nullptr) {
        servos[pin_idx]->detach();

        //delete the servo
        delete servos[pin_idx];
        servos[pin_idx] = nullptr;
      }

      run_once = false;    
    }
    else if(cmd[0]==CMD_SERVO_WRITE && run_once)
    {
      //Servo pins on Due are offset by 2
      int pin = cmd[1];
      int pin_idx = pin-SERVO_PIN_OFFSET; 
      int angle = (cmd[3] << 8) + cmd[2];

      //Serial.print("Servo Write. Pin: ");
      //Serial.print(pin);
      //Serial.print(", Angle: ");
      //Serial.println(angle);

      if(servos[pin_idx] != nullptr) {
        servos[pin_idx]->write(angle);
      }

      run_once = false;    
    }
    else if(cmd[0]==CMD_SERVO_READ && run_once)
    {
      //Servo pins on Due are offset by 2
      int pin = cmd[1];
      int pin_idx = pin-SERVO_PIN_OFFSET; 

      //Serial.print("Servo Read. Pin: ");
      //Serial.print(pin);

      if(servos[pin_idx] != nullptr) {
        servoRead = servos[pin_idx]->read();
        b[1]=servoRead/256;
        b[2]=servoRead%256;
      }

      //Serial.print(", Angle: ");
      //Serial.println(servoRead);

      run_once = false;    
    }
    //Grove temp and humidity sensor pro
    //40- Temperature
    else if(cmd[0]==CMD_TEMP_HUMIDITY_READ)
    {
		if(run_once)
		{
			if(cmd[2]==0)
			dht.begin(cmd[1],DHT11);
			else if(cmd[2]==1)
			dht.begin(cmd[1],DHT22);
			else if(cmd[2]==2)
			dht.begin(cmd[1],DHT21);
			else if(cmd[2]==3)
			dht.begin(cmd[1],AM2301);
			float t= dht.readTemperature();
			float h= dht.readHumidity();
			//Serial.print(t);
			//Serial.print("#");
			byte *b1=(byte*)&t;
			byte *b2=(byte*)&h;
			for(j=0;j<4;j++)
			dht_b[j+1]=b1[j];
			for(j=4;j<8;j++)
			dht_b[j+1]=b2[j-4];
			run_once=0;
		}
    }

    // Grove LED Bar
    // http://www.seeedstudio.com/wiki/Grove_-_LED_Bar
    // pins: data,clock,vcc,gnd

    // Commands
    // [50, pin, greenToRed, unused]  initialise a LED Bar
    // [51, pin, greenToRed, unused]  setGreenToRed(bool greenToRed)
    // [52, pin, level, unused]       setLevel(unsigned char level)
    // [53, pin, led, state]          setLed(unsigned char led, bool state)
    // [54, pin, led, unused]         toggleLed(unsigned char led)
    // [55, pin, bits 1-8, bits 9-10] setBits(unsigned int bits)
    // [56, pin, unused, unused]      getBits()

    // Initialise
    // [50, pin, orientation, unused]
    else if(cmd[0] == CMD_LED_BAR_INIT)
    {
      // clock pin is always next to the data pin
      ledbar[cmd[1]-2].begin(cmd[1]+1, cmd[1], cmd[2]); // clock, data, orientation
    }

    // Change the orientation
    // Green to red, or red to green
    // [51, pin, greenToRed, unused]
    else if(cmd[0] == CMD_LED_BAR_SET_GTOR && ledbar[cmd[1]-2].ready())
    {
      ledbar[cmd[1]-2].setGreenToRed(cmd[2]);
    }

    // Set level (0-10)
    // Level 0 means all leds off
    // Level 10 means all leds on
    // [52, pin, level, unused]
    else if(cmd[0] == CMD_LED_BAR_SET_LEVEL && ledbar[cmd[1]-2].ready())
    {
      ledbar[cmd[1]-2].setLevel(cmd[2]);
    }

    // Set a single led
    // led (1-10)
    // state (0=off, 1=on)
    // [53, pin, led, state]
    else if(cmd[0] == CMD_LED_BAR_SET_LED && ledbar[cmd[1]-2].ready())
    {
      ledbar[cmd[1]-2].setLed(cmd[2], cmd[3]);
    }

    // Toggle a single led
    // led (1-10)
    // [54, pin, led, unused]
    else if(cmd[0] == CMD_LED_BAR_TOGGLE_LED && ledbar[cmd[1]-2].ready())
    {
      ledbar[cmd[1]-2].toggleLed(cmd[2]);
    }

    // Set the current state, one bit for each led
    // 0    = 0x0   = 0b000000000000000 = all leds off
    // 5    = 0x05  = 0b000000000000101 = leds 1 and 3 on, all others off
    // 341  = 0x155 = 0b000000101010101 = leds 1,3,5,7,9 on, 2,4,6,8,10 off
    // 1023 = 0x3ff = 0b000001111111111 = all leds on
    //                       |        |
    //                       10       1
    // [55, pin, bits 1-8, bits 9-10]
    else if(cmd[0] == CMD_LED_BAR_SET_STATE && ledbar[cmd[1]-2].ready())
    {
      ledbar[cmd[1]-2].setBits(cmd[2] ^ (cmd[3] << 8));
    }

    // Return the current state
    // [56, pin, unused, unused]
    else if(cmd[0] == CMD_LED_BAR_RET_STATE && ledbar[cmd[1]-2].ready())
    {
      unsigned int state = ledbar[cmd[1]-2].getBits();
      b[1] = state & 0xFF;
      b[2] = state >> 8;
    }

    // end Grove LED Bar

    //  start dynamixel control
#ifdef INCLUDE_DYNAMIXEL

    // Sets a register value in a Dynamixel servo
    else if(cmd[0] == CMD_DYN_SET_REGISTER && run_once)
    {
      dynamixelSetRegister();
      run_once = false;
    }
    
    // Gets a register value from a Dynamixel servo
    else if(cmd[0] == CMD_DYN_GET_REGISTER && run_once)
    {
      dynamixelGetRegister();
      run_once = false;
    }
    
    // Start a Dynamixel servo moving 
    else if(cmd[0] == CMD_DYN_MOVE && run_once)
    {
      dynamixelMove();
      run_once = false;
    }

    // Stop a Dynamixel servo moving 
    else if(cmd[0] == CMD_DYN_STOP && run_once)
    {
      dynamixelStop();
      run_once = false;
    }

    // Set the Dynamixel servo moving endlessly
    else if(cmd[0] == CMD_DYN_SET_ENDLESS && run_once)
    {
      dynamixelSetEndless();
      run_once = false;
    }

    // Set the Dynamixel endless turn speed
    else if(cmd[0] == CMD_DYN_SET_TURN_SPEED && run_once)
    {
      dynamixelSetTurnSpeed();
      run_once = false;
    }

    // Start a synch move command
    else if(cmd[0] == CMD_DYN_START_SYNCH_MOVE && run_once)
    {
      dynamixelStartSynchMove();
      run_once = false;
    }

    // Add a servo to a sync move command
    else if(cmd[0] == CMD_DYN_ADD_SERVO_SYNCH && run_once)
    {
      dynamixelAddToSynchMove();
      run_once = false;
    }

    // Execute a sync move command
    else if(cmd[0] == CMD_DYN_EXEC_SYNCH_MOVE && run_once)
    {
      dynamixelExecuteSynchMove();
      run_once = false;
    }

#endif
    //  end dynamixel control

    // Grove 4 Digit Display (7 segment)
    // http://www.seeedstudio.com/wiki/Grove_-_4-Digit_Display
    // pins: clock,data,vcc,gnd

    // Commands
    // [70, pin, unused, unused]      initialise a 4 digit display
    // [71, pin, brightness, unused]  set brightness
    // [72, pin, bits 1-8, bits 9-16] right aligned decimal value without leading zeros
    // [73, pin, bits 1-8, bits 9-16] right aligned decimal value with leading zeros
    // [74, pin, index, dec]          set individual digit
    // [75, pin, index, binary]       set individual segment
    // [76, pin, left, right]         set left and right values with colon
    // [77, pin, analog pin, seconds] display analog read for n seconds
    // [78, pin, unused, unused]      display on
    // [79, pin, unused, unused]      display off

    // initialise a 4 digit display
    // [70, pin, unused, unused]
    else if(cmd[0] == CMD_4D_INIT)
    {
      // clock pin is always next to the data pin
      fourdigit[cmd[1]-2].begin(cmd[1], cmd[1]+1);  // clock, data
    }

    // set brightness
    // [71, pin, brightness, unused]
    else if(cmd[0] == CMD_4D_SET_BRIGHT && fourdigit[cmd[1]-2].ready())
    {
      fourdigit[cmd[1]-2].setBrightness(cmd[2]);  // setBrightness(brightness)
    }

    // show right aligned decimal value without leading zeros
    // [72, pin, bits 1-8, bits 9-16]
    else if(cmd[0] == CMD_4D_VAL_W_ZERO && fourdigit[cmd[1]-2].ready())
    {
      fourdigit[cmd[1]-2].showNumberDec(cmd[2] ^ (cmd[3] << 8), false);  // showNumberDec(number, leading_zero)
    }

    // show right aligned decimal value with leading zeros
    // [73, pin, bits 1-8, bits 9-16]
    else if(cmd[0] == CMD_4D_VAL_WO_ZERO && fourdigit[cmd[1]-2].ready())
    {
      fourdigit[cmd[1]-2].showNumberDec(cmd[2] ^ (cmd[3] << 8), true);  // showNumberDec(number, leading_zero)
    }

    // set individual digit
    // [74, pin, index, dec]
    else if(cmd[0] == CMD_4D_SET_DIGIT && fourdigit[cmd[1]-2].ready())
    {
      uint8_t data[] = {};
      data[0] = fourdigit[cmd[1]-2].encodeDigit(cmd[3]);  // encodeDigit(number)
      fourdigit[cmd[1]-2].setSegments(data, 1, cmd[2]);  // setSegments(segments[], length, position)
    }

    // set individual segment
    // [75, pin, index, binary]
    else if(cmd[0] == CMD_4D_SET_SEGMENT && fourdigit[cmd[1]-2].ready())
    {
      // 0xFF = 0b11111111 = Colon,G,F,E,D,C,B,A
      // Colon only works on 2nd segment (index 1)
      //     -A-
      //  F |   | B
      //     -G-
      //  E |   | C
      //     -D-
      uint8_t data[] = {};
      data[0] = cmd[3];  // byte
      fourdigit[cmd[1]-2].setSegments(data, 1, cmd[2]);  // setSegments(segments[], length, position)
    }

    // set left and right with colon separator
    // [76, pin, left, right]
    else if(cmd[0] == CMD_4D_SET_COLON && fourdigit[cmd[1]-2].ready())
    {
      uint8_t data[] = {};
      // 1st segment
      data[0] = fourdigit[cmd[1]-2].encodeDigit(cmd[2] / 10);  // encodeDigit(number)
      // 2nd segment
      data[1] = fourdigit[cmd[1]-2].encodeDigit(cmd[2] % 10);  // encodeDigit(number)
      // colon
      data[1] |= 0x80;
      // 3rd segment
      data[2] = fourdigit[cmd[1]-2].encodeDigit(cmd[3] / 10);  // encodeDigit(number)
      // 4th segment
      data[3] = fourdigit[cmd[1]-2].encodeDigit(cmd[3] % 10);  // encodeDigit(number)
      // send
      fourdigit[cmd[1]-2].setSegments(data, 4, 0);  // setSegments(segments[], length, position)
    }

    // analog read
    // [77, pin, analog pin, seconds]
    else if(cmd[0] == CMD_4D_ANALOG_READ && fourdigit[cmd[1]-2].ready())
    {
      int pin = cmd[2];
      int reads = 4 * cmd[3];  // 1000/250 * cmd[3]

      // reading analog pin 4x per second
      for(int i = 0; i < reads; i++) {
        fourdigit[cmd[1]-2].showNumberDec(analogRead(pin), false);  // showNumberDec(number, leading_zero)
        delay(250);
      }
    }

    // display on
    // [78, pin, unused, unused]
    else if(cmd[0] == CMD_4D_DISPLAY_ON && fourdigit[cmd[1]-2].ready())
    {
      uint8_t data[] = { 0xFF, 0xFF, 0xFF, 0xFF };
      fourdigit[cmd[1]-2].setSegments(data, 4, 0);  // setSegments(segments[], length, position)
    }

    // display off
    // [79, pin, unused, unused]
    else if(cmd[0] == CMD_4D_DISPLAY_OFF && fourdigit[cmd[1]-2].ready())
    {
      uint8_t data[] = { 0x00, 0x00, 0x00, 0x00 };
      fourdigit[cmd[1]-2].setSegments(data, 4, 0);  // setSegments(segments[], length, position)
    }

    // end Grove 4 Digit Display
    
    // Grove Chainable RGB LED
    // http://www.seeedstudio.com/wiki/Grove_-_Chainable_RGB_LED
    // pins: ci,di,vcc,gnd and co,do,vcc,gnd
    
    // Commands
    // [90, red, green, blue]                store color for later use
    // [91, pin, num leds, unused]           initialise a chain of leds
    // [92, pin, num leds, unused]           initialise a chain of leds and set all to a test color
    // [93, pin, pattern, which led]         set one or more leds to the stored color by pattern
    // [94, pin, led offset, modulo divisor] set one or more leds to the stored color by modulo
    // [95, pin, level, reverse]             sets leds similar to a bar graph, reversible

    // Store RGB color for later use
    // [90, red, green, blue]
    else if(cmd[0] == CMD_CLED_STORE_COLOR)
    {
      rgb[0] = cmd[1];
      rgb[1] = cmd[2];
      rgb[2] = cmd[3];
    }

    // Initialise a RGB LED chain
    // [91, pin, num leds, unused]
    else if(cmd[0] == CMD_CLED_INIT_CHAIN)
    {
      rgbled[cmd[1]-2].begin(cmd[1], cmd[1]+1, cmd[2]);  // clock, data, num leds
    }
    
    // Test colors, repeating red green blue
    // color code: 0 black (off), 1 blue, 2 green, 3 cyan, 4 red, 5 magenta, 6 yellow, 7 white
    // [92, pin, num leds, color code]
    else if(cmd[0] == CMD_CLED_INIT_SET_TEST)
    {
      rgbled[cmd[1]-2].begin(cmd[1], cmd[1]+1, cmd[2]);
      
      // figure out which color to display, a single bit for each rgb led
      byte rr = ((cmd[3] & 4) >> 2) * 255,
           gg = ((cmd[3] & 2) >> 1) * 255,
           bb = ((cmd[3] & 1)) * 255;

      // set each led to the specified color
      for(int i = 0; i < cmd[2]; i++)
      {
        rgbled[cmd[1]-2].setColorRGB(i, rr, gg, bb);
      }
    }

    // Set one or more leds to the stored color using pattern
    // pattern: 0 = this led only, 1 all leds except this led, 2 this led and all leds inwards, 3 this led and all leds outwards
    // which led: 0 = led closest to the GrovePi, 1 = second led counting outwards
    // [93, pin, pattern, which led]
    else if(cmd[0] == CMD_CLED_SET_PATTERN)
    {
      if(cmd[2] == 0) {
        // set an individual led to the stored color
        rgbled[cmd[1]-2].setColorRGB(cmd[3], rgb[0], rgb[1], rgb[2]);  // which led, red, green, blue
      }
      else {
        // set all leds to stored color
        byte num_leds = rgbled[cmd[1]-2].getNumLeds();

        for(int i = 0; i < num_leds; i++)
        {
          // cmd[2] == 1: set all leds other than this one to the stored color
          // cmd[2] == 2: this led and all previous leds, inwards
          // cmd[2] == 3: this led and all next leds, outwards
          if((cmd[2] == 1 && i != cmd[3]) || (cmd[2] == 2 && i <= cmd[3]) || (cmd[2] == 3 && i >= cmd[3])) {
            rgbled[cmd[1]-2].setColorRGB(i, rgb[0], rgb[1], rgb[2]);  // which led, red, green, blue
          }
        }
      }
    }
    
    // Set one or more leds to the stored color using modulo
    // led offset: 0 = led closest to the GrovePi, counting outwards
    // modulo divisor: when 1 (default) sets stored color on all leds >= offset, when 2 sets every 2nd led >= offset and so on
    // [94, pin, led offset, modulo divisor]
    else if(cmd[0] == CMD_CLED_SET_MODULO)
    {
      // modulo divisor must be >= 1
      if(cmd[3] < 1) {
        cmd[3] = 1;
      }

      // get the chain length
      byte num_leds = rgbled[cmd[1]-2].getNumLeds();
      
      // starting at the offset, step through each led and if the result of the modulo operator results in zero, set the stored color on the led
      for(int i = cmd[2]; i < num_leds; i++)
      {
        // use modulo to set every n led
        if((i - cmd[2]) % cmd[3] == 0) {
          rgbled[cmd[1]-2].setColorRGB(i, rgb[0], rgb[1], rgb[2]);  // which led, red, green, blue
        }
      }
    }
    
    // Set level (0 to num leds), counting outwards from the GrovePi, 0 = all off, 1 = first led, reversible to count inwards
    // [95, pin, level, reverse]
    else if(cmd[0] == CMD_CLED_SET_lEVEL)
    {
      // get the chain length
      byte num_leds = rgbled[cmd[1]-2].getNumLeds();

      if(cmd[3] == 0)
      {
        // outwards
        for(int i = 0; i < num_leds; i++)
        {
          if(cmd[2] > i) {
            rgbled[cmd[1]-2].setColorRGB(i, rgb[0], rgb[1], rgb[2]);  // which led, red, green, blue
          }
          else {
            rgbled[cmd[1]-2].setColorRGB(i, 0, 0, 0);  // which led, red, green, blue
          }
        }
      }
      else {
        // inwards
        for(int i = num_leds; i > 0; i--)
        {
          if((num_leds - cmd[2]) <= i) {
            rgbled[cmd[1]-2].setColorRGB(i, rgb[0], rgb[1], rgb[2]);  // which led, red, green, blue
          }
          else {
            rgbled[cmd[1]-2].setColorRGB(i, 0, 0, 0);  // which led, red, green, blue
          }
        }
      }
    }
    else if(cmd[0]==CMD_DUST_SENSOR_EN)
	{
		attachInterrupt(0,readPulseDust,CHANGE);
		dust_run_bk=1;
		starttime=millis();
		cmd[0]=0;
	}
	else if(cmd[0]==CMD_DUST_SENSOR_DIS)
	{
		detachInterrupt(0);
		dust_run_bk=0;
		cmd[0]=0;
	}
	else if(cmd[0]==CMD_DUST_SENSOR_READ)
	{
		if(run_once==1)
		{
		b[0]=dust_latest;
		b[1]=latest_dust_val%256;
		latest_dust_val=latest_dust_val/256;
		b[2]=latest_dust_val%256;
		b[3]=latest_dust_val/256;
		run_once=0;
		}
	}
	else if(cmd[0]==CMD_ENCODER_EN)
	{
		//encoder.Timer_init(); 
		//enc_run_bk=1;
		//cmd[0]=0;
	}
	else if(cmd[0]==CMD_ENCODER_DIS)
	{
		//encoder.Timer_disable();
		//enc_run_bk=0;
	}
	else if(cmd[0]==CMD_FLOW_EN)
	{
		pinMode(2, INPUT); 
		attachInterrupt(0, rpm, RISING);
		NbTopsFan = 0;
		flow_read_start=millis();
		flow_run_bk=1;
		cmd[0]=0;
	}
	else if(cmd[0]==CMD_FLOW_DIS)
    {
		flow_run_bk=0;
        detachInterrupt(0);
        cmd[0]=0;
    }
  }
    //Dust sensor can run in background so has a dedicated if condition
    if(dust_run_bk)
    {
		if(millis()-starttime>30000)
		{
			dust_latest=1;
			latest_dust_val=lowpulseoccupancy;
			lowpulseoccupancy=0;
			starttime=millis();
		}
    }

    if(enc_run_bk)
    {/*
        if (encoder.rotate_flag ==1)
        {
            if (encoder.direct==1)
            {
                index_LED++;
                if (index_LED>24)
                index_LED=0;
                enc_val[0]=1;
                enc_val[1]=index_LED;
            }
            else
            {
                index_LED--;
                if(index_LED<0)
                index_LED=24;
                enc_val[0]=1;
                enc_val[1]=index_LED;
            }
            encoder.rotate_flag =0;
        }
        */
    }

    if(flow_run_bk)
    {
        if(millis()-flow_read_start>2000)
        {
            Calc = (NbTopsFan * 30 / 73);
            flow_val[0]=1;
            flow_val[1]=Calc%256;
            flow_val[2]=Calc/256;
            NbTopsFan = 0;
            flow_read_start=millis();
        }
    }
}

void receiveData(int byteCount)
{
    //Serial.print("Avail: "); 
    //Serial.println(Wire.available());
  
    while(Wire.available())
    {
      if(Wire.available()==6)
      {
        flag=0; 
        idx=0;
		    run_once=1;
      }
        cmd[idx++] = Wire.read();
    }
}

// callback for sending data
void sendData()
{
  //Serial.println("sendData");
  
  if(cmd[0] == CMD_DIGITAL_READ)
    Wire.write(val);
  if(cmd[0] == CMD_ANALOG_READ || 
     cmd[0] == CMD_ULTRASONIC_READ || 
     cmd[0] == CMD_LED_BAR_RET_STATE ||
     cmd[0] == CMD_SERVO_READ || 
     cmd[0] == CMD_DYN_GET_REGISTER)
  {
    Wire.write(b, 3);

    //Serial.print("Sending data 3,7,56: ");
    //Serial.print(b[0]);
    //Serial.print(", ");
    //Serial.print(b[1]);
    //Serial.print(", ");
    //Serial.println(b[2]);
  }
  if(cmd[0] == CMD_FIRMWARE_VERSION || 
     cmd[0] == CMD_ACCEl_XYZ_READ)
    Wire.write(b, 4);
  if(cmd[0] == CMD_RTC_TIME_READ) 
    Wire.write(b, 9);
  if(cmd[0] == CMD_TEMP_HUMIDITY_READ) 
    Wire.write(dht_b, 9);
  
  if(cmd[0]==CMD_IR_RECV)
  {
    Wire.write(b,CMD_IR_RECV);     
    b[0]=0;
  }
  if(cmd[0]==CMD_DUST_SENSOR_READ)
  {
    Wire.write(b,4);     
	dust_latest=0;
	cmd[0]=0;
  }
  if(cmd[0]==CMD_ENCODER_READ)
  {
    Wire.write(enc_val,2);     
    enc_val[0]=0;
	cmd[0]=0;
  }
  if(cmd[0]==CMD_FLOW_READ)
  {
    Wire.write(flow_val,3);     
    flow_val[0]=0;
	cmd[0]=0;
  }
 
}

//ISR for the flow sensor
void rpm ()     //This is the function that the interupt calls 
{ 
  NbTopsFan++;  //This function measures the rising and falling edge of the 
 
//hall effect sensors signal
} 

void readPulseDust()
{
  t = millis();
  l_status = digitalRead(2);  // Represents if the line is low or high.  
  if(l_status)
  { 
	 digitalWrite(8,0);
    // If the line is high (1), the pulse just ended
    pulse_end = t;
  }
  else
  {   // If the line is low (0), the pulse just started
    pulse_start = t;
	digitalWrite(8,1);
  }
  
  if(pulse_end > pulse_start)
  {
    duration = pulse_end - pulse_start;
    lowpulseoccupancy = lowpulseoccupancy+duration;   // Add to the pulse length.
    pulse_end = 0;    // If you don't reset this, you'll keep adding the pulse length over and over.
  }
}
