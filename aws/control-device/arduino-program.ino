int relay=2;
void setup() {
  pinMode(relay,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()) {
    String s=Serial.readString();
    if(s=="on") {
      digitalWrite(relay,0);
    } else if(s=="off") {
      digitalWrite(relay,1);
    }
  }
}
  
