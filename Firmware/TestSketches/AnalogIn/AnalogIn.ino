

void setup() {
  Serial.begin(57600);         // start serial for output

  //Set lines A0-A11 to inputs
  for(int pin=54; pin<=65; pin++) {
    pinMode(pin, INPUT);
  }

  delay(2000);
  Serial.println("Setup finished");
}

void readAnalogPins() {
  int val = 0;
  for(int pin=54; pin<=65; pin++) {
    val = analogRead(pin);
    Serial.print(val);
    Serial.print(", ");
  }

  Serial.println("");
}

void loop() {
  readAnalogPins();
  delay(2000);
}
