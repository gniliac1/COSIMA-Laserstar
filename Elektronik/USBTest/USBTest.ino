#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_ADS1015.h>

//Initialize I2C address of multiplexer
Adafruit_ADS1015 mux0(0x48);

int diode1;
int diode2;
char report[64];

void setup() {

  Serial.begin(9600);

  mux0.setGain(GAIN_FOUR);
  mux0.begin();
  
}

void loop() {

  diode1 = mux0.readADC_SingleEnded(0);
  diode2 = mux0.readADC_SingleEnded(1);

  sprintf(report,"Test erfolgreich:\n%d %d",diode1,diode2);
  Serial.println(report);

  delay(1000);
  
}
