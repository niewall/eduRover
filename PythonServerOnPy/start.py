from gpiozero import Button
import os
import time
button = Button(17)

while True:
    if button.is_pressed:
        #print("Button is pressed")
        os.system("serv.py 1")
        time.sleep(5)
    else:
        #print("Button is not pressed")