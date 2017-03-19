#include <Bridge.h>

// OLED
#include <Wire.h>  //載入I2C函式庫
#include <SeeedOLED.h> //載入SeeedOLED函式庫

// DHT
#include "DHT.h"
#define DHTPIN A0
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

// Temperature
int h;
int h1;
float temperature;
int B=3975;                  //B value of the thermistor
float resistance;

// LED
int ledPin = 5; 

// Dust Sensor
int dustPin = 8; 
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 30000;//sampe 30s ;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
float concentrationPM25_ugm3;

void setup() 
{
    Serial.begin(9600); 
    dht.begin();
    Bridge.begin();

    // LED
    pinMode(ledPin, OUTPUT);

    // Dust Sensor
    pinMode(dustPin, INPUT);
    starttime = millis();//get the current time;

    // OLED
    Wire.begin();
    SeeedOled.init();  
    SeeedOled.clearDisplay();  //清除螢幕
    SeeedOled.setNormalDisplay(); //設定螢幕為正常模式(非反白)
    SeeedOled.setPageMode();  //設定尋址模式頁模式
    SeeedOled.setTextXY(0,0); //設定啟始坐標
    SeeedOled.putString("Temp&Humi&Dust"); 

}

void loop() 
{
    
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    int moistureValue = analogRead(1);
    h1 = analogRead(A2);
    resistance=(float)(1023-h)*10000/h1;                       // get the resistance of the sensor;
    temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;  // convert to temperature via

    if (t > 25) 
    {
        digitalWrite(ledPin, 1);
    } 
    else 
    {
        digitalWrite(ledPin, 0);
    }

    // check if returns are valid, if they are NaN (not a number) then something went wrong!
    if (isnan(t) || isnan(h)) 
    {
        Serial.println("Failed to read from DHT");
    } 
    else 
    {
        // Dust Sensor
        duration = pulseIn(dustPin, LOW);
        lowpulseoccupancy = lowpulseoccupancy+duration;
        ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
        concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
       
        //concentrationPM25_ugm3 = conversion25(concentration);
        //Serial.print("PM25: ");
        //Serial.print(concentrationPM25_ugm3);
        //Serial.println(" ug/m3");
        //Serial.print("\n");
  
        lowpulseoccupancy = 0;
        starttime = millis();

        Serial.print("concentration: ");
        Serial.print(concentration);
        Serial.print(" pcs/0.01cf");
        Serial.print(" \t");
        Serial.print("DHT-Humidity: "); 
        Serial.print(h);
        Serial.print(" %\t");
        Serial.print("DHT-Temperature: "); 
        Serial.print(t);
        Serial.print(" *C\t");
        Serial.print("Moisture: "); 
        Serial.print(moistureValue);
        Serial.print(" \t");
        Serial.print("Temperature: "); 
        Serial.println(temperature);

        // OLED
        SeeedOled.setTextXY(1,0); //設定啟始坐標
        SeeedOled.putString("Dust: "); 
        SeeedOled.putNumber(concentration); 
        SeeedOled.setTextXY(2,0); //設定啟始坐標
        SeeedOled.putString("Temp: "); 
        SeeedOled.putNumber(t); 
        SeeedOled.putString(" *C"); 
        SeeedOled.setTextXY(3,0); //設定啟始坐標
        SeeedOled.putString("Humidity: "); 
        SeeedOled.putNumber(h); 
        SeeedOled.putString(" %"); 
        SeeedOled.setTextXY(4,0); //設定啟始坐標
        SeeedOled.putString("Moisture: "); 
        SeeedOled.putNumber(moistureValue);
        SeeedOled.putString(" %");
        SeeedOled.setTextXY(5,0); //設定啟始坐標
        SeeedOled.putString("Temp: "); 
        SeeedOled.putNumber(temperature);
        SeeedOled.putString(" *C");
               
        // Bridge
        Bridge.put("d", String(concentration));
        Bridge.put("h", String(h));
        Bridge.put("t", String(t));
        
    }
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

