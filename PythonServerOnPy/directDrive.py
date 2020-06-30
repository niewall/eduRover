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


def drive(pCommand):

    # Convert String like "/1,200,20,1,200,20" to list like [1, 200, 20, 1, 200, 20]
    pCommand = pCommand[1:]
    print(pCommand)
    commandList = pCommand.split(',')
    commandList = list(map(int, commandList))
    print(commandList)

    index = 0

    pTime = commandList[2]
    speed = commandList[0]
    speed2 = commandList[3]

    if speed == 1:
        duty = 12
    if speed == 2:
        duty = 2
    if speed2 == 1:
        duty2 = 12
    if speed2 == 2:
        duty2 = 2

    GPIO.output(servoPIN, True)
    GPIO.output(servoPIN2, True)
    p.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty2)
    print(speed, pTime,speed2, pTime)
    time.sleep(pTime)
    GPIO.output(servoPIN, False)
    GPIO.output(servoPIN2, False)
    p.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)





