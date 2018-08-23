#include "BluetoothSerial.h"

#define forward 10 //gelb
#define backwards 11 //rot
#define left 5 //schwarz
#define right 9 // grün

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

int pwm1 = 1;
int pwm2 = 2;
int pwm3 = 3;
int pwm4 = 4;

String drive;
int freq = 5000;
int res = 10;

BluetoothSerial SerialBT;
void setup() {
    
  SerialBT.begin("OktoAuto");
  Serial.begin(9600);
  pinMode(forward, OUTPUT);
  pinMode(backwards, OUTPUT);
  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT);

  ledcAttachPin(forward, pwm1);
  ledcAttachPin(backwards, pwm2);
  ledcAttachPin(left, pwm3);
  ledcAttachPin(right, pwm4);

  ledcSetup(pwm1, freq, res);
  ledcSetup(pwm2, freq, res);
  ledcSetup(pwm3, freq, res);
  ledcSetup(pwm4, freq, res);

  // put your setup code here, to run once:

}

void loop() {
  
  drive = SerialBT.read();
  if(drive == "119"){
    ledcWrite(pwm1, 255);
    Serial.println(drive);
    SerialBT.print("moved forward");
    delay(2000);
    ledcWrite(pwm1, 0);
    }
  if(drive == "97"){
    ledcWrite(pwm2, 255);
    Serial.println(drive);
    SerialBT.print("moved left");
    delay(2000);
    ledcWrite(pwm2, 0);
    }
  if(drive == "100"){
    ledcWrite(pwm3, 255);
    Serial.println(drive);
    SerialBT.print("moved right");
    delay(2000);
    ledcWrite(pwm3, 0);
    }
  if(drive == "115"){
    ledcWrite(pwm4, 255);
    Serial.println(drive);
    SerialBT.print("moved backwards");
    delay(2000);
    ledcWrite(pwm4, 0);
    }
  delay(300);


}
