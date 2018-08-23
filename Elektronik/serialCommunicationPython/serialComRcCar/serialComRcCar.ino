#import <SoftwareSerial.h>

#define forward 10 //gelb
#define backwards 11 //rot
#define left 5 //schwarz
#define right 9 // grün

SoftwareSerial bt(7,6); //RX, TX
String direction;


void setup(){
    int freq = 5000;
    int res = 8;
    forwardSetup(forward, freq, res);
    backwardsSetup(backwards, freq, res);
    leftSetup(left, freq, res);
    rightSetup(right, freq, res);
    Serial.begin(9600);
    bt.begin(9600);
}

void loop(){
    direction = bt.readString();
    if (direction == "w"){
            analogWrite(forward, 255);
            Serial.println(direction);
            bt.print("moved forward");
            delay(2000);
            analogWrite(forward, 0);
      }
    if (direction == "s"){
            analogWrite(backwards, 255);
            Serial.println(direction);
            bt.print("moved backwards");
            delay(2000);
            analogWrite(backwards, 0);
      }
    if (direction == "a"){
            analogWrite(left, 255);
            Serial.println(direction);
            bt.print("moved left");
            delay(2000);
            analogWrite(left, 0);
      }
    if (direction == "d"){
            analogWrite(right, 255);
            Serial.println(direction);
            bt.print("moved right");
            delay(2000);
            analogWrite(right, 0);
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
