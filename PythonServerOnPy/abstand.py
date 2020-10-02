# Bibliotheken einbinden

import RPi.GPIO as GPIO
import time

# GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# GPIO Pins zuweisen
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#Für die LED

blue = 0
green = 5
red = 6

GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

GPIO.output(blue, False)
GPIO.output(green, False)
GPIO.output(red, False)

#Für Piezo

led = 26
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)


def distanz():
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartZeit = time.time()
    StopZeit = time.time()

    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()

    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()

    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2


    return distanz

def ledAn(farbe):

    if farbe == "rot":
        GPIO.output(red, 1)
        GPIO.output(green, 0)
        GPIO.output(blue, 0)

    if farbe == "gruen":
        GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 0)

    if farbe == "blau":
        GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(blue, 1)

    if farbe == "lila":
        GPIO.output(red, 1)
        GPIO.output(green, 0)
        GPIO.output(blue, 1)

    if farbe == "gelb":
        GPIO.output(red, 1)
        GPIO.output(green, 1)
        GPIO.output(blue, 0)

    if farbe == "cyan":
        GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)

    if farbe == "weiß":
        GPIO.output(red, 1)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)


    if farbe == "aus":
        GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(blue, 0)



def sound(freq, t):          # Diese Funktion erzeugt eine bestimmte Zeit t lang
   dur=1.0/freq/2.0          # die Frequenz freq auf dem LED-Pin
   anz=int(t/dur/2)
   for i in range (0,anz):   # range macht, solange der zweite Wert kleiner ist
                             # (nicht gleich), darum beginnen wir bei 0
      GPIO.output(led, GPIO.HIGH)
      time.sleep(dur)
      GPIO.output(led, GPIO.LOW)
      time.sleep(dur)
