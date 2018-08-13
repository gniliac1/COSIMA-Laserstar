#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_ADS1015.h>

Adafruit_ADS1015 mux0(0x1001000);
Adafruit_ADS1015 mux1(0x1001001);
Adafruit_ADS1015 mux2(0x1001010);
Adafruit_ADS1015 mux3(0x1001011);
SoftwareSerial bt(7,6); //RX, TX

void setup() {
  //Set Gain level for OPA
  /*ads1015.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV (default)
  ads1015.setGain(GAIN_ONE);     // 1x gain   +/- 4.096V  1 bit = 2mV
  ads1015.setGain(GAIN_TWO);     // 2x gain   +/- 2.048V  1 bit = 1mV
  ads1015.setGain(GAIN_FOUR);    // 4x gain   +/- 1.024V  1 bit = 0.5mV
  ads1015.setGain(GAIN_EIGHT);   // 8x gain   +/- 0.512V  1 bit = 0.25mV
  ads1015.setGain(GAIN_SIXTEEN); // 16x gain  +/- 0.256V  1 bit = 0.125mV*/
  
  //Initaialize 16bit signal for each line on each mux
  int16_t adc00, adc01, adc02, adc03;
  int16_t adc10, adc11, adc12, adc13;
  int16_t adc20, adc21, adc22, adc23;
  int16_t adc30, adc31, adc32, adc33;
  
  //First mux
  adc00 = mux0.readADC_SingleEnded(0);
  adc01 = mux0.readADC_SingleEnded(1);
  adc02 = mux0.readADC_SingleEnded(2);
  adc03 = mux0.readADC_SingleEnded(3);
  //Second mux
  adc10 = mux1.readADC_SingleEnded(0);
  adc11 = mux1.readADC_SingleEnded(1);
  adc12 = mux1.readADC_SingleEnded(2);
  adc13 = mux1.readADC_SingleEnded(3);
  //Third mux
  adc20 = mux2.readADC_SingleEnded(0);
  adc21 = mux2.readADC_SingleEnded(1);
  adc22 = mux2.readADC_SingleEnded(2);
  adc23 = mux2.readADC_SingleEnded(3);
  //Fourth mux
  adc30 = mux3.readADC_SingleEnded(0);
  adc31 = mux3.readADC_SingleEnded(1);
  adc32 = mux3.readADC_SingleEnded(2);
  adc33 = mux3.readADC_SingleEnded(3);
  //Start serial / i2c communication
  mux0.begin;
  mux1.begin;
  mux2.begin;
  mux3.begin;
  bt.begin(9600);

}

void loop() {
  //Read values from mux0 - mux3 and send them via bluetooth to python 
  Wire.requestFrom(mux0, 16);
  bt.print("Value00 = ");
  bt.println(adc00);
  bt.print("Value01 = ");
  bt.println(adc01);
  bt.print("Value02 = ");
  bt.println(adc02);
  bt.print("Value03 = ");
  bt.println(adc03);
  
  Wire.requestFrom(mux1, 16);
  bt.print("Value10 = ");
  bt.println(adc10);
  bt.print("Value11 = ");
  bt.println(adc11);
  bt.print("Value12 = ");
  bt.println(adc12);
  bt.print("Value13 = ");
  bt.println(adc13);
  
  Wire.requestFrom(mux2, 16);
  bt.print("Value20 = ");
  bt.println(adc20);
  bt.print("Value21 = ");
  bt.println(adc21);
  bt.print("Value22 = ");
  bt.println(adc22);
  bt.print("Value23 = ");
  bt.println(adc23);
  
  Wire.requestFrom(mux3, 16);
  bt.print("Value30 = ");
  bt.println(adc30);
  bt.print("Value31 = ");
  bt.println(adc31);
  bt.print("Value32 = ");
  bt.println(adc32);
  bt.print("Value33 = ");
  bt.println(adc33)
  
}
