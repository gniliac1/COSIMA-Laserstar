#import <SoftwareSerial.h>

#define forward 10
#define backwards 11
#define left 5
#define right 6

SoftwareSerial bt(7,6); //RX, TX

void setup(){
    pinMode(forward, OUTPUT);
    pinMode(backwards OUTPUT);
    pinMode(left, OUTPUT);
    pinMode(right, OUTPUT);

    string direction = '';
    bt.begin(9600);
}

void loop(){
    bt.read(direction);
    switch (direction){
        case 'W':
            forward();
            break;
        case 'S':
            backwards();
            break;
        case 'A'
            left();
            break;
        case 'D':
            right();
            break;
        default:
            break;
    }
}

void forward(){
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