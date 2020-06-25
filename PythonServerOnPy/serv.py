from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import serial
import struct
import time
import executer
import os
import netifaces
from directDrive import drive

Raspberry = False
if Raspberry:
    import write

inputF = ""

arduino = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.1)

class Serv(BaseHTTPRequestHandler):

    def do_PUT(self):  # For whole Programms    //in cmd: curl -T input.txt http://192.168.2.186:8080/
        filename = os.path.basename(self.path)
        print(self.path)
        file_length = int(self.headers['Content-Length'])
        with open('input.txt', 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Raspberry saved "%s"\n' % filename
        write.writeToScreen("Incomming File")
        self.wfile.write(reply_body.encode('utf-8'))
        makePyFileAndExecute()

    def do_GET(self):  # For direct Commands
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


def execute(pOutput):
    i = 0
    while i < len(pOutput):
        data = arduino.readline()[:-2]  # [:-2]  löscht den Zeilenumbruch
        if data != b'':
            print(data)
        if data == b'finished':

            for z in range(6):  # Every 6 values are one Driving Command for both Motors
                arduino.write(struct.pack('>B', int(pOutput[i])))
                #time.sleep(0.1)
                i += 1
            print("______")


def makePyFileAndExecute():  # Die Leere Beispieldatei mit der importierten Datei kombinieren und danach ausführen


    # Reading data from file1
    with open('emptyExample.txt') as fp:
        data = fp.read()

    # Reading data from file2
    with open('input.txt') as fp:
        lines = fp.read().split("\n")
        newlines = []
        for line in lines:
            line = line.rstrip()
            newline = line[:0] + '    ' + line[0:]  # Absatz vor jede Zeile Schreiben
            newlines.append(newline)
    with open("input.txt", "w") as newfile:
        newfile.write("\n".join(newlines))
    with open("input.txt") as newfile:
        data2 = newfile.read()

    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2

    with open('programF.py', 'w') as fp:
        fp.write(data)

    output = executer.execute()  # Gets the output from the written program
    execute(output)


hostname = socket.gethostname()
ip = netifaces.ifaddresses("{C8D05377-E107-4707-A118-BACCD51D82B5}")[2][0]["addr"]

print("MotorControl 3000X Pro ver 0.0.3 by NieWall")
print("Der Computer-Name: " + hostname)
print("Die IP-Adresse/n: ")
print("running on IP: " + ip)
print("running on Port 8080")
print()
if Raspberry:
    write.writeToScreen("Name: " + hostname)
    write.writeToScreen("IP: " + ip)
    write.writeToScreen("Port: 8080")

httpd = HTTPServer((ip, 8080), Serv)
httpd.serve_forever()
