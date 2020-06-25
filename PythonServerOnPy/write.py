import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

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
fontKlein = ImageFont.truetype('/usr/share/fonts/truetype/lato/Lato-Bold.ttf', 10)




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

    disp.clear()
    disp.image(image)
    disp.display()


run = True
running = True
x = 0
