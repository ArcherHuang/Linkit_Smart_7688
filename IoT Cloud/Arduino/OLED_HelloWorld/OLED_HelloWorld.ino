// OLED
#include <Wire.h>  //載入I2C函式庫
#include <SeeedOLED.h> //載入SeeedOLED函式庫

void setup() {
  // put your setup code here, to run once:
  // OLED
  Wire.begin();
  SeeedOled.init();  
  SeeedOled.clearDisplay();  //清除螢幕
  SeeedOled.setTextXY(0,0); //設定啟始坐標
  SeeedOled.putString("Hello World"); 
}

void loop() {
  // put your main code here, to run repeatedly:
  // OLED
  SeeedOled.setTextXY(1,0);
  SeeedOled.putString("Pa Pa Go"); 
        
  delay(1000); 
}
