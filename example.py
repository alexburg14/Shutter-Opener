import shutter_opener as so
import time
so.get_serial_ports() # This will print the serial ports, then choose the one you want

so.send_high("/dev/cu.usbserial-1420")

time.sleep(2)

so.send_low("/dev/cu.usbserial-1420")