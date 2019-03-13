int geoStop = 25;
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, geoStop);
}

void loop() {
  if (Serial.available() > 0) {
    char lock=Serial.read();
    if (lock == 'T')
      geoStop += 1;
    else if (lock == 'F')
      geoStop -= 1;
  }
  geoStop=constrain(geoStop,0,25);
  if(geoStop==25)
  digitalWrite(LED_BUILTIN, HIGH);
  else if(geoStop==0)
  digitalWrite(LED_BUILTIN, LOW);
}
