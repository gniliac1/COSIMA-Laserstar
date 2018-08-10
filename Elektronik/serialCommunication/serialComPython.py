import serial
import time

bt = serial.Serial('COM5', 9600, timeout = .1) #COMx is used COM-Port x must be checked on PC
mod = input('Modus? r(read), s(send)')

if mod == 'r':
    while True:
        data = bt.readline()[:-2]
        input = input('>> ')

        if data:
            print(data)

        if input == 'exit':
            bt.close()
            exit()
        else:
            bt.write(input + '\r\n')
            out = ''
            time.sleep(1)
            while bt.inWaiting() > 0:
                out += bt.read(1)
                if out != '':
                    print ('>>' + out)

