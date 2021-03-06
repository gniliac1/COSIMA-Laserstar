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

void bluetoothCOM(void * pvParameters){
      drive = SerialBT.read();
      SerialBT.println(drive);
}

void Setup(){

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

    xTaskCreatePinnedToCore(
                    bluetoothCOM,   /* Function to implement the task */
                    "bluetoothCOM", /* Name of the task */
                    10000,      /* Stack size in words */
                    NULL,       /* Task input parameter */
                    1,          /* Priority of the task */
                    NULL,       /* Task handle. */
                    &Task1
                    1);         /* Core */
 
  SerialBT.println("Task created...");

}

void loop(){

     if(drive == "119"){
    ledcWrite(1, 150);
    //Serial.println(drive);
    //SerialBT.print("moved forward");
    /*delay(1000);
    ledcWrite(1, 0);*/
    }

  if(drive == "97"){
    ledcWrite(3, 255);
    //Serial.println(drive);
    //SerialBT.print("moved left");
    /*delay(2000);
    ledcWrite(3, 0);
    ledcWrite(1, 0);*/
    }

  if(drive == "100"){
    ledcWrite(4, 255);
    //Serial.println(drive);
    //SerialBT.print("moved right");
    /*delay(2000);
    ledcWrite(4, 0);
    ledcWrite(1, 0);*/
  }

  if(drive == "115"){
    ledcWrite(2, 150);
    //Serial.println(drive);
    //SerialBT.print("moved backwards");
    /*delay(1000);
    ledcWrite(2, 0);*/
    }
    
  if(drive == "113"){
    ledcWrite(1, 0);
    ledcWrite(2, 0);
    ledcWrite(3, 0);
    ledcWrite(4, 0);
    }

}
