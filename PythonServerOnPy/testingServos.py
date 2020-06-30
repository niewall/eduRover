import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
pwm=GPIO.PWM(03, 50)


def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

SetAngle(0)
print("0")
time.sleep(5)
SetAngle(90)
print("90")
time.sleep(5)
SetAngle(180)
print("180")
time.sleep(5)
pwm.stop()
GPIO.cleanup()
