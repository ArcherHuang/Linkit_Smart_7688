// DHT
#include "DHT.h"
#define DHTPIN A0
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

#include <Bridge.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  dht.begin();
  Bridge.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  float h = dht.readHumidity();
  float t = dht.readTemperature();
      
  Serial.print("DHT-Humidity: "); 
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("DHT-Temperature: "); 
  Serial.print(t);
  Serial.println(" *C\t");

  // Bridge
  Bridge.put("h", String(h));
  Bridge.put("t", String(t));
        
  delay(1000); //每秒回傳一次資料
}
