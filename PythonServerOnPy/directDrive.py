import RPi.GPIO as GPIO
import time

servoPIN = 17
servoPIN2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(0) # Initialisierung
p2 = GPIO.PWM(servoPIN2, 50) # GPIO 17 als PWM mit 50Hz
p2.start(0) # Initialisierung


def drive(pCommand):

    # Convert String like "/1,200,20,1,200,20" to list like [1, 200, 20, 1, 200, 20]
    pCommand = pCommand[1:]
    print(pCommand)
    commandList = pCommand.split(',')
    commandList = list(map(int, commandList))
    print(commandList)

    index = 0
    missCounter = 0

    pTime = commandList[2]
    direction1 = commandList[0]
    direction2 = commandList[3]
    speedDiff = commandList[1]

    if direction1 == 1:
        duty = 2
    if direction1 == 2:
        duty = 12
    if direction2 == 1:
        duty2 = 12
    if direction2 == 2:
        duty2 = 2

    print("Direction1: " + str(direction1) + " | " + "Direction2: " + str(direction2) + " | " + "Time1: " + str(pTime) +  " | " )

    GPIO.output(servoPIN, True)
    GPIO.output(servoPIN2, True)

    while index < pTime*100:
        time.sleep(0.01)

        index += 1

        if missCounter <= speedDiff:
            p.ChangeDutyCycle(duty)
            p2.ChangeDutyCycle(duty2)
        else:
            p.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)

    GPIO.output(servoPIN, False)
    GPIO.output(servoPIN2, False)
    p.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)





