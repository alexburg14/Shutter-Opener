import serial,time
import serial.tools.list_ports

def send_high(serial_port):
    ser = serial.Serial(serial_port, 9600)
    time.sleep(2) # Serial needs a bit of time to initialize, 2s was the minimum that worked
    ser.write(b"HIGH\n")
    print("Sent: HIGH")

def send_low(serial_port):
    ser = serial.Serial(serial_port, 9600)
    time.sleep(2) # Serial needs a bit of time to initialize, 2s was the minimum that worked
    ser.write(b"LOW\n")
    print("Sent: LOW")

def get_serial_ports():
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(port, desc, hwid))
    return ports

