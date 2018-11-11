#include <Adafruit_ADS1015.h>
#include <SoftwareSerial.h>
#include <Wire.h>

#define TCAADDR 0x70

/* Assign a unique ID to this sensor at the same time */
Adafruit_ADS1015 mux00(0x4A);
Adafruit_ADS1015 mux10(0x4A);



void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}


void setup(void) 
{
  Serial.begin(9600);
  Serial.println("Multiplexer Breakout Test"); Serial.println("");
  
  /* Initialise the 1st sensor */
  tcaselect(0);
  mux00.begin();
  mux00.setGain(GAIN_EIGHT);

  tcaselect(1);
  mux10.begin();
  mux10.setGain(GAIN_EIGHT);
  
  Serial.println("Initializing done");
}



void loop(void) 
{
  
  tcaselect(0); // Oktokommander
  int16_t adc00 = mux00.readADC_SingleEnded(0);
  int16_t adc01 = mux00.readADC_SingleEnded(1);
  int16_t adc02 = mux00.readADC_SingleEnded(2);
  int16_t adc03 = mux00.readADC_SingleEnded(3);

  tcaselect(1); // Detektormodul
  int16_t adc10 = mux10.readADC_SingleEnded(0);
  int16_t adc11 = mux10.readADC_SingleEnded(1);
  int16_t adc12 = mux10.readADC_SingleEnded(2);
  int16_t adc13 = mux10.readADC_SingleEnded(3);
 
  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  Serial.print("Modul 1 Sensor 0 - "); Serial.println(adc00);
  Serial.print("Modul 1 Sensor 1 - "); Serial.println(adc01);
  Serial.print("Modul 1 Sensor 2 - "); Serial.println(adc02);
  Serial.print("Modul 1 Sensor 3 - "); Serial.println(adc03);
  Serial.println("");
  Serial.print("Modul 2 Sensor 0 - "); Serial.println(adc10);
  Serial.print("Modul 2 Sensor 1 - "); Serial.println(adc11);
  Serial.print("Modul 2 Sensor 2 - "); Serial.println(adc12);
  Serial.print("Modul 2 Sensor 3 - "); Serial.println(adc13);
  Serial.println("");
  
  delay(2000);
}
