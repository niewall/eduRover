import importlib
import programF
import write

def execute():
    """
    Der Code in programF wird ausgeführt.
    Bei einem Fehler wird dieser auf dem Roverbildschirm und in der Konsole ausgegeben.
    Der Code in programmF greift auf Methoden aus operations.py zu, welche die einfache Programmierung des
    Rovers ermöglichen.
    """
    try:
        importlib.reload(programF)
        programF.program()
    except Exception as e:
        print(e)
        write.writeToScreen("ERROR:" + str(e))
        with open('/home/pi/eduRover/PythonServerOnPy/emptyExample.txt') as fp:
            data = fp.read()
        data += "\n"
        with open('/home/pi/eduRover/PythonServerOnPy/programF.py', 'w') as fp:
            fp.write(data)
        print("Ein Fehler ist aufgetreten!")

