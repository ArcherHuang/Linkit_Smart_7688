// Dust Sensor
int dustPin = 8; 
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 2000;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
float concentrationPM25_ugm3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  
  // Dust Sensor
  pinMode(dustPin, INPUT);
  starttime = millis();//get the current time;
}

void loop() {
  // put your main code here, to run repeatedly:
  // Dust Sensor
  duration = pulseIn(dustPin, LOW);
  lowpulseoccupancy = lowpulseoccupancy+duration;
  ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=&gt;100
  concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
  
  Serial.print("concentration = ");
  Serial.print(concentration);
  Serial.println(" pcs/0.01cf");
  
  concentrationPM25_ugm3 = conversion25(concentration);
  Serial.print("PM25: ");
  Serial.print(concentrationPM25_ugm3);
  Serial.println(" ug/m3");
        
  lowpulseoccupancy = 0;
  starttime = millis();
       
  delay(1000); //每秒回傳一次資料
}

// convert from particles/0.01 ft3 to μg/m3
float conversion25(long concentrationPM25) {
  double pi = 3.14159;
  double density = 1.65 * pow (10, 12);
  double r25 = 0.44 * pow (10, -6);
  double vol25 = (4/3) * pi * pow (r25, 3);
  double mass25 = density * vol25;
  double K = 3531.5;
  return (concentrationPM25) * K * mass25;
}
