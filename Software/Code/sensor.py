# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 12:57:11 2018

@author: Cailing
"""

import numpy as np

class Sensor:
    value = -1
    minValue = 0
    maxValue = 255
    
    def __init__(self, value=0):
        self.value = value
    
    # Wert zwischen 0 und 1 
    def getValue(self):
        return (self.value - self.minValue) / (self.maxValue - self.minValue)
    
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


class PhotoPlatte:

	nSensors = 1	# wie viele Sensoren?
	
	def __init__(self, nSensors = 16):
		self.nSensors = nSensors
		self.sensorArray = np.zeros([1,nSensors], dtype = "int")
			
	def writeSensorData(self, file):
		# iterate over all sensors and write their current values to a string
		arrayString = ""
		for i in range(self.nSensors):
			arrayString = arrayString + str(self.sensorArray[0,i])
			if i != self.nSensors-1:
				arrayString = arrayString + ","
		# write the arrayString to the file
		file.write(arrayString + "\n")
		
	def setSensorData(self, data):
		self.sensorArray[0,data[0]] = data[1]


class SensorHandschuh:

	nSensors = 4 		# wie viele verschiedene Arten von Sensoren -> 4
	nCompass = 3 		# 3 Werte vom Kompass
	nAccelerometer = 3	# 3 Werte von Beschleunigungssensoren
	nGyroscope = 3 		# 3 Werte vom Gyroskop
	nBendingSensors = 5 # 5 Werte von Biegesensoren

	def __init__(self):
		# 3 Werte vom Kompass
		self.compass = np.zeros([1,self.nCompass], dtype = "int")
		# 3 Werte von Beschleunigungssensoren
		self.accelerometer = np.zeros([1,self.nAccelerometer], dtype = "int")
		# 3 Werte vom Gyroskop
		self.gyroscope = np.zeros([1,self.nGyroscope], dtype = "int")
		# 5 Werte von Biegesensoren
		self.bendingSensors = np.zeros([1,self.nBendingSensors], dtype = "int")
	
	def writeSensorData(self, file):
		# write compass data
		arrayString = ""
		for i in range(self.nCompass):
			arrayString = arrayString + str(self.compass[0,i])
			if i != self.nCompass-1:
				arrayString = arrayString + ","
		# write the arrayString to the file
		file.write(arrayString + "\n")
		# write accelerometer data
		arrayString = ""
		for i in range(self.nAccelerometer):
			arrayString = arrayString + str(self.accelerometer[0,i])
			if i != self.nAccelerometer-1:
				arrayString = arrayString + ","
		# write the arrayString to the file
		file.write(arrayString + "\n")
		# write gyroscope data
		arrayString = ""
		for i in range(self.nGyroscope):
			arrayString = arrayString + str(self.gyroscope[0,i])
			if i != self.nGyroscope-1:
				arrayString = arrayString + ","
		# write the arrayString to the file
		file.write(arrayString + "\n")
		# write bending sensor data
		arrayString = ""
		for i in range(self.nBendingSensors):
			arrayString = arrayString + str(self.bendingSensors[0,i])
			if i != self.nBendingSensors-1:
				arrayString = arrayString + ","
		# write the arrayString to the file
		file.write(arrayString + "\n")
		
	def setSensorData(self,data):
		# first entry of the data array corresponds to the sensor type
		# data[0] == 0 -> compass, 3 values
		# data[0] == 1 -> accelerometer, 3 values
		# data[0] == 2 -> gyroscope, 3 values
		# data[0] == 3 -> bending sensor, 5 values
		if data[0] == 0:
			# set compass data
			for i in range(self.nCompass):
				self.compass[0,i] = data[i+1]
		elif data[0] == 1:
			# set accelerometer data
			for i in range(self.nAccelerometer):
				self.accelerometer[0,i] = data[i+1]
		elif data[0] == 2:
			# set gyroscope data
			for i in range(self.nGyroscope):
				self.gyroscope[0,i] = data[i+1]
		elif data[0] == 3:
			# set bending sensor data
			for i in range(self.nBendingSensors):
				self.bendingSensors[0,i] = data[i+1]
			

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