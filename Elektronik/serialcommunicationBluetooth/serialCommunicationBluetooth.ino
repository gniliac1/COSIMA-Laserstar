#include <SoftwareSerial.h>

SoftwareSerial bt(7,6); // RX, TX

int thisByte = 33;

void setup() {
  bt.begin(9600);
  bt.println("ASCII Table ~ Character Map");
}

void loop() {
  bt.write(thisByte);

  bt.print(", dec: ");
  bt.print(thisByte);
  bt.print(", hex: ");
  bt.print(thisByte, HEX);
  bt.print(", oct: ");
  bt.print(thisByte, OCT);
  bt.print(", bin: ");
  bt.println(thisByte, BIN);

  if(thisByte == 126) {
    thisByte = 32;
  }
  thisByte++;
}
