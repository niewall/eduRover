import subprocess
import write
import keyboard

ssid = ""
passkey = ""
current = 0



def addToInput(pChar):
    global ssid
    global passkey
    global current

    # cls()

    if current == 0:
        ssid += pChar
        print(ssid)
    elif current == 1:
        passkey += pChar
        print(passkey)

    networkMenu()


def removeFromInput():
    global ssid
    global passkey
    global current

    # cls()

    if current == 0:
        ssid = ssid[:-1]
        print(ssid)
    elif current == 1:
        passkey = passkey[:-1]
        print(passkey)

    networkMenu()


def nextInput():
    global ssid
    global passkey
    global current

    if current == 0:
        current = 1
    elif current == 1:
        current = 0
        changeNetwork()


def key_press(key):
    global ssid
    global passkey
    global current

    if key.name == "backspace":
        removeFromInput()
    elif key.name == "enter":
        nextInput()
    else:
        addToInput(str(key.name))
        print(str(key.name))

keyboard.on_press(key_press)



def changeNetwork():

    p1 = subprocess.Popen(["wpa_passphrase", ssid, passkey], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["sudo", "tee", "-a", "/etc/wpa_supplicant/wpa_supplicant.conf", ">", "/dev/null"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()  # Give p1 a SIGPIPE if p2 dies.
    output,err = p2.communicate()

def networkMenu():
    global ssid
    global passkey
    global current

    write.writeCach("Netzwerkdaten eingeben")
    write.writeCach("SSID: " + ssid)
    write.writeCach("PWD:" + passkey)
    write.showCachText()

