import serial
import serial.tools.list_ports

def send_high(serial_port):
    ser = serial.Serial(serial_port, 9600)
    ser.write(b'HIGH\n')
    print("Sent: HIGH")

def send_low(serial_port):
    ser = serial.Serial(serial_port, 9600)
    ser.write(b'LOW\n')
    print("Sent: LOW")

def get_serial_ports():
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(port, desc, hwid))
