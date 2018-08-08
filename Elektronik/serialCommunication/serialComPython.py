import serial
import time 

readData = serial.Serial('COMx', 9600, timeout = .1) #COMx is used COM-Port x must be checked on PC
sendData = serial.Serial('COMx', 9600, timeout = .1) 

while True:
    data = readData.readline()[:-2]
    input = input('>> ')

    if data:
        print(data)

    if input == 'exit':
        sendData.close()
        exit()
    else:
        sendData.write(input + '\r\n')
        out = ''
        time.sleep(1)
        while sendData.inWaiting() > 0:
            out +=readData.read(1)
        if out != '':
            print ('>>' + out)

