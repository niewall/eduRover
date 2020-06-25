import struct
import time
import serial


def drive(pCommand):

    # Convert String like "/1,200,20,1,200,20" to list like [1, 200, 20, 1, 200, 20]
    pCommand = pCommand[1:]
    print(pCommand)
    commandList = pCommand.split(',')
    commandList = list(map(int, commandList))
    print(commandList)

    index = 0

    data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
    while data != b'finished':
        data = arduino.readline()[:-2]

    for z in range(6):  # Every 6 values are one Driving Command for both Motors
        arduino.write(struct.pack('>B', int(commandList[index])))
        time.sleep(0.01)
        index += 1
    print("______")

