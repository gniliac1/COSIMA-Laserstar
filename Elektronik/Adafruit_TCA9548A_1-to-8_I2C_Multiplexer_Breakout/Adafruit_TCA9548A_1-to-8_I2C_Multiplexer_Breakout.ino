#include <Adafruit_ADS1015.h>
#include <SoftwareSerial.h>
#include <Wire.h>

#define TCAADDR 0x70

/* Assign a unique ID to this sensor at the same time */
Adafruit_ADS1015 mux00(0x4A);
Adafruit_ADS1015 mux10(0x4A);
Adafruit_ADS1015 mux20(0x4A);
Adafruit_ADS1015 mux30(0x4A);
Adafruit_ADS1015 mux40(0x4A);
Adafruit_ADS1015 mux50(0x4A);
Adafruit_ADS1015 mux60(0x4A);
Adafruit_ADS1015 mux70(0x4A);


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

  tcaselect(2);
  mux10.begin();
  mux10.setGain(GAIN_EIGHT);
  
  tcaselect(3);
  mux10.begin();
  mux10.setGain(GAIN_EIGHT);
  
  tcaselect(4);
  mux10.begin();
  mux10.setGain(GAIN_EIGHT);

  tcaselect(5);
  mux10.begin();
  mux10.setGain(GAIN_EIGHT);

  tcaselect(6);
  mux10.begin();
  mux10.setGain(GAIN_EIGHT);

  tcaselect(7);
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

  tcaselect(2); // Detektormodul
  int16_t adc20 = mux20.readADC_SingleEnded(0);
  int16_t adc21 = mux20.readADC_SingleEnded(1);
  int16_t adc22 = mux20.readADC_SingleEnded(2);
  int16_t adc23 = mux20.readADC_SingleEnded(3);

  tcaselect(3); // Detektormodul
  int16_t adc30 = mux30.readADC_SingleEnded(0);
  int16_t adc31 = mux30.readADC_SingleEnded(1);
  int16_t adc32 = mux30.readADC_SingleEnded(2);
  int16_t adc33 = mux30.readADC_SingleEnded(3);

  tcaselect(4); // Detektormodul
  int16_t adc40 = mux40.readADC_SingleEnded(0);
  int16_t adc41 = mux40.readADC_SingleEnded(1);
  int16_t adc42 = mux40.readADC_SingleEnded(2);
  int16_t adc43 = mux40.readADC_SingleEnded(3);
 
  tcaselect(5); // Detektormodul
  int16_t adc50 = mux50.readADC_SingleEnded(0);
  int16_t adc51 = mux50.readADC_SingleEnded(1);
  int16_t adc52 = mux50.readADC_SingleEnded(2);
  int16_t adc53 = mux50.readADC_SingleEnded(3);

  tcaselect(6); // Detektormodul
  int16_t adc60 = mux60.readADC_SingleEnded(0);
  int16_t adc61 = mux60.readADC_SingleEnded(1);
  int16_t adc62 = mux60.readADC_SingleEnded(2);
  int16_t adc63 = mux60.readADC_SingleEnded(3);

  tcaselect(7); // Detektormodul
  int16_t adc70 = mux70.readADC_SingleEnded(0);
  int16_t adc71 = mux70.readADC_SingleEnded(1);
  int16_t adc72 = mux70.readADC_SingleEnded(2);
  int16_t adc73 = mux70.readADC_SingleEnded(3);

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
  Serial.print("Modul 3 Sensor 0 - "); Serial.println(adc20);
  Serial.print("Modul 3 Sensor 1 - "); Serial.println(adc21);
  Serial.print("Modul 3 Sensor 2 - "); Serial.println(adc22);
  Serial.print("Modul 3 Sensor 3 - "); Serial.println(adc23);
  Serial.println("");
  Serial.print("Modul 4 Sensor 0 - "); Serial.println(adc30);
  Serial.print("Modul 4 Sensor 1 - "); Serial.println(adc31);
  Serial.print("Modul 4 Sensor 2 - "); Serial.println(adc32);
  Serial.print("Modul 4 Sensor 3 - "); Serial.println(adc33);
  Serial.println("");
  Serial.print("Modul 5 Sensor 0 - "); Serial.println(adc40);
  Serial.print("Modul 5 Sensor 1 - "); Serial.println(adc41);
  Serial.print("Modul 5 Sensor 2 - "); Serial.println(adc42);
  Serial.print("Modul 5 Sensor 3 - "); Serial.println(adc43);
  Serial.println("");
  Serial.print("Modul 6 Sensor 0 - "); Serial.println(adc50);
  Serial.print("Modul 6 Sensor 1 - "); Serial.println(adc51);
  Serial.print("Modul 6 Sensor 2 - "); Serial.println(adc52);
  Serial.print("Modul 6 Sensor 3 - "); Serial.println(adc53);
  Serial.println("");
  Serial.print("Modul 7 Sensor 0 - "); Serial.println(adc60);
  Serial.print("Modul 7 Sensor 1 - "); Serial.println(adc61);
  Serial.print("Modul 7 Sensor 2 - "); Serial.println(adc62);
  Serial.print("Modul 7 Sensor 3 - "); Serial.println(adc63);
  Serial.println("");
  Serial.print("Modul 8 Sensor 0 - "); Serial.println(adc70);
  Serial.print("Modul 8 Sensor 1 - "); Serial.println(adc71);
  Serial.print("Modul 8 Sensor 2 - "); Serial.println(adc72);
  Serial.print("Modul 8 Sensor 3 - "); Serial.println(adc73);
  Serial.println("");
  delay(2000);
}
