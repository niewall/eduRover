from http.server import HTTPServer, BaseHTTPRequestHandler

# config "sudo nano /etc/systemd/system/startServer.service" for autostart
# to enable: "sudo systemctl daemon-reload" then:
# "sudo systemctl enable startServer.service" and
# "sudo systemctl start startServer.service"

# required packages for display: "sudo apt-get install libtiff5" and "sudo apt-get install libopenjp2-7"


import socket
import serial
import struct
import time
import executer
import network
import os
import netifaces
from directDrive import drive
import abstand
from subprocess import call

import write

inputF = ""


class Serv(BaseHTTPRequestHandler):

    def do_PUT(self):  # //in cmd: curl -T input.txt http://192.168.2.186:8080/
        """
        Mittels http-PUT Befehl wird ein Programmcode vom Rover empfangen und in input.txt gespeichert.
        An den Sender wird eine Antwort zurückgeschickt.
        Ist der Akku leer, wird der Rover heruntergefahren.
        """

        filename = os.path.basename(self.path)
        print(self.path)
        file_length = int(self.headers['Content-Length'])
        with open('/home/pi/eduRover/PythonServerOnPy/input.txt', 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Raspberry saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

        batteryStatePercS = abstand.batteryState()
        if batteryStatePercS <= 5:
            write.writeToScreen("Battery too Low")
            write.writeToScreen("Bitte Ausschalten")
            call("sudo nohup shutdown -h now", shell=True)
        else:
            write.updateBatPerc(batteryStatePercS)
            write.showBattery(True)
            makePyFileAndExecute()

    def do_GET(self):  # For direct Commands
        """
        Mittels http-GET Befehl wird ein einzelner Fahrbefehl vom Rover empfangen.
        """
        if str(self.path) != "/favicon.ico":
            try:
                command = str(self.path)
                drive(command)
                self.send_response(200)
                self.end_headers()
                self.path = ""
                self.wfile.write(bytes("erfolgreich", 'utf-8'))
            except:
                self.end_headers()
                self.wfile.write(bytes("error", 'utf-8'))


def makePyFileAndExecute():
    """
    Die leere Beispieldatei mit der importierten Datei kombinieren und dann ausführen.
    """

    # den Text aus der leeren Beispieldatei einlesen
    with open('/home/pi/eduRover/PythonServerOnPy/emptyExample.txt') as fp:
        data = fp.read()

    # den Text aus der empfangenden Datei einlesen
    with open('/home/pi/eduRover/PythonServerOnPy/input.txt') as fp:
        lines = fp.read().split("\n")  # den empfangen Programmcode Zeile für Zeile in eine Liste einfügen
        newlines = []  # neue leere Liste "newlines" erstellen
        for line in lines:
            line = line.rstrip()
            newline = line[:0] + '    ' + line[0:]  # einen Absatz vor jede Zeile Schreiben
            newlines.append(newline)
    with open("/home/pi/eduRover/PythonServerOnPy/input.txt", "w") as newfile:
        newfile.write("\n".join(newlines))  # empfangene Datei umschreiben, damit sie ausgeführt werden kann
    with open("/home/pi/eduRover/PythonServerOnPy/input.txt") as newfile:
        data2 = newfile.read()  # umgeänderte empfangene Datei neu als "data2" einlesen

    # die leere Beispieldatei mit der angepassten Input-Datei kombinieren
    data += "\n"
    data += data2

    # die fertig angepasste Datei nach "programF.py" schrieben
    with open('/home/pi/eduRover/PythonServerOnPy/programF.py', 'w') as fp:
        fp.write(data)

    executer.execute()  # das angepasste Programm wird ausgeführt


hostname = socket.gethostname()

try:
    ip = netifaces.ifaddresses("wlan0")[2][0]["addr"]
except:
    network.networkMenu()
    while True:
        i = 1


print("Education Robot Software on Pi (ERoSPi) by NieWall")
print("Der Computer-Name: " + hostname)
print("running on IP: " + ip)
print("running on Port 8080")
print()

batteryStatePerc = abstand.batteryState()



# Beim Start wichtige Informationen anzeigen
write.writeToScreen("IP:  " + ip)
write.writeToScreen("Port:  8080")
write.writeToScreen("Battery State:  " + str(batteryStatePerc) + "%")
if batteryStatePerc <= 5:
    write.writeToScreen("Battery too Low")
    write.writeToScreen("-> POWER OFF")
    call("sudo nohup shutdown -h now", shell=True)


httpd = HTTPServer((ip, 8080), Serv)
httpd.serve_forever()


