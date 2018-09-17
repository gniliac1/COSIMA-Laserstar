#include <Wire.h>
#include <LIS3MDL.h>
#include <LSM6.h>

#define daumen 0
#define zeigefinger 1
#define mittelfinger 2
#define ringfinger 3
#define kleinerfinger 4

LIS3MDL mag;
LSM6 imu;

char reportCompass[80];
char reportAccelerometer[80];
char reportGyroscope[80];
char reportBendingSensor[160];

void setup()
{
  Serial.begin(9600);
  Wire.begin();

  if (!mag.init())
  {
    Serial.println("Failed to detect and initialize magnetometer!");
    while (1);
  }

  if (!imu.init())
  {
    Serial.println("Failed to detect and initialize IMU!");
    while (1);
  }
  
  imu.enableDefault();
  mag.enableDefault();
}

void loop()
{
  
  // send data only when you receive data:
  if (Serial.available() > 0) {
    
    // read the incoming byte:
    int incomingByte = Serial.read();
    
    // check whether this is the expected byte
    if (incomingByte == 'a') {

      // read compass data
      mag.read();
      snprintf(reportCompass, sizeof(reportCompass), "0 %d %d %d", mag.m.x, mag.m.y, mag.m.z);

      // read accelerometer & gyroscope data
      imu.read();
      snprintf(reportAccelerometer, sizeof(reportAccelerometer), "1 %d %d %d", imu.a.x, imu.a.y, imu.a.z);
      snprintf(reportGyroscope, sizeof(reportGyroscope), "2 %d %d %d", imu.g.x, imu.g.y, imu.g.z);

      // read bending sensor data
      int daumenValue = analogRead(daumen);
      int zeigefingerValue = analogRead(zeigefinger);
      int mittelfingerValue = analogRead(mittelfinger);
      int ringfingerValue = analogRead(ringfinger);
      int kleinerfingerValue = analogRead(kleinerfinger);
      snprintf(reportBendingSensor, sizeof(reportBendingSensor), "3 %d %d %d %d %d", 
                daumenValue, zeigefingerValue, mittelfingerValue, ringfingerValue, kleinerfingerValue);
      
      // send data
      Serial.println(reportCompass);
      Serial.println(reportAccelerometer);
      Serial.println(reportGyroscope);
      Serial.println(reportBendingSensor);
    
    } // incomingByte == 'a'
  
  } // Serial.available() > 0
  
  delay(1000);
}
