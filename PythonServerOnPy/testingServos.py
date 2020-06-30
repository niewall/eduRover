import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung



def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    print(angle, duty)
    time.sleep(5)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(0)

SetAngle(0)
SetAngle(90)
SetAngle(180)




p.stop()
GPIO.cleanup()

