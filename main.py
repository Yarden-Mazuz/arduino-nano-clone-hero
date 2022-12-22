#  written in python 3.9
import serial.tools.list_ports
from pynput.keyboard import Key, Controller

keyboard = Controller()
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(portList))  # allowing u to see which port the guitar is connected to.

port = input('Which port is your guitar connected to?')  # allowing u to choose the guitar's port

portVar = "COM" + str(port)
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
inputs = ['a', 's', 'd', 'e', 'w', 'q', 'z', 'x', 'c']  # the game inputs

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        packet = packet.decode('utf').rstrip('\n')  # taking button inputs from the chosen COM which the guitar is
        # connected to, the input comes in the from of 1 and 0 so that 1 is unpressed button and 0 is pressed
        print(packet)
        g = 0
        for i in inputs:
            if packet[g] == "0":
                keyboard.press(i)
            else:
                keyboard.release(i)
            g += 1

        # __old code__

        # if packet[0] == "0":
        #     keyboard.press('a')
        # else:
        #     keyboard.release('a')
        # if packet[1] == "0":
        #     keyboard.press('s')
        # else:
        #     keyboard.release('s')
        # if packet[2] == "0":
        #     keyboard.press('d')
        # else:
        #     keyboard.release('d')
        # if packet[3] == "0":
        #     keyboard.press('e')
        # else:
        #     keyboard.release('e')
        # if packet[4] == "0":
        #     keyboard.press('w')
        # else:
        #     keyboard.release('w')
        # if packet[5] == "0":
        #     keyboard.press('q')
        # else:
        #     keyboard.release('q')
        # if packet[6] == "0":
        #     keyboard.press('z')
        # else:
        #     keyboard.release('z')
        # if packet[7] == "0":
        #     keyboard.press('x')
        # else:
        #     keyboard.release('x')
        # if packet[8] == "0":
        #     keyboard.press('c')
        # else:
        #     keyboard.release('c')
