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
    #time.sleep(1)
    print(bt.readline())
    #time.sleep(0.1)
    
if direction == 'exit':
    bt.close()

