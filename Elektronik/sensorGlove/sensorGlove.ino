#include <Wire.h>

#define Gyro 0x1101011b
#define Magnet 0x0011110b

#define daumen A0
#define zeigefinger A1
#define mittelfinger A2
#define ringfinger A3
#define kleinerfinger A4

void setup(){
    Wire.begin();
    Serial.begin(9600);
}

void loop(){
    gyroValue = wire.read(Gyro);
    magnetValue = wire.read(Magent);
    
    daumenValue = analogRead(daumen);
    zeigefingerValue = analogRead(zeigefinger);
    mittelfingerValue = analogRead(mittelfinger);
    ringfingerValue = analogRead(ringfinger);
    kleinerfingerValue = analogRead(kleinerfinger);

    Serial.print("Value Gyro = ");
    Serial.println(gyroValue);

    Serial.print("Value Magentometer = ");
    Serial.println(magnetValue);

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