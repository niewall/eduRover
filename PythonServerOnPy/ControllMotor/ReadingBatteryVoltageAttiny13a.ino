//library Borad: MircoCore ATtiny13 https://github.com/MCUdude/MicroCore
//Settings: 9,6MHz internal clock, BOD disabled
//Bootloader: Arduino as ISP
//Programming Guide for ATtiny13: https://create.arduino.cc/projecthub/taunoerik/programming-attiny13-with-arduino-uno-07beba

int analogPin = A0;
int inPin = 0;
int signalPin = 4;
int intervall = 50;

float voltAtPin = 0.0;
int batteryPerc = 0;
int voltMathInt = 0;

void setup() {
  pinMode(inPin, INPUT);   
  pinMode(signalPin, OUTPUT);// Setzt den Digitalpin 13 als Outputpin
  digitalWrite(signalPin, 0);
}         

void loop() {
  //Serial.println("Pressed: " + String(pressed));

  if(digitalRead(inPin) == HIGH){
    readVoltage();
    delay(20);
    for(int i = 0; i< batteryPerc; i++){
      digitalWrite(signalPin, 1);
      delay(intervall);
      digitalWrite(signalPin, 0);
      delay(intervall);
    }
    delay(intervall);
  }
}


void readVoltage(){
  
  voltAtPin = (analogRead(A0) / 1024.00) * 5.1;
  voltMathInt = int(10*voltAtPin);
  batteryPerc= voltMathInt - 39; // 7 should be max, under 0 is to far discharched
  
}