import struct
import time
from directDrive import *

Raspberry = False
if Raspberry:
    from write import writeToScreen,writeCach, showCachText
    from abstand import distanz, ledAn, sound
    import serial


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

def send(pCommandArray):

    pTime = commandList[2]
    direction1 = commandList[0]
    direction2 = commandList[3]

    if direction1 == 1:
        duty = 12
    if direction1 == 2:
        duty = 2
    if direction2 == 1:
        duty2 = 12
    if direction2 == 2:
        duty2 = 2

    GPIO.output(servoPIN, True)
    GPIO.output(servoPIN2, True)
    p.ChangeDutyCycle(duty)
    p2.ChangeDutyCycle(duty2)
    print("Direction1: " + direction1 + "Direction2: " + direction2 + "Time1: " + pTime)
    time.sleep(pTime)
    GPIO.output(servoPIN, False)
    GPIO.output(servoPIN2, False)
    p.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)



