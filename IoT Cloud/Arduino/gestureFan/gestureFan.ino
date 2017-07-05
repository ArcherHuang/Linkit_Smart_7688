#include <Wire.h>
#include "paj7620.h"

#define Fan_Motor 5

void setup() {
  // put your setup code here, to run once:
  
  pinMode(Fan_Motor, OUTPUT);
  
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
      Serial.println("Please input your gestures:\n");
  }
  
}

void loop() {
  // put your main code here, to run repeatedly:

  uint8_t data = 0;  // Read Bank_0_Reg_0x43/0x44 for gesture result.

  paj7620ReadReg(0x43, 1, &data);
  if (data == GES_UP_FLAG){
    Serial.println("GES_UP_FLAG");
    digitalWrite(Fan_Motor, 5);
  }else if (data == GES_DOWN_FLAG){
    Serial.println("GES_DOWN_FLAG");
    digitalWrite(Fan_Motor, 0);
  }
}
