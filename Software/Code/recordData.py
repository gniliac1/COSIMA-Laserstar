# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:30:23 2018

@author: Daniel Wolff
"""

import gestiFuncs as funcs
import sensor
import serial
from time import sleep

# �ffnen der Ports f�r die Photoplatte und den Sensorhandschuh
# Die COMx Ports m�ssen abh�ngig von dem verwendeten PC neu ermittelt werden
print("Opening Serial Port COM4 ...")
photoPort = serial.Serial('COM4', 9600, timeout = .1)
print("... done")

# Ports schlie�en, f�r den Fall, dass das Programm abst�rtzt
photoPort.close()

# und dann neu �ffnen, um damit arbeiten zu k�nnen
photoPort.open()

# erstelle Objekt f�r Photoplatte
photoSensors = sensor.PhotoPlatte(nSensors = 16)

# erstelle Datei zum Speichern der Datens�tze
dataFile = open("data/test.csv","a")

print("Entering Program Loop")

try:
	# eigentliche Programm-Schleife
	while True:
		
		# clear old data
		photoPort.reset_input_buffer()
		
		####################################
		## lese Daten von der Photoplatte ##
		####################################
		
		# Auslesen der Sensordaten der Photoplatte, solange es noch �nderungen gibt
		# newDataPhoto[0] = Sensornummer, newDataPhoto[1] = Wert
		for counter in range( photoSensors.nSensors ):
			# read two integers from serial port
			newDataPhoto = funcs.readIntgersFromSerialPort(photoPort,2)
			# convert data from string to integer
			newDataPhoto = list(map(int, newDataPhoto))
			print(newDataPhoto)
			# update the value in the data structure
			photoSensors.setSensorData(newDataPhoto)
		
		# write sensor array to the specified file
		photoSensors.writeSensorData(dataFile)
		# write the target value corresponding to the current gesture
		# 1 -> flach
		# 2 -> links
		# 3 -> rechts
		dataFile.write("3\n")
		
		# zum testen, etwas warten
		print("\n\n")
		
except KeyboardInterrupt:

	dataFile.close()
	print("Closing Ports")
	photoPort.close()
	print("Done")