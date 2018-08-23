#include "BluetoothSerial.h"

#define forward 10 //gelb
#define backwards 11 //rot
#define left 5 //schwarz
#define right 9 // grün

BluetoothSerial bt;

String direction;


void setup(){
    int freq = 5000;
    int res = 8;
    ledcSetup(forward, freq, res);
    ledcSetup(backwards, freq, res);
    ledcSetup(left, freq, res);
    ledcSetup(right, freq, res);
    Serial.begin(9600);
    bt.begin("ESP32");
}

void loop(){
    direction = bt.readString();
    if (direction == "w"){
            ledcWrite(forward, 255);
            Serial.println(direction);
            bt.print("moved forward");
            delay(2000);
            ledcWrite(forward, 0);
      }
    if (direction == "s"){
            ledcWrite(backwards, 255);
            Serial.println(direction);
            bt.print("moved backwards");
            delay(2000);
            ledcWrite(backwards, 0);
      }
    if (direction == "a"){
            ledcWrite(left, 255);
            Serial.println(direction);
            bt.print("moved left");
            delay(2000);
            ledcWrite(left, 0);
      }
    if (direction == "d"){
            ledcWrite(right, 255);
            Serial.println(direction);
            bt.print("moved right");
            delay(2000);
            ledcWrite(right, 0);
      }
}

/*void forward(){
    analogWrite(forward, 255);
    delay(500);
    analogWrite(forward, 0);
}

void backwards(){
    analogWrite(backwards, 255);
    delay(500);
    analogWrite(backwards, 0);
}

void left(){
    analogWrite(left, 255);
}

void right(){
    analogWrite(right, 255);
}
*/
