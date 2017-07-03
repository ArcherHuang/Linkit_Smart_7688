#include <Wire.h>
#include "paj7620.h"

void setup() {
  // put your setup code here, to run once:
  
  uint8_t error = 0;

  Serial.begin(9600);
  Serial.println("\nPAJ7620U2 TEST DEMO: Recognize 9 gestures.");

  error = paj7620Init();          // initialize Paj7620 registers
  if (error)
  {
      Serial.print("INIT ERROR,CODE:");
      Serial.println(error);
  }
  else
  {
      Serial.println("INIT OK");
  }
  Serial.println("Please input your gestures:\n");
  
}

void loop() {
  // put your main code here, to run repeatedly:

  uint8_t data = 0;  // Read Bank_0_Reg_0x43/0x44 for gesture result.

  paj7620ReadReg(0x43, 1, &data);
  if (data == GES_UP_FLAG){
    Serial.println("GES_UP_FLAG");
  }else if (data == GES_DOWN_FLAG){
    Serial.println("GES_DOWN_FLAG");
  }else if (data == GES_LEFT_FLAG){
    Serial.println("GES_LEFT_FLAG");
  }else if (data == GES_DOWN_FLAG){
    Serial.println("GES_DOWN_FLAG");
  }else if (data == GES_RIGHT_FLAG){
    Serial.println("GES_RIGHT_FLAG");
  }else if (data == GES_FORWARD_FLAG){
    Serial.println("GES_FORWARD_FLAG");
  }else if (data == GES_BACKWARD_FLAG){
    Serial.println("GES_BACKWARD_FLAG");
  }else if (data == GES_CLOCKWISE_FLAG){
    Serial.println("GES_CLOCKWISE_FLAG");
  }else if (data == GES_COUNT_CLOCKWISE_FLAG){
    Serial.println("GES_COUNT_CLOCKWISE_FLAG");
  }else if (data == GES_WAVE_FLAG){
    Serial.println("GES_WAVE_FLAG");
  }
}
