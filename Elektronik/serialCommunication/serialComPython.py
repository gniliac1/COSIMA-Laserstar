import serial

bt = serial.Serial('COM5', 9600, timeout = .1) #COMx is used COM-Port x must be checked on PC
mod = input('Modus? r(read), e(exit)')
print(mod)
while True:
    data = bt.readline()[:-2]
    
    if mod== 'r':
        print(data)

    if mod == 'e':
        bt.close()
                    
    else:
        print('wrong choice, closing connection')
        bt.close()
            

