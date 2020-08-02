import RPi.GPIO as GPIO
import time

enA = 18
enB = 12
serA1 = 17
serA2 = 27
serB1 = 5
serB2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.setup(serA1, GPIO.OUT)
GPIO.setup(serA2, GPIO.OUT)
GPIO.setup(serB1, GPIO.OUT)
GPIO.setup(serB2, GPIO.OUT)

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
    duty = commandList[1]
    duty2 = commandList[4]




    GPIO.output(enA, True)
    GPIO.output(enB, True)
    p.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty2)

    if direction1 == 1:
        GPIO.output(serA1, True)
        GPIO.output(serA2, False)
    if direction1 == 2:
        GPIO.output(serA1, False)
        GPIO.output(serA2, True)
    if direction2 == 1:
        GPIO.output(serB1, True)
        GPIO.output(serB2, False)
    if direction2 == 2:
        GPIO.output(serB1, True)
        GPIO.output(serB2, False)


    print("Direction1: " + str(direction1) + " | " + "Direction2: " + str(direction2) + " | " + "Time1: " + str(
        pTime) + " |  ")
    
    time.sleep(pTime)
    GPIO.output(enA, False)
    GPIO.output(enB, False)
    p.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)






