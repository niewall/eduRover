import importlib
import programF
import write

def execute():
    programF.output.clear()  # Clearing the List before Every new request


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
        programF.output.clear()  # Clearing the List before Every new request
        print("Ein Fehler ist aufgetreten!")
        #Lampe leuchten lassen
    print("NEW: " + str(programF.output))
    return programF.output

