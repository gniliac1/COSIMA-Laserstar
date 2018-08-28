import serial, time

ser = serial.Serial('COM7', 9600, timeout=.1)
bt = serial.Serial('COM6', 115200, timeout=.1)
direction = 'f' #initialize with false value
ser.close()
ser.open()
bt.close()
bt.open()

while direction != 'exit':
    direction =ser.readline()
    print(direction)
    bt.write(direction)
    print(bt.readline())
    
if direction == 'exit':
    bt.close()

