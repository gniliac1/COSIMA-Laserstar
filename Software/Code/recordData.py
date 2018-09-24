# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:30:23 2018

@author: Daniel Wolff
"""

def readIntgersFromSerialPort(port,nIntegers):
	# wait for valid data
	while True:
		# try to read data
		newData = port.readline()
		# if data has been received
		if newData:
			# try to decode the string
			newData = newData.decode("ascii").split(" ")
			# check whether the data is valid and consists of nIntegers integers
			if len(newData) == 2:
				# received data is valid, so leave the loop and process the data
				break
	return newData

import sensor
import serial
from time import sleep

# Öffnen der Ports für die Photoplatte und den Sensorhandschuh
# Die COMx Ports müssen abhängig von dem verwendeten PC neu ermittelt werden
print("Opening Serial Port COM4 ...")
photoPort = serial.Serial('COM4', 9600, timeout = .1)
print("... done")

# Ports schließen, für den Fall, dass das Programm abstürtzt
photoPort.close()

# und dann neu öffnen, um damit arbeiten zu können
photoPort.open()

# erstelle Objekt für Photoplatte
photoSensors = sensor.PhotoPlatte(nSensors = 16)

# erstelle Datei zum Speichern der Datensätze
dataFile = open("photoData_rechts.csv","a")

print("Entering Program Loop")

try:
	# eigentliche Programm-Schleife
	while True:
		
		# clear old data
		photoPort.reset_input_buffer()
		
		####################################
		## lese Daten von der Photoplatte ##
		####################################
		
		# Auslesen der Sensordaten der Photoplatte, solange es noch Änderungen gibt
		# newDataPhoto[0] = Sensornummer, newDataPhoto[1] = Wert
		for counter in range( photoSensors.nSensors ):
			# read two integers from serial port
			newDataPhoto = readIntgersFromSerialPort(photoPort,2)
			# convert data from string to integer
			newDataPhoto = list(map(int, newDataPhoto))
			print(newDataPhoto)
			# update the value in the data structure
			photoSensors.sensorArray[newDataPhoto[0]].value = newDataPhoto[1]
		
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