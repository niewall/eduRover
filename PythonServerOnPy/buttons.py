import RPi.GPIO as GPIO

buttonPin1 = 10
buttonPin2 = 9

GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonPressed(buttonNr):
    buttonState1 = GPIO.input(buttonPin1)
    buttonState2 = GPIO.input(buttonPin2)

    if buttonNr == 1:
        return buttonState1
    if buttonNr == 2:
        return buttonState2

    if buttonNr != 1 and buttonNr != 2:
        return False
