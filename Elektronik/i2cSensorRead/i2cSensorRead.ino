#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_ADS1015.h>

//Initialize I2C addresses of multiplexers
Adafruit_ADS1015 mux0(0x48);
Adafruit_ADS1015 mux1(0x49);
Adafruit_ADS1015 mux2(0x4A);
Adafruit_ADS1015 mux3(0x4B);

SoftwareSerial bt(7,6); //RX, TX

void setup() {
  //Set Gain level for OPA
  /*ads1015.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV (default)
  ads1015.setGain(GAIN_ONE);     // 1x gain   +/- 4.096V  1 bit = 2mV
  ads1015.setGain(GAIN_TWO);     // 2x gain   +/- 2.048V  1 bit = 1mV
  ads1015.setGain(GAIN_FOUR);    // 4x gain   +/- 1.024V  1 bit = 0.5mV
  ads1015.setGain(GAIN_EIGHT);   // 8x gain   +/- 0.512V  1 bit = 0.25mV
  ads1015.setGain(GAIN_SIXTEEN); // 16x gain  +/- 0.256V  1 bit = 0.125mV*/
  
  Serial.begin(9600);
  mux0.begin();
  mux1.begin();
  mux2.begin();
  mux3.begin();

}

void loop() {
  
  //Initialize variables for A0 - A3 of each multiplexer
  int16_t adc00, adc01, adc02, adc03;
  int16_t adc10, adc11, adc12, adc13;
  int16_t adc20, adc21, adc22, adc23;
  int16_t adc30, adc31, adc32, adc33;
  
  //Read sensorvalues of each photodiode
  adc00 = mux0.readADC_SingleEnded(0);
  adc01 = mux0.readADC_SingleEnded(1);
  adc02 = mux0.readADC_SingleEnded(2);
  adc03 = mux0.readADC_SingleEnded(3);

  adc10 = mux1.readADC_SingleEnded(0);
  adc11 = mux1.readADC_SingleEnded(1);
  adc12 = mux1.readADC_SingleEnded(2);
  adc13 = mux1.readADC_SingleEnded(3);

  adc20 = mux2.readADC_SingleEnded(0);
  adc21 = mux2.readADC_SingleEnded(1);
  adc22 = mux2.readADC_SingleEnded(2);
  adc23 = mux2.readADC_SingleEnded(3);

  adc30 = mux3.readADC_SingleEnded(0);
  adc31 = mux3.readADC_SingleEnded(1);
  adc32 = mux3.readADC_SingleEnded(2);
  adc33 = mux3.readADC_SingleEnded(3);

  //Print sensorvalues to serialport
  Serial.print("AIN00: "); Serial.println(adc00);
  Serial.print("AIN01: "); Serial.println(adc01);
  Serial.print("AIN02: "); Serial.println(adc02);
  Serial.print("AIN03: "); Serial.println(adc03);
  Serial.println(" ");


  Serial.print("AIN10: "); Serial.println(adc10);
  Serial.print("AIN11: "); Serial.println(adc11);
  Serial.print("AIN12: "); Serial.println(adc12);
  Serial.print("AIN13: "); Serial.println(adc13);
  Serial.println(" ");

  Serial.print("AIN20: "); Serial.println(adc20);
  Serial.print("AIN21: "); Serial.println(adc21);
  Serial.print("AIN22: "); Serial.println(adc22);
  Serial.print("AIN23: "); Serial.println(adc23);
  Serial.println(" ");
  
  Serial.print("AIN30: "); Serial.println(adc30);
  Serial.print("AIN31: "); Serial.println(adc31);
  Serial.print("AIN32: "); Serial.println(adc32);
  Serial.print("AIN33: "); Serial.println(adc33);
  Serial.println(" ");
  /*We can use bt.println instead to send senordata via bluetooth if wanted */
  
  delay(10);
  
  //Just for testing the RC-Car
  /*if(adc00 >= 2.5){
    Serial.println("w");
  }
  if(adc01 >= 2.5){
    Serial.println("s");
  }
  if(adc02 >= 2.5){
    Serial.println("a");
  }
  if(adc03 >= 2.5){
    Serial.println("r");
  }*/
}