# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:30:23 2018

@author: Daniel Wolff
"""

import sensor
import serial
from time import sleep

# �ffnen der Ports f�r die Photoplatte und den Sensorhandschuh
# Die COMx Ports m�ssen abh�ngig von dem verwendeten PC neu ermittelt werden
print("Opening Serial Port COM4 ...")
photoPort = serial.Serial('COM4', 9600, timeout = .1)
print("... done")
print("Opening Serial Port COM6 ...")
glovePort = serial.Serial('COM6', 9600, timeout = .1)
print("... done")

# Ports schlie�en, f�r den Fall, dass das Programm abst�rtzt
photoPort.close()
glovePort.close()

# und dann neu �ffnen, um damit arbeiten zu k�nnen
photoPort.open()
glovePort.open()

# erstelle Objekt f�r Photoplatte
photoSensors = sensor.PhotoPlatte(nSensors = 16)

# erstelle Objekt f�r Sensorhandschuh
sensorGlove = sensor.SensorHandschuh()

print("Entering Program Loop")

try:
	# eigentliche Programm-Schleife
	while True:
		
		# clear old data
		photoPort.reset_input_buffer()
		glovePort.reset_input_buffer()
		
		####################################
		## lese Daten von der Photoplatte ##
		####################################
		
		# # warten, bis sich was ge�ndert hat (Anzahl Bytes im Input Buffer < 2)
		while photoPort.in_waiting <= 2:
			sleep(0.1)
		
		# Auslesen der Sensordaten der Photoplatte, solange es noch �nderungen gibt
		# newDataPhoto[0] = Sensornummer, newDataPhoto[1] = Wert
		for counter in range( photoSensors.nSensors ):
			while photoPort.in_waiting <= 2:
				sleep(0.1)
			# read in data and convert to integer
			newDataPhoto = photoPort.readline().decode("ascii").split(" ")
			newDataPhoto = list(map(int, newDataPhoto))
			# update the value in the data structure
			#photoSensors.sensorArray[newDataPhoto[0]].value = newDataPhoto[1]
			print(newDataPhoto)
			sleep(0.0) # warten bis neue �nderungen angekommen sind
		
		####################################
		## lese Daten vom Sensorhandschuh ##
		####################################
		
		# schicke Anfrage 
		glovePort.write('a'.encode('utf-8'))
		
		# warten, bis sich was ge�ndert hat (Anzahl Bytes im Input Buffer < 2)
		while glovePort.in_waiting <= 2:
			sleep(0.1)
			
		# Auslesen der Sensordaten der Photoplatte, solange es noch �nderungen gibt
		# newDataGlove[0] = Sensornummer, newDataGlove[1:3/5] = Wert
		# newDataGlove[0] == 0 -> compass, 3 Werte
		# newDataGlove[0] == 1 -> accelerometer, 3 Werte
		# newDataGlove[0] == 2 -> gyroscope, 3 Werte
		# newDataGlove[0] == 3 -> bending sensor, 5 Werte
		for counter in range( sensorGlove.nSensors ):
			while glovePort.in_waiting <= 2:
				sleep(0.1)
			# read in data and convert to integer
			newDataGlove = glovePort.readline().decode("ascii").split(" ")
			newDataGlove = list(map(int, newDataGlove))
			print(newDataGlove)
			sleep(0.0) # warten bis neue �nderungen angekommen sind
		
		# schreibe Daten in die gew�nschte Datei
		# todo ...
		
		# zum testen, etwas warten
		print("\n\n")
		sleep(1)
		
except KeyboardInterrupt:

	print("Closing Ports")
	photoPort.close()
	glovePort.close()
	print("Done")