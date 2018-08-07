#define leftTrigger 3
#define leftEcho 2
#define rightTrigger 7
#define rightEcho 8
#define forward 10
#define backwards 11
#define left 5
#define right 6

void setup() {

  pinMode (leftTrigger, OUTPUT);
  pinMode (leftEcho, INPUT);
  pinMode (rightTrigger, OUTPUT);
  pinMode (rightEcho, INPUT);

  pinMode (forward, OUTPUT);
  pinMode (backwards, OUTPUT);
  pinMode (left, OUTPUT);
  pinMode (right, OUTPUT);

  digitalWrite (leftTrigger, HIGH); //turn off left signal
  digitalWrite (rightTrigger, HIGH); //turn off right signal
  
  Serial.begin (9600);

}

void loop() {
  //int distanceRight = measureDistanceRight();
  int distanceLeft = measureDistanceLeft();
 
  // Measures distance left and right and determents if the car has to turn right, left or straight forward
  if (distanceLeft >= 50){
    analogWrite (forward, 255); //pwm with ~50% dutycycle
    delay (1000); //forward for 1s with half speed
    analogWrite (forward, 0); //stop for remeasurement
  }
  Serial.print("Distance: ");
  Serial.print(distanceLeft, DEC);
  Serial.print("\n");
  delay(3000);
/**  else if (distanceRight < 100) {
    analogWrite (left, 255); //full turn left
    analogWrite (forward, 125);
    delay(500);
    analogWrite (left, 0); 
    analogWrite (forward, 0);
  }*/
  /**else{
    analogWrite (right, 255); //full turn left
    analogWrite (forward, 125);
    delay(500);
    analogWrite (right, 0); 
    analogWrite (forward, 0);
  }*/
  

  
 
}

//measure distance with the ultrasonic sensor
int measureDistanceRight(){
  long rightDistance = 0;
  long echoTime = 0;

  digitalWrite (rightTrigger, LOW);
  delayMicroseconds(3);
  noInterrupts(); //we do not want any interrupts here to mess with the measurement
  digitalWrite (rightTrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite (rightTrigger, LOW);
  echoTime = pulseIn(rightEcho, HIGH); //measure time for echo to return
  interrupts();

  echoTime = (echoTime/2);
  rightDistance = echoTime / 29.1; //according to the internet this is the distance in cm

  return rightDistance;
  }

  int measureDistanceLeft(){
  long leftDistance = 0;
  long echoTime = 0;

  digitalWrite (leftTrigger, LOW);
  delayMicroseconds(3);
  noInterrupts(); //we do not want any interrupts here to mess with the measurement
  digitalWrite (leftTrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite (leftTrigger, LOW);
  echoTime = pulseIn(leftEcho, HIGH); //measure time for echo to return
  interrupts();

  echoTime = (echoTime/2);
  leftDistance = echoTime / 29.1; //according to the internet this is the distance in cm

  return leftDistance;
  }
