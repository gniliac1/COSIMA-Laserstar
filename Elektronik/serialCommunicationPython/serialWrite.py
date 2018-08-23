import serial, time

bt = serial.Serial('COM6', 115200, timeout=.1)
direction = 'f' #initialize with false value
bt.close()
bt.open()

while direction != 'exit':
    direction =input('WASD: ')
    bt.write(str.encode(direction))
    time.sleep(1)
    print(bt.readline())
    time.sleep(0.1)
    
if direction == 'exit':
    bt.close()

