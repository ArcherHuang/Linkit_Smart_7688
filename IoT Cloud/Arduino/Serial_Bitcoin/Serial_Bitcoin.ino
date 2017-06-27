// OLED
#include <Wire.h>  //載入I2C函式庫
#include <SeeedOLED.h> //載入SeeedOLED函式庫

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(115200);  // open serial connection to USB Serial                           //port(connected to your computer)
  Serial1.begin(57600);  // open internal serial connection to MT7688
  
  // OLED
  Wire.begin();
  SeeedOled.init();  
  SeeedOled.clearDisplay();  //清除螢幕
  SeeedOled.setNormalDisplay(); //設定螢幕為正常模式(非反白)
  SeeedOled.setPageMode();  //設定尋址模式頁模式
  SeeedOled.setTextXY(0,0); //設定啟始坐標
  SeeedOled.putString("Bitcoin"); 

}

void loop() 
{
  // put your main code here, to run repeatedly:
  
  String s = "";
  
  while (Serial1.available()) {
      char c = Serial1.read();
      if(c!='\n'){
          s += c;
      }
      delay(5);    // 沒有延遲的話 UART 串口速度會跟不上Arduino的速度，會導致資料不完整
  }

  if(s!=""){
      Serial.println(s); 
      
      String tmp1 = s.substring(0, s.indexOf("~"));
      Serial.println(tmp1);
      int str_len1 = tmp1.length() + 1;
      char char_array1[str_len1];
      tmp1.toCharArray(char_array1, str_len1);
  
      SeeedOled.setTextXY(1,0); //設定啟始坐標
      SeeedOled.putString(char_array1);
      
      String tmp2 = s.substring(s.indexOf("~")+1, s.lastIndexOf("~"));
      Serial.println(tmp2);
      int str_len2 = s.substring(s.indexOf("~")+1, s.lastIndexOf("~")).length() + 1;
      char char_array2[str_len2];
      tmp2.toCharArray(char_array2, str_len2);
  
      SeeedOled.setTextXY(2,0); //設定啟始坐標
      SeeedOled.putString(char_array2);   
      
      String tmp3 = s.substring(s.lastIndexOf("~")+1, s.length());
      Serial.println(tmp3);
      int str_len3 = s.substring(s.lastIndexOf("~")+1, s.length()).length() + 1;
      char char_array3[str_len3];
      tmp3.toCharArray(char_array3, str_len3);
  
      SeeedOled.setTextXY(3,0); //設定啟始坐標
      SeeedOled.putString(char_array3); 
  }
    
  
}


