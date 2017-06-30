#define Fan_Motor 5

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);                                   	// init serial link for debugging
  pinMode(Fan_Motor, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(Fan_Motor, 10);
}
