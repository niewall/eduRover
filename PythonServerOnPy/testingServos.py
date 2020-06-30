import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung



def drive(speed, timeV):
    if speed == 1:
        duty = 12
    if speed == -1:
        duty = 2
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    print(speed, timeV)
    time.sleep(timeV)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(0)

drive(1,5)
drive(-1,5)
drive(1,1)
drive(-1,1)




p.stop()
GPIO.cleanup()

