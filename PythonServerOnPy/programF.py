from operations import *


def program():
    def calcTime(strecke):
        time = strecke / speed
        timeInt = int(time)
        return timeInt

    speed = 2.75
    timeNeeded = calcTime(10)

    forward(6, timeNeeded)


