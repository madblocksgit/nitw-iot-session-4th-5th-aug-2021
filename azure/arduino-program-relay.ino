// .cpp to .HEX - Cross-Compiler (Embedded C, Embedded C++, Embedded Java)
// .cpp to .EXE - General Purpose Compiler

// IDE - To write program
// Compiler - To Compile Program
// Programmer - Burn the Program (uploading the hex onto the MCU)

// Library Manager - 
// Boards Manager - ESP8266/ESP32 - Espressif

// Azure Pub -> Azure Broker (Mosquitto) -> Raspberry Pi (Sub) -> Arduino -> Relay

int relay=2; // assign a pin number according to the connection

void setup() {
  // put your setup code here, to run once:
  pinMode(relay,OUTPUT); // every pin is bi-directional (I & O) - INPUT
  // write permission to write data onto the relay
  Serial.begin(9600); // Serial UART - Pin 0,1 - 9600 bps
}

void loop() { // this logic will be iterated until power goes off
  // put your main code here, to run repeatedly:
  while(Serial.available()) { // wait for the instruction - 0 (not available) - len(on) or len(off)
    String s=Serial.readString(); // on
    if(s=="on" || s=="ON") {
      digitalWrite(relay,0); // 0 to relay - realy will be ON
    } else if(s=="off" || s=="OFF") {
      digitalWrite(relay,1); // 1 to relay - relay will be OFF
    }
  }

}
