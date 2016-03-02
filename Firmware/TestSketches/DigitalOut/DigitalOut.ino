

void setup() {
  Serial.begin(57600);         // start serial for output

  //Set lines D2-D13 and D23-D29 to outputs
  for(int pin=2; pin<=13; pin++) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
  }
  
  for(int pin=23; pin<=29; pin++) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
  }

  delay(2000);
  Serial.println("Setup finished");
}

void setDigital(bool val) {
  for(int pin=2; pin<=13; pin++) {
    digitalWrite(pin, val);
  }
  
  for(int pin=23; pin<=29; pin++) {
    digitalWrite(pin, val);
  }  
}

void loop() {
  Serial.println("High");  
  setDigital(HIGH);  
  delay(2000);
  Serial.println("Low");  
  setDigital(LOW);
  delay(2000);
}
