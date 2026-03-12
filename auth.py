#!/usr/bin/env python3

import serial
from serial.tools import list_ports

AUTH = {
    "1": b"AT+SUDDLMOD=0,0\r",
    "2": b"AT+FUS?\r",
}

print("Select one to boot into Download Mode")
print("1) Auth 1")
print("2) Auth 2")

choice = input("Choice: ").strip()
cmd = AUTH.get(choice)

if not cmd:
    print("Invalid option")
    exit(1)

port = None
for p in list_ports.comports():
    if p.vid == 0x04E8:
        port = p.device
        break

if not port:
    print("No Samsung serial port found")
    exit(1)

print("Sending auth...")

with serial.Serial(port, 115200, timeout=1) as s:
    s.write(cmd)

print("Done")