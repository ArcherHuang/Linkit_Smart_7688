#include <Bridge.h>

// DHT
#include "DHT.h"
#define DHTPIN A0
#define MoisturePin A1     //訊號來源為第A1腳位
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Bridge.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int moistureVal = analogRead(MoisturePin);
  
  Serial.print("DHT-Humidity: "); 
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("DHT-Temperature: "); 
  Serial.print(t);
  Serial.print(" *C\t");
  Serial.print("Moisture:");
  Serial.print(moistureVal);
  Serial.println(" %\t");
  
  Bridge.put("h", String(h));
  Bridge.put("t", String(t));
  Bridge.put("m", String(moistureVal));
  
  delay(1000); //每秒回傳一次資料
}
