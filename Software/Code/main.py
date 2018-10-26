# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:48:19 2018

@author: Cailing

"""

# custom packages
import gestiFuncs as funcs
import sensor
import userModel

# predefined packages
import numpy as np
import serial
from time import sleep

print("\n\nInitializing\n\n")

# Variablen initialisieren
oldCommand = np.array([0,0])

# Laden der User-datei zum laden der Modelle, erstellen der NutzerConfig und co
myUserModel = userModel.UserModel("data/test.usr")

# Erstellen von Sensoren in einem array der Länge nSensoren (darin enthalten 
# sollten alle nötigen Sensoren sein wie Photodioden und Abstandssensor)
nSensoren = 16
photoSensors = sensor.PhotoPlatte(nSensors = nSensoren)

# Öffnen der Ports für die Photoplatte und das Oktoauto
# COMx is used COM-Port x must be checked on PC
photoPort = serial.Serial('COM4', 9600, timeout = .1) # Die COM - Ports sind auf meinem Laptop gemappt. Wenn ein anderer PC genutzt wird -> COM-Ports checkst!
#oktoPort = serial.Serial('COM6', 9600, timeout = .1)

photoPort.close()
#oktoPort.close() #Es ist immer besser zuerst den port zu schließen (für den Fall das, dass Prog. abgestürzt ist der Port ist dann noch offen und lässt sich nicht benutzen)
                  #und dann den Port neu zu öffnen.

photoPort.open()
#oktoPort.open()

print("\n\nStarting Program Loop\n\n")

try:
	# program loop
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
			newDataPhoto = funcs.readIntgersFromSerialPort(photoPort,2)
			# convert data from string to integer
			newDataPhoto = list(map(int, newDataPhoto))
			print(newDataPhoto)
			# update the value in the data structure
			photoSensors.setSensorData(newDataPhoto)

		# TODO: Bereinigen der Daten, falls nötig. Der Teil muss noch geguckt werden...

		# Erkennen der Geste durch die Daten und das Model des Nutzers 
		# sowie zuordnung zu einem Steuerungsbefehl
		newCommand = myUserModel.getControlCommand(photoSensors)

		# Senden des Steuerungsbefehls an das Oktoauto 
		#if np.array_equal(newCommand, oldCommand) == 0:
		#	oktoPort.write(newCommand[0])
		#	oktoPort.write(newCommand[1])

		oldCommand = newCommand
		
except KeyboardInterrupt:

	print("Closing Ports")
	photoPort.close()
	#oktoPort.close()
	print("Done")