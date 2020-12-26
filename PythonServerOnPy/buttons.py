import RPi.GPIO as GPIO

# Buttons get pulled to vcc(+) over a resistor. If pressed, they get connected to Ground and output LOW (False)
# That would be the Pressed state, therefore the opposite state is returned.

buttonPin1 = 10
buttonPin2 = 9

GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonPressed(buttonNr):
    buttonState1 = GPIO.input(buttonPin1)
    buttonState2 = GPIO.input(buttonPin2)

    if buttonNr == 1:
        return not buttonState1
    if buttonNr == 2:
        return not buttonState2

    if buttonNr != 1 and buttonNr != 2:
        return False
