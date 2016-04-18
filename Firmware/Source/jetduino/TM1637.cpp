//  Author:Frankie.Chu
//  Date:9 April,2012
//
//  This library is free software; you can redistribute it and/or
//  modify it under the terms of the GNU Lesser General Public
//  License as published by the Free Software Foundation; either
//  version 2.1 of the License, or (at your option) any later version.
//
//  This library is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
//  Lesser General Public License for more details.
//
//  You should have received a copy of the GNU Lesser General Public
//  License along with this library; if not, write to the Free Software
//  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
//
//  Modified record:
//
/*******************************************************************************/
#include "TM1637.h"
#include <Arduino.h>
static int8_t TubeTab[] = {0x3f,0x06,0x5b,0x4f,
                           0x66,0x6d,0x7d,0x07,
                           0x7f,0x6f,0x77,0x7c,
                           0x39,0x5e,0x79,0x71};//0~9,A,b,C,d,E,F                        

TM1637::TM1637()
{
  Clkpin = 0;
  Datapin = 0;
  Cmd_SetData = 0x40;
  Cmd_SetAddr = 0xc0;
}

void TM1637::init(uint8_t Clk, uint8_t Data)
{
  Clkpin = Clk;
  Datapin = Data;
  Cmd_SetData = 0x40;
  Cmd_SetAddr = 0xc0;

  pinMode(Clkpin,OUTPUT);
  pinMode(Datapin,OUTPUT);

  clearDisplay();
}

void TM1637::writeByte(int8_t wr_data)
{
  uint8_t i,count1;   
  for(i=0;i<8;i++)        //sent 8bit data
  {
    digitalWrite(Clkpin,LOW);      
    if(wr_data & 0x01)digitalWrite(Datapin,HIGH);//LSB first
    else digitalWrite(Datapin,LOW);
    wr_data >>= 1;      
    digitalWrite(Clkpin,HIGH);
      
  }  
  digitalWrite(Clkpin,LOW); //wait for the ACK
  digitalWrite(Datapin,HIGH);
  digitalWrite(Clkpin,HIGH);     
  pinMode(Datapin,INPUT);
  while(digitalRead(Datapin))    
  { 
    count1 +=1;
    if(count1 == 200)//
    {
     pinMode(Datapin,OUTPUT);
     digitalWrite(Datapin,LOW);
     count1 =0;
    }
    pinMode(Datapin,INPUT);
  }
  pinMode(Datapin,OUTPUT);
  
}
//send start signal to TM1637
void TM1637::start(void)
{
  digitalWrite(Clkpin,HIGH);//send start signal to TM1637
  digitalWrite(Datapin,HIGH); 
  digitalWrite(Datapin,LOW); 
  digitalWrite(Clkpin,LOW); 
} 
//End of transmission
void TM1637::stop(void)
{
  digitalWrite(Clkpin,LOW);
  digitalWrite(Datapin,LOW);
  digitalWrite(Clkpin,HIGH);
  digitalWrite(Datapin,HIGH); 
}
//display function.Write to full-screen.
void TM1637::display(int8_t DispData[])
{
  int8_t SegData[4];
  uint8_t i;

  //Serial.println("display start");
  for(i = 0;i < 4;i ++)
  {
    SegData[i] = DispData[i];    
    //Serial.println(DispData[i]);
  }
  coding(SegData);

  displaySegments(SegData);
}

void TM1637::displaySegments(int8_t SegData[4])
{
  uint8_t i;

  start();          //start signal sent to TM1637 from MCU
  writeByte(ADDR_AUTO);//
  stop();           //
  start();          //
  writeByte(Cmd_SetAddr);//
  for(i=0;i < 4;i ++)
  {
    writeByte(SegData[i]);        //
  }
  stop();           //
  start();          //
  writeByte(Cmd_DispCtrl);//
  stop();           //
}

//******************************************
void TM1637::display(uint8_t BitAddr,int8_t DispData)
{
  int8_t SegData;
  SegData = coding(DispData);
  start();          //start signal sent to TM1637 from MCU
  writeByte(ADDR_FIXED);//
  stop();           //
  start();          //
  writeByte(BitAddr|0xc0);//
  writeByte(SegData);//
  stop();            //
  start();          //
  writeByte(Cmd_DispCtrl);//
  stop();           //
}

void TM1637::displaySegment(uint8_t BitAddr,int8_t DispData)
{
  int8_t SegData;
  SegData = DispData;
  start();          //start signal sent to TM1637 from MCU
  writeByte(ADDR_FIXED);//
  stop();           //
  start();          //
  writeByte(BitAddr|0xc0);//
  writeByte(SegData);//
  stop();            //
  start();          //
  writeByte(Cmd_DispCtrl);//
  stop();           //
}

void TM1637::clearDisplay(void)
{
  display(0x00,0x7f);
  display(0x01,0x7f);
  display(0x02,0x7f);
  display(0x03,0x7f);  
}
//To take effect the next time it displays.
void TM1637::set(uint8_t brightness,uint8_t SetData,uint8_t SetAddr)
{
  Cmd_SetData = SetData;
  Cmd_SetAddr = SetAddr;
  Cmd_DispCtrl = 0x88 + brightness;//Set the brightness and it takes effect the next time it displays.
}

//Whether to light the clock point ":".
//To take effect the next time it displays.
void TM1637::point(boolean PointFlag)
{
  _PointFlag = PointFlag;
}
void TM1637::coding(int8_t DispData[])
{
  uint8_t PointData;
  if(_PointFlag == POINT_ON)PointData = 0x80;
  else PointData = 0; 
  for(uint8_t i = 0;i < 4;i ++)
  {
    if(DispData[i] == 0x7f)DispData[i] = 0x00;
    else DispData[i] = TubeTab[DispData[i]] + PointData;

    //Serial.println(DispData[i]);
  }
}
int8_t TM1637::coding(int8_t DispData)
{
  uint8_t PointData;
  if(_PointFlag == POINT_ON)PointData = 0x80;
  else PointData = 0; 
  if(DispData == 0x7f) DispData = 0x00 + PointData;//The bit digital tube off
  else DispData = TubeTab[DispData] + PointData;
  return DispData;
}

void TM1637::showNumberDec(int num, bool leading_zero, uint8_t length, uint8_t pos, bool colon)
{
  int8_t digits[4];
  const static int divisors[] = { 1, 10, 100, 1000 };
  bool leading = true;

  for (int8_t k = 0; k < 4; k++) {
    int divisor = divisors[4 - 1 - k];
    int d = num / divisor;

    if (d == 0) {
      if (leading_zero || !leading || (k == 3))
        digits[k] = d;
      else
        digits[k] = 0x7f;
    }
    else {
      digits[k] = d;
      num -= d * divisor;
      leading = false;
    }
  }

  _PointFlag = colon;
  
  display(digits);
}


// Has this instance been initialised?
bool TM1637::ready()
{
  return Clkpin != 0;
}
