# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:17:44 2018

@author: chris
"""

import serial
bt = serial.Serial('COM5', 9600, timeout =.1) #COMx is used COM-Port x must be checked on PC


while True:
    for i in range(0, 10000):
        data = bt.readline()[:-2]
        if data:
            print (data)
        i += i
    bt.close()
    