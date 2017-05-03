#define PIR_MOTION_SENSOR 5

void setup() {
  // put your setup code here, to run once:
  pinMode(PIR_MOTION_SENSOR, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(isPeopleDetected());
  delay(1000); //每秒回傳一次資料
}

boolean isPeopleDetected()
{
    int sensorValue = digitalRead(PIR_MOTION_SENSOR);
    if(sensorValue == HIGH)//if the sensor value is HIGH?
    {
        return true;//yes,return true
    }
    else
    {
        return false;//no,return false
    }
}
