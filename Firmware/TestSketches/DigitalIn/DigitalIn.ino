

void setup() {
  Serial.begin(57600);         // start serial for output

  //Set lines D2-D13 and D23-D29 to inputs
  for(int pin=2; pin<=13; pin++) {
    pinMode(pin, INPUT);
  }
  
  for(int pin=23; pin<=29; pin++) {
    pinMode(pin, INPUT);
  }

  delay(2000);
  Serial.println("Setup finished");
}

void readDigitalPins() {
  int val = 0;
  for(int pin=2; pin<=13; pin++) {
    val = digitalRead(pin);
    Serial.print(val);
    Serial.print(", ");
  }
  
  for(int pin=23; pin<=29; pin++) {
    val = digitalRead(pin);
    Serial.print(val);
    Serial.print(", ");
  }  

  Serial.println("");
}

void loop() {
  readDigitalPins();
  delay(2000);
}
