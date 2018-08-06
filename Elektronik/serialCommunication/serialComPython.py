import serial
sendData = serial.Serial('COMx', 9600, timeout =.1) #COMx is used COM-Port x must be checked on PC

while True:
    data = sendData.readline()[:-2]
    if data:
        print data
