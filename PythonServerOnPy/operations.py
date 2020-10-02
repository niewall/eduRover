import struct
import time
from directDrive import *

from write import writeToScreen, writeCach, showCachText

Raspberry = False
if Raspberry:
    import serial

from abstand import distanz, ledAn, sound


output = []
ArrayMethode = False


def forward(pSpeed, pTime):
    if ArrayMethode:
        output.extend([1, pSpeed, pTime, 1, pSpeed, pTime])
    else:
        send([1, pSpeed, pTime, 1, pSpeed, pTime])


def backward(pSpeed, pTime):
    if ArrayMethode:
        output.extend([2, pSpeed, pTime, 2, pSpeed, pTime])
    else:
        send([2, pSpeed, pTime, 2, pSpeed, pTime])

def turn(pDirection, pSpeed, pTime):
    if ArrayMethode:
        if pDirection == "rechts" or pDirection == "right":
            output.extend([1, pSpeed, pTime, 2, pSpeed, pTime])
        elif pDirection == "links" or pDirection == "left":
            output.extend([2, pSpeed, pTime, 1, pSpeed, pTime])
    else:
        if pDirection == "rechts" or pDirection == "right":
            send([1, pSpeed, pTime, 2, pSpeed, pTime])
        elif pDirection == "links" or pDirection == "left":
            send([2, pSpeed, pTime, 1, pSpeed, pTime])

def write(pText):
    writeToScreen(pText)

def writeInCach(pText):
    writeCach(pText)

def showCach():
    showCachText()


def abstand():
    return distanz()

def wait(pTime):
    time.sleep(pTime)

def led(pFarbe):
    ledAn(pFarbe)

def piep(mode, time):

    if mode == 1:
        sound(500, time)
    if mode == 2:
        sound(1000, time)
    if mode == 3:
        sound(1500, time)
    if mode == 4:
        sound(2000, time)
    if mode == 5:
        sound(2500, time)
    if mode == 6:
        sound(3000, time)

def send(commandList):

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
        GPIO.output(serB1, False)
        GPIO.output(serB2, True)


    print("Direction1: " + str(direction1) + " | " + "Direction2: " + str(direction2) + " | " + "Time1: " + str(
        pTime) + " |  ")

    time.sleep(pTime)
    GPIO.output(enA, False)
    GPIO.output(enB, False)
    GPIO.output(serA1, False)
    GPIO.output(serA2, False)
    GPIO.output(serB1, False)
    GPIO.output(serB2, False)
    p.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)


