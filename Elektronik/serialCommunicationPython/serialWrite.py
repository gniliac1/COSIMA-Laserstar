import serial, time

bt = serial.Serial('COMx', 9600, timeout=.1)
bt.open()
direction = 'f' #initialize with false value

while direction != 'exit':
    direction =input('WASD: ')
    bt.write(direction)
    time.sleep(0.1)
    
if direction == 'exit':
    bt.close()
