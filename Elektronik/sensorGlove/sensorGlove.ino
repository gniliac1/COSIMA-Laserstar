#include <Wire.h>
#include <LSM6.h>
#include <LIS3MDL.h>

LSM6 Gyro; 
LIS3MDL Magnet; 

#define daumen A0
#define zeigefinger A1
#define mittelfinger A2
#define ringfinger A3
#define kleinerfinger A4

int daumenValue, zeigefingerValue, mittelfingerValue, ringfingerValue, kleinerfingerValue;

void setup(){
    Wire.begin();
    Serial.begin(9600);

    pinMode(daumen, OUTPUT);
    pinMode(zeigefinger, OUTPUT);
    pinMode(mittelfinger, OUTPUT);
    pinMode(ringfinger, OUTPUT);
    pinMode(kleinerfinger, OUTPUT);

    Magnet.enableDefault();
    Gyro.enableDefault();
}

void loop(){
    //Read Gyro data i2c and print it
    Gyro.read();
    snprintf(report, sizeof(report), "A: %6d %6d %6d    G: %6d %6d %6d",
        Gyro.a.x, Gyro.a.y, Gyro.a.z,
        Gyro.g.x, Gyro.g.y, Gyro.g.z);
    Serial.println(report);

    //Read Magent data i2c and pritn it
    Magnet.read();
    snprintf(report, sizeof(report), "M: %6d %6d %6d",
        Magnet.m.x, Magnet.m.y, Magnet.m.z);
    Serial.println(report);
    
    //Read finger data single wire and print it
    daumenValue = analogRead(daumen);
    zeigefingerValue = analogRead(zeigefinger);
    mittelfingerValue = analogRead(mittelfinger);
    ringfingerValue = analogRead(ringfinger);
    kleinerfingerValue = analogRead(kleinerfinger);

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

}