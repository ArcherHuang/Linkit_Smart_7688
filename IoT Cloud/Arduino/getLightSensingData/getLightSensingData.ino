#define LightPin A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
  float lightSensingData = analogRead(LightPin);
  Serial.print("Light Sensor: "); 
  Serial.println(lightSensingData);
  delay(1000); //每秒回傳一次資料
}
