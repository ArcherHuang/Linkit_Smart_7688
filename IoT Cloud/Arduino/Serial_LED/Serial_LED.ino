int ledPin = 7; 

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(115200);  // open serial connection to USB Serial                           //port(connected to your computer)
  Serial1.begin(57600);  // open internal serial connection to MT7688
  pinMode(ledPin, OUTPUT); // in MT7688, this maps to device 
}

void loop() {
  // put your main code here, to run repeatedly:
  int c = Serial1.read();      // read from MT7688
  if (c != -1) {
       switch(c) { 
           case '0':                // turn off D7 when receiving "0"
               digitalWrite(ledPin, 0); 
               break; 
           case '1':                // turn on D7 when receiving "1" 
               digitalWrite(ledPin, 1); 
               break; 
       } 
   } 
}
