import serial
import time

s = serial.Serial("COM5", 9600) #port is 11 (for COM12, and baud rate is 9600
time.sleep(2)    #wait for the Serial to initialize
txt = 'Ingresar ID'
s.write(txt.encode())
time.sleep(2)
while True:
    strs = input('Enter text: ')
    strs = strs.strip()
    if strs == 'exit' :
        strs = 'Gracias'
        strs = strs.strip()
        s.write(strs.encode())
        time.sleep(2)
        strs = '--Ctrl Alt Tec--'
        strs = strs.strip()
        s.write(strs.encode())
        time.sleep(3)
        exit()
    s.write(strs.encode())