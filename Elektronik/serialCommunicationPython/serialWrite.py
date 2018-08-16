import serial, time

bt = serial.Serial('COMx', 9600, timeout=.1)
bt.open()

while direction != 'exit':
    direction =input('WASD: ')
    bt.write(direction)
    
if direction == 'exit'
    bt.close()
