#import <SoftwareSerial.h>

#define forward 10
#define backwards 11
#define left 5
#define right 6

SoftwareSerial bt(7,6); //RX, TX

void setup(){
    pinMode(forward, OUTPUT);
    pinMode(backwards, OUTPUT);
    pinMode(left, OUTPUT);
    pinMode(right, OUTPUT);
    bt.begin(9600);
}

void loop(){
    char direction = bt.read();
    switch (direction){
        case 'W':
            analogWrite(forward, 255);
            bt.println(direction);
            break;
        case 'S':
            analogWrite(backwards, 255);
            bt.println(direction);
            break;
        case 'A':
            analogWrite(left, 255);
            bt.println(direction);
            break;
        case 'D':
            analogWrite(right, 255);
            bt.println(direction);
            break;
        default:
            break;
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
