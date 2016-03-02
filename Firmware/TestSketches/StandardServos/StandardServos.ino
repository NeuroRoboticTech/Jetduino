#include <Servo.h>

Servo servos[12];

void setup() {
  Serial.begin(57600);         // start serial for output

  //Attach to 12 PWM servo lines.
  for(int pin=2; pin<=13; pin++) {
    servos[pin].attach(pin);
  }

  Serial.println("Setup finished");
}

void loop() {
  Serial.println("Servos from 0 to 180");
  for(int angle=0; angle<180; angle+=10) {
    for(int pin=2; pin<=13; pin++) {
      servos[pin].write(angle);
    }  
    delay(50);
  }
  
  delay(2000);

  Serial.println("Servos from 180 to 0");
  for(int angle=180; angle>0; angle-=10) {
    for(int pin=2; pin<=13; pin++) {
      servos[pin].write(angle);
    }  
    delay(50);
  }

  delay(2000);
}
