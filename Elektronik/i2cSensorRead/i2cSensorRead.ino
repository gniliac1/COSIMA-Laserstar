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
  
  // Set Gain level for OPA
  // GAIN_TWOTHIRDS - 2/3x gain +/- 6.144V  1 bit = 3mV (default)
  // GAIN_ONE       - 1x gain   +/- 4.096V  1 bit = 2mV
  // GAIN_TWO       - 2x gain   +/- 2.048V  1 bit = 1mV
  // GAIN_FOUR      - 4x gain   +/- 1.024V  1 bit = 0.5mV
  // GAIN_EIGHT     - 8x gain   +/- 0.512V  1 bit = 0.25mV
  // GAIN_SIXTEEN   - 16x gain  +/- 0.256V  1 bit = 0.125mV
  mux0.setGain(GAIN_EIGHT);
  mux1.setGain(GAIN_EIGHT);    
  mux2.setGain(GAIN_EIGHT);    
  mux3.setGain(GAIN_EIGHT);    
  
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
  zSerial.print("0 "); Serial.println(adc00);
  Serial.print("1 "); Serial.println(adc01);
  Serial.print("2 "); Serial.println(adc02);
  Serial.print("3 "); Serial.println(adc03);
  //Serial.println(" ");

  Serial.print("4 "); Serial.println(adc10);
  Serial.print("5 "); Serial.println(adc11);
  Serial.print("6 "); Serial.println(adc12);
  Serial.print("7 "); Serial.println(adc13);
  //Serial.println(" ");

  Serial.print("8 "); Serial.println(adc20);
  Serial.print("9 "); Serial.println(adc21);
  Serial.print("10 "); Serial.println(adc22);
  Serial.print("11 "); Serial.println(adc23);
  //Serial.println(" ");

  Serial.print("12 "); Serial.println(adc30);
  Serial.print("13 "); Serial.println(adc31);
  Serial.print("14 "); Serial.println(adc32);
  Serial.print("15 "); Serial.println(adc33);
  Serial.println(" ");
  
  /*We can use bt.println instead to send senordata via bluetooth if wanted */
  
  delay(1000);
  
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
