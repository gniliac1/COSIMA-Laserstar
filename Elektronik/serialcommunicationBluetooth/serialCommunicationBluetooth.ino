#include <SoftwareSerial.h>

SoftwareSerial bt(7,6); // RX, TX

int thisByte = 33;
int modus = 0;

void setup() {
  //Serial.begin(9600);
  bt.begin(9600);
  //bt.println("Modus? read(r) send(s) ");
  
}

void loop() {
  modus = bt.read();
  //Serial.println(modus);
  bt.print("Modus: ");
  bt.println(modus);
  
  if (modus == "0"){
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
  if(modus == "1"){
    if(bt){
      bt.println("active");
    }
  }
}
