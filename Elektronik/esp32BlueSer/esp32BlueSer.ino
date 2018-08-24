#include "BluetoothSerial.h"


uint8_t forward = 32; //gelb
uint8_t backwards = 33; //rot
uint8_t left = 14; //schwarz
uint8_t right = 12; // grün

uint8_t ledArray[4] = {1, 2, 3, 4}; // four led channels


#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif


String drive;

BluetoothSerial SerialBT;

void setup() {
    
  SerialBT.begin("OktoAuto");
  Serial.begin(9600);
  
  ledcAttachPin(forward, 1); // assign fblr pins to channels
  ledcAttachPin(backwards, 2);
  ledcAttachPin(left, 3);
  ledcAttachPin(right, 4);

  ledcSetup(1, 500, 8); // 10 kHz PWM, 8-bit resolution
  ledcSetup(2, 500, 8);
  ledcSetup(3, 500, 8);
  ledcSetup(4, 500, 8);

  // put your setup code here, to run once:

}

void loop() {
  
  drive = SerialBT.read();
  if(drive == "119"){
    ledcWrite(1, 195);
    Serial.println(drive);
    SerialBT.print("moved forward");
    delay(1000);
    ledcWrite(1, 0);
    }
  if(drive == "97"){
    ledcWrite(3, 200);
    ledcWrite(1, 195);
    Serial.println(drive);
    SerialBT.print("moved left");
    delay(2000);
    ledcWrite(3, 0);
    ledcWrite(1, 0);
    }
  if(drive == "100"){
    ledcWrite(4, 200);
    ledcWrite(1, 195);
    Serial.println(drive);
    SerialBT.print("moved right");
    delay(2000);
    ledcWrite(4, 0);
    ledcWrite(1, 0);
    }
  if(drive == "115"){
    ledcWrite(2, 195);
    Serial.println(drive);
    SerialBT.print("moved backwards");
    delay(1000);
    ledcWrite(2, 0);
    }

}
