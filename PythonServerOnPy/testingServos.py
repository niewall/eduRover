import RPi.GPIO as GPIO
import time

servoPIN = 17
servoPIN2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
p2 = GPIO.PWM(servoPIN2, 50) # GPIO 17 als PWM mit 50Hz
p2.start(2.5) # Initialisierung



def drive(speed, timeV,speed2, timeV2,):
    if speed == 1:
        duty = 12
    if speed == -1:
        duty = 2
    if speed2 == 1:
        duty2 = 12
    if speed2 == -1:
        duty2 = 2
    GPIO.output(servoPIN, True)
    GPIO.output(servoPIN2, True)
    p.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty2)
    print(speed, timeV,speed2, timeV2)
    time.sleep(timeV)
    GPIO.output(servoPIN, False)
    GPIO.output(servoPIN2, False)
    p.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)

drive(1,5,-1,5)
drive(-1,5,-1,5)
drive(1,1,1,1)
drive(-1,1,-1,1)

p.stop()
GPIO.cleanup()

