#  written in python 3.9
import serial.tools.list_ports
from pynput.keyboard import Controller


def button_inputs_to_keyboard_inputs():
    current_guitar_input = 0
    for current_keyboard_input in keyboard_inputs:
        if guitar_inputs[current_guitar_input] == "0":
            keyboard.press(current_keyboard_input)
        else:
            keyboard.release(current_keyboard_input)
        current_guitar_input += 1


def port_configuration():
    ports = serial.tools.list_ports.comports()
    port_list = []

    for one_port in ports:
        port_list.append(str(one_port))
        print(str(port_list))

    chosen_port_number = input('Which port is your guitar connected to? COM')
    serial_inst.baudrate = 9600
    serial_inst.port = "COM" + str(chosen_port_number)


keyboard = Controller()
keyboard_inputs = ['a', 's', 'd', 'e', 'w', 'q', 'z', 'x', 'c']

serial_inst = serial.Serial()
port_configuration()
serial_inst.open()

while True:
    if serial_inst.in_waiting:
        guitar_inputs = serial_inst.readline()  # taking button inputs from the chosen COM which the guitar is
        # connected to, the input comes in the from of 1 and 0 so that 1 is unpressed button and 0 is pressed
        guitar_inputs = guitar_inputs.decode('utf').rstrip('\n')

        button_inputs_to_keyboard_inputs()
