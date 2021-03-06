from datetime import datetime

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import abstand

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Display
RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
padding = -2
top = padding
yCurrent = 0
bottom = height - padding
draw = ImageDraw.Draw(image)
x = 0
yCr = 0
writeTextCach = ["", "", "", ""]
writeCachTextCach = ["", "", "", ""]
fontKlein = ImageFont.truetype('/home/pi/eduRover/PythonServerOnPy/Lato-Bold.ttf', 10)
last = datetime.now()
batPercWrite = abstand.batteryState()
showBatteryState = True





def writeCach(pText):

    writeCachTextCach[3] = pText
    for l in range(len(writeCachTextCach) - 1):
        writeCachTextCach[l] = writeCachTextCach[l + 1]

def showCachText():
    disp.clear()
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    yCrC = 0
    for l in range(len(writeCachTextCach) - 1):
        draw.text((x, yCrC), str(writeCachTextCach[l]), font=fontKlein, fill=255)
        yCrC = yCrC + 10

    disp.clear()
    disp.image(image)
    disp.display()


def writeToScreen(ppText):
    global yCr
    global writeTextCach
    pText = str(ppText)


    if len(pText) >= 58:

        disp.clear()
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        draw.text((x, 0), str(pText[:29]), font=fontKlein, fill=255)
        draw.text((x, 10), str(pText[29::58]), font=fontKlein, fill=255)
        draw.text((x, 20), str(pText[58:]), font=fontKlein, fill=255)

        drawBatteryState()
        disp.clear()
        disp.image(image)
        disp.display()


        #writeToScreen(pText[:29])
        #writeToScreen(pText[29::58])
        #writeToScreen(pText[58:])

        return

    if len(pText) > 29:
        writeToScreen(pText[:29])
        writeToScreen(pText[29:])
        return



    fit = False

    for l in range(len(writeTextCach) - 1):
        if writeTextCach[l] == "":
            writeTextCach[l] = str(pText)
            fit = True
            break

    if fit == False:
        writeTextCach[3] = pText
        for l in range(len(writeTextCach) - 1):
            writeTextCach[l] = writeTextCach[l + 1]
        disp.clear()
        draw.rectangle((0,0,width,height), outline=0, fill=0)

    yCr = 0
    for l in range(len(writeTextCach) - 1):
        draw.text((x, yCr), str(writeTextCach[l]), font=fontKlein, fill=255)
        yCr = yCr + 10

    drawBatteryState()
    disp.clear()
    disp.image(image)
    disp.display()


run = True
running = True
x = 0


def updateBatPerc(perc):
    global batPercWrite
    global last

    last = datetime.now()
    batPercWrite = perc


def showBattery(state):
    global showBatteryState
    if state:
        showBatteryState = True
    if not state:
        showBatteryState = False
        writeToScreen("")



def drawBatteryState():


    if showBatteryState:


        #Update Battery Status every 120 sec
        now = datetime.now()
        global last
        global batPercWrite

        diff = now - last
        if diff.total_seconds() > 120:
            batPercWrite = abstand.batteryState()
            last = datetime.now()

        batStart = 101
        length = 24

        #Battery Body:
        draw.line((batStart, 1, batStart + length, 1), fill=1)
        draw.line((batStart, 6, batStart + length, 6), fill=1)
        draw.line((batStart, 2, batStart, 6), fill=1)
        draw.line((batStart + length, 2, batStart + length, 6), fill=1)
        draw.rectangle((batStart + length, 3, batStart + length +3, 4), outline=1, fill=1)

        #Battery State Bar

        bars = int(batPercWrite / 100 * 7)

        for i in range(bars):
            draw.rectangle((batStart + 1 + (i*3), 2, batStart + 5 + (i * 3), 5), outline=1, fill=1)



