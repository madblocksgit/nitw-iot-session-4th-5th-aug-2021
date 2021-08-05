#include "DHT.h"

DHT dht(2,DHT11);

void setup() {
 dht.begin();
 Serial.begin(9600);
}

void loop() {

  Serial.print("#");
  Serial.print(",");
  Serial.print(dht.readHumidity());
  Serial.print(",");
  Serial.print(dht.readTemperature());
  Serial.print(",");
  Serial.print("~");
  Serial.println();
  delay(2000);

}
