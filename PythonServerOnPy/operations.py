import struct
import time
import serial

Raspberry = False
if Raspberry:
    from write import writeToScreen,writeCach, showCachText
    from abstand import distanz, ledAn, sound

arduino = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.1)

output = []
ArrayMethode = True


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

    commandArray = pCommandArray
    index = 0
    data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
    while data != b'finished':
        data = arduino.readline()[:-2]
        print(data)

    for z in range(6):  # Every 6 values are one Driving Command for both Motors
        if int(commandArray[index]) > 255:
            commandArray[index] = 255
        arduino.write(struct.pack('>B', int(commandArray[index])))
        #time.sleep(0.01)
        index += 1
    print("______")

    #Waiting for Command to be executed because for some reason the finish is posted to soon
    if commandArray[2] > commandArray[5]:
        time.sleep(commandArray[2])
    else:
        time.sleep(commandArray[5])



