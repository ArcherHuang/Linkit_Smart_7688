#define MoisturePin A1     //訊號來源為第A1腳位

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int moistureVal = analogRead(MoisturePin);
  Serial.print("Moisture:");
  Serial.print(moistureVal);
  Serial.println(" %\t");
  delay(1000); //每秒回傳一次資料
}
