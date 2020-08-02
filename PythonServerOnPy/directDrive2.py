import RPi.GPIO as GPIO
import time

servoPIN = 17
servoPIN2 = 27
sPIN = 19
sPIN2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
GPIO.setup(sPIN, GPIO.OUT)
GPIO.setup(sPIN2, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(0) # Initialisierung
p2 = GPIO.PWM(servoPIN2, 50) # GPIO 17 als PWM mit 50Hz
p2.start(0) # Initialisierung


def drive(pCommand):

    # Convert String like "/1,200,20,1,200,20" to list like [1, 200, 20, 1, 200, 20]
    pCommand = pCommand[1:]
    print(pCommand)
    commandList = pCommand.split(',')
    commandList = list(map(float, commandList))
    print(commandList)

    index = 0

    pTime = commandList[2]
    direction1 = commandList[0]
    direction2 = commandList[3]
    speedDiff = commandList[1]

    if direction1 == 1:
        duty = speedDiff
    if direction1 == 2:
        duty = 14-speedDiff
    if direction2 == 1:
        duty2 = 14-speedDiff
    if direction2 == 2:
        duty2 = speedDiff


    GPIO.output(servoPIN, True)
    GPIO.output(servoPIN2, True)
    GPIO.output(sPIN, True)
    GPIO.output(sPIN2, False)

    p.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty2)
    print("Direction1: " + str(direction1) + " | " + "Direction2: " + str(direction2) + " | " + "Time1: " + str(
        pTime) + " |  ")
    time.sleep(pTime)

    GPIO.output(servoPIN, False)
    GPIO.output(servoPIN2, False)
    GPIO.output(sPIN, False)
    GPIO.output(sPIN2, False)
    p.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)






