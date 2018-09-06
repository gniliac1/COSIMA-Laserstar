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

char report[80];
char reportI[80];

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
  mag.read();

  snprintf(report, sizeof(report), "M: %6d %6d %6d",
    mag.m.x, mag.m.y, mag.m.z);
    imu.read();

  snprintf(reportI, sizeof(reportI), "A: %6d %6d %6d    G: %6d %6d %6d",
    imu.a.x, imu.a.y, imu.a.z,
    imu.g.x, imu.g.y, imu.g.z);
  
  Serial.println(reportI);
  Serial.println(report);

    int daumenValue = analogRead(daumen);
    int zeigefingerValue = analogRead(zeigefinger);
    int mittelfingerValue = analogRead(mittelfinger);
    int ringfingerValue = analogRead(ringfinger);
    int kleinerfingerValue = analogRead(kleinerfinger);

    Serial.print("Value daumen = ");
    Serial.println(daumenValue);
    Serial.print("Value zeigefinger = ");
    Serial.println(zeigefingerValue);
    Serial.print("Value mittelfinger = ");
    Serial.println(mittelfingerValue);
    Serial.print("Value ringfinger = ");
    Serial.println(ringfingerValue);
    Serial.print("Value kleinerfinger = ");
    Serial.println(kleinerfingerValue);

  delay(100);
}
