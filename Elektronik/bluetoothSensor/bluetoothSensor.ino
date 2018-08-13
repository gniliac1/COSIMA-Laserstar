#include <SoftwareSerial.h>

#define input0 A0

SoftwareSerial bt(7,6); //RX, TX

float value0 = 0.0;
float value = 0.0;
float valueMittel = 0.0;

void setup() {
  pinMode(input0, INPUT);
  bt.begin(9600);

}

void loop() {
  for(int i = 0; i<10; i++){
  value0 = analogRead(input0);
  value += value0;
  delay(100);
  }
  valueMittel = (value / 10) * (5.0 / 1023.0);
  bt.print("Value0 = ");
  bt.println(valueMittel);
  value = 0;
  valueMittel = 0;
}
