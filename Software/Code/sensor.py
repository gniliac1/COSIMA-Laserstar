# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 12:57:11 2018

@author: Cailing
"""

class Sensor :
    value = -1
    minValue = 0
    maxValue = 255
    
    def __init__(self, value=0) :
        self.value = value
    
    # Wert zwischen 0 und 1 
    def getValue(self):
        return self.value / (self.maxValue - self.minValue)
  
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