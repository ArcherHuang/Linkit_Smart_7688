long linuxBaud = 9600;       // the baudrate for 7688 UART0
 
void setup() {
  Serial.begin(115200);      // open serial connection via USB-Serial
  Serial1.begin(linuxBaud);  // open serial connection to 7688 UART0
}
 
void loop() {
  int c = Serial.read();     // read from the USB-Serial
 
  if (c != -1) {
    Serial1.write(c);        // pass it to the 7688 UART0
  }
 
  c = Serial1.read();        // read from the 7688 UART0
  if (c != -1) {             
    Serial.write(c);         // pass it to the USB-Serial
  }
}  

