#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_ADS1015.h>                                                

//Initialize I2C addresses of multiplexers
Adafruit_ADS1015 mux0(0x48);
Adafruit_ADS1015 mux1(0x49);
Adafruit_ADS1015 mux2(0x4A);
Adafruit_ADS1015 mux3(0x4B);

SoftwareSerial bt(7,6); //RX, TX

const int16_t nPhotodiodes = 16;  // number of photodiodes
int16_t adc[nPhotodiodes];        // global array for photo current
bool valueChanged;                // indicates whether the photo current has changed compared to the previous iteration
bool changesWritten;              // ndcates whether the photo currents have already been written to the serial port
const int16_t threshold = 3;      // threshold by which the values have to be changed before they are communicated
int16_t temp;                     // temporary variable for storing the photo current
int16_t counter = 0;              // contains the current iteration of the loop

void setup() {
  
  // Set Gain level for OPA
  // GAIN_TWOTHIRDS - 2/3x gain +/- 6.144V  1 bit = 3mV (default)
  // GAIN_ONE       - 1x gain   +/- 4.096V  1 bit = 2mV
  // GAIN_TWO       - 2x gain   +/- 2.048V  1 bit = 1mV
  // GAIN_FOUR      - 4x gain   +/- 1.024V  1 bit = 0.5mV
  // GAIN_EIGHT     - 8x gain   +/- 0.512V  1 bit = 0.25mV
  // GAIN_SIXTEEN   - 16x gain  +/- 0.256V  1 bit = 0.125mV
  mux0.setGain(GAIN_FOUR);
  mux1.setGain(GAIN_FOUR);    
  mux2.setGain(GAIN_FOUR);    
  mux3.setGain(GAIN_FOUR);    
  
  Serial.begin(9600);
  mux0.begin();
  mux1.begin();
  mux2.begin();
  mux3.begin();

  changesWritten = false;

}

void loop() {
  
  // no value has changed yet
  valueChanged = false;

  // iterate over all diodes and check for changes in the photo current
  for(int16_t iDiode=0; iDiode < 4; ++iDiode) {
    // check for changes in mux0 (LED 1-4)
    temp = mux0.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode]) >= threshold ) {
      valueChanged = true;
      adc[iDiode] = temp;
    }
    
    // check for changes in mux1 (LED 5-8)
    temp = mux1.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+4]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+4] = temp;
    }
    
    // check for changes in mux2 (LED 9-12)
    temp = mux2.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+8]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+8] = temp;
    }

    // check for changes in mux3 (LED 13-16)
    temp = mux3.readADC_SingleEnded(iDiode);
    if( abs(temp - adc[iDiode+12]) >= threshold ) {
      valueChanged = true;
      adc[iDiode+12] = temp;
    }
  }

  // only send data, if no value has changed and if the values have not yet been written to the stream
  if(!valueChanged && !changesWritten) {

    // send data to the serial port
    for(int16_t iDiode=0; iDiode<nPhotodiodes; ++iDiode) {
      Serial.print(iDiode); Serial.print(" "); Serial.println(adc[iDiode]);
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
