#include <Adafruit_ADS1015.h>
#include <SoftwareSerial.h>
#include <Wire.h>

#define TCAADDR 0x70

/* Assign a unique ID to this sensor at the same time */
Adafruit_ADS1015 mux0(0x4A);
Adafruit_ADS1015 mux1(0x4A);
Adafruit_ADS1015 mux2(0x4A);
Adafruit_ADS1015 mux3(0x4A);
Adafruit_ADS1015 mux4(0x4A);
Adafruit_ADS1015 mux5(0x4A);
Adafruit_ADS1015 mux6(0x4A);
Adafruit_ADS1015 mux7(0x4A);

const int16_t numADS = 8;         // number of AD converter
const int16_t nPhotodiodes = 32;  // number of photodiodes
int16_t adc[nPhotodiodes];        // global array for photo current
bool valueChanged;                // indicates whether the photo current has changed compared to the previous iteration
bool changesWritten;              // ndcates whether the photo currents have already been written to the serial port
const int16_t threshold = 3;      // threshold by which the values have to be changed before they are communicated
char photoReport[64];             // variable for communicating changes to python
int16_t temp;                     // temporary variable for storing the photo current
int16_t counter = 0;              // contains the current iteration of the loop


void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}


void setup(void) 
{
  Serial.begin(9600);
  
  // Initialize all AD converter
  tcaselect(0);
  mux0.begin();
  mux0.setGain(GAIN_EIGHT);

  tcaselect(1);
  mux1.begin();
  mux1.setGain(GAIN_EIGHT);

  tcaselect(2);
  mux2.begin();
  mux2.setGain(GAIN_EIGHT);

  tcaselect(3);
  mux3.begin();
  mux3.setGain(GAIN_EIGHT);

  tcaselect(4);
  mux4.begin();
  mux4.setGain(GAIN_EIGHT);

  tcaselect(5);
  mux5.begin();
  mux5.setGain(GAIN_EIGHT);

  tcaselect(6);
  mux6.begin();
  mux6.setGain(GAIN_EIGHT);

  tcaselect(7);
  mux7.begin();
  mux7.setGain(GAIN_EIGHT);

  changesWritten = false;
}



void loop(void) 
{

  // no value has changed yet
  valueChanged = false;

  // iterate over all diodes and check for changes in the photo current
  for(int16_t iDiode=0; iDiode < 4; ++iDiode) {

    tcaselect(0);
    
    // check for changes in mux0 (LED 1-4)
    temp = mux0.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode]) >= threshold ) {
      valueChanged = true;
      adc[iDiode] = temp;
    }

    tcaselect(1);
    
    // check for changes in mux1 (LED 5-8)
    temp = mux1.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+4]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+4] = temp;
    }

    tcaselect(2);
    
    // check for changes in mux2 (LED 9-12)
    temp = mux2.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+8]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+8] = temp;
    }

    tcaselect(3);

    // check for changes in mux3 (LED 13-16)
    temp = mux3.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+12]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+12] = temp;
    }

    tcaselect(4);

    // check for changes in mux4 (LED 17-20)
    temp = mux4.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+16]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+16] = temp;
    }

    tcaselect(5);

    // check for changes in mux5 (LED 21-24)
    temp = mux5.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+20]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+20] = temp;
    }

    tcaselect(6);

    // check for changes in mux6 (LED 25-28)
    temp = mux6.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+24]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+24] = temp;
    }

    tcaselect(7);

    // check for changes in mux6 (LED 29-32)
    temp = mux7.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+28]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+28] = temp;
    }
  }

  // only send data, if no value has changed and if the values have not yet been written to the stream
  if(!valueChanged && !changesWritten) {

    // send data to the serial port
    for(int16_t iDiode=0; iDiode<nPhotodiodes; ++iDiode) {
      sprintf(photoReport,"%d %d",iDiode,adc[iDiode]);
      Serial.println(photoReport);
    }

    // values have been written
    changesWritten = true;

  }

  // if the values have been currently changed, these changes have not yet been written to the serial port
  if(valueChanged) {
    changesWritten = false;
  }
  
  ++counter;
  
  delay(100);
}
