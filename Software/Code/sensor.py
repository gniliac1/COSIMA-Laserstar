# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 12:57:11 2018

@author: Cailing
"""

class Sensor:
    value = -1
    minValue = 0
    maxValue = 255
    
    def __init__(self, value=0):
        self.value = value
    
    # Wert zwischen 0 und 1 
    def getValue(self):
        return self.value / (self.maxValue - self.minValue)
    
    # Wert zwischen minValue und maxValue :) Immer :) 
    def setValue(self, newValue):
        if newValue < self.minValue:
            self.value = self.minValue
        elif newValue > self.maxValue:
            self.value = self.maxValue
        else:
            self.value = newValue
    
    # MinValue muss mindestens 1 kleiner als MaxValue sein        
    def setMinValue(self, newMin):
        if newMin > self.maxValue:
            self.minValue = self.maxValue - 1
        else:
            self.minValue = newMin
            
    # MaxValue muss mindestens 1 größer als MinValue sein        
    def setMaxValue(self, newMax):
        if newMax < self.minValue:
            self.maxValue = self.minValue + 1
        else:
            self.maxValue = newMax
    
""" Falls nötig

class Photodiode(Sensor) :
    def __init__(self, value, minValue, maxValue):
        Sensor.__init__(self, value)
        self.maxValue = maxValue;
        self.minValue = minValue;

class DistanceSensor(Sensor) : 
    def __init__(self, value, minValue, maxValue):
        Sensor.__init__(self, value)
        self.maxValue = maxValue;
        self.minValue = minValue;
        
"""