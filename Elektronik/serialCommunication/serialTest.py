# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:17:44 2018

@author: chris
"""

import serial
bt = serial.Serial('COM5', 9600, timeout =.1) #COMx is used COM-Port x must be checked on PC

<<<<<<< HEAD

while True:
    for i in range(0, 10000):
        data = bt.readline()[:-2]
        if data:
            print (data)
        i += i
    bt.close()
    
=======
while data:
    data = bt.readline()[:-2]
    if data:
        print (data)
        
if !data:
    bt.close()
>>>>>>> abe6c11f4281c5e0e461aa7597f71556b6b7a2c3
