// Motoransteuerung mit dem Arduino bei dem Prototyp. Bei neuer Version nicht mehr in Verwendung.

// MD03A_Motor_basic + encoder

#define InA1            9                      // INA motor pin
#define InB1            10                      // INB motor pin
#define PWM1            11                      // PWM motor pin
#define encodPinA1      2                       // encoder A pin
#define encodPinB1      4                       // encoder B pin

#define InA2            7                      // INA motor pin
#define InB2            8                      // INB motor pin
#define PWM2            6                       // PWM motor pin
#define encodPinA2      3                       // encoder A pin
#define encodPinB2      5                       // encoder B pin

#define LOOPTIME        100                     // PID loop time

unsigned long lastMilli = 0;                    // loop timing
unsigned long lastMilliPrint = 0;               // loop timing
long count = 0;                                 // rotation counter
long countInit;
long tickNumber = 0;
boolean run = false;                                     // motor moves

unsigned long lastMilli2 = 0;                    // loop timing
unsigned long lastMilliPrint2 = 0;               // loop timing
long count2 = 0;                                 // rotation counter
long countInit2;
long tickNumber2 = 0;
boolean run2 = false; 

float speed1 = 0.0;
float speed2 = 0.0;

float val[6];

void setup() {

 Serial.begin(9600);

 pinMode(InA1, OUTPUT);
 pinMode(InB1, OUTPUT);
 pinMode(PWM1, OUTPUT);
 pinMode(encodPinA1, INPUT);
 pinMode(encodPinB1, INPUT);
 digitalWrite(encodPinA1, HIGH);                      // turn on pullup resistor
 digitalWrite(encodPinB1, HIGH);

 pinMode(InA2, OUTPUT);
 pinMode(InB2, OUTPUT);
 pinMode(PWM2, OUTPUT);
 pinMode(encodPinA2, INPUT);
 pinMode(encodPinB2, INPUT);
 digitalWrite(encodPinA2, HIGH);                      // turn on pullup resistor
 digitalWrite(encodPinB2, HIGH);

}

void loop() {

  Serial.println("finished");

  for( int i = 0; i<6;i++){
  while (Serial.available() == 0);
  val[i] = Serial.read();
  //Serial.println(val[i]);
  }

//map speed 1-10 into pwm 1-255
  speed1 = map(val[1],0,10,0,255);
  speed2 = map(val[4],0,10,0,255);

//Direction (1,2), Speed PWM, Ticks, time in mSec
  moveMotor(val[0], speed1, 464*2);  //Direction (1,2), Speed PWM, Ticks
  moveMotor2(val[3], speed2, 464*2);

  if((val[2] - val[5]) < 0){
    delay(val[2]*100);
    motorBrake();
    delay(((val[2] - val[5]) * (-1))*100);
    motorBrake2();
  }else{
    delay(val[5]*100);
    motorBrake2();
    delay((val[2] - val[5])*100);
    motorBrake();

  }
}

void moveMotor(int direction1, int PWM_val, long tick)  {
 if(direction1==1)          motorForward(PWM_val);
 else if(direction1==2)    motorBackward(PWM_val);
}

void moveMotor2(int direction2, int PWM_val2, long tick2)  {
 if(direction2==1)          motorForward2(PWM_val2);
 else if(direction2==2)    motorBackward2(PWM_val2);
}

void motorForward(int PWM_val)  {
 analogWrite(PWM1, PWM_val);
 digitalWrite(InA1, LOW);
 digitalWrite(InB1, HIGH);
 run = true;
}

void motorBackward(int PWM_val)  {
 analogWrite(PWM1, PWM_val);
 digitalWrite(InA1, HIGH);
 digitalWrite(InB1, LOW);
 run = true;
}

void motorBrake()  {
 analogWrite(PWM1, 0);
 digitalWrite(InA1, HIGH);
 digitalWrite(InB1, HIGH);
 run = false;
}

void motorForward2(int PWM_val2)  {
 analogWrite(PWM2, PWM_val2);
 digitalWrite(InA2, LOW);
 digitalWrite(InB2, HIGH);
 run = true;
}

void motorBackward2(int PWM_val2)  {
 analogWrite(PWM2, PWM_val2);
 digitalWrite(InA2, HIGH);
 digitalWrite(InB2, LOW);
 run = true;
}

void motorBrake2()  {
 analogWrite(PWM2, 0);
 digitalWrite(InA2, HIGH);
 digitalWrite(InB2, HIGH);
 run2 = false;
}}