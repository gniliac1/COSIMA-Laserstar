# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:30:23 2018

@author: Daniel Wolff
"""

import sensor
import serial
from time import sleep

# Öffnen der Ports für die Photoplatte und den Sensorhandschuh
# Die COMx Ports müssen abhängig von dem verwendeten PC neu ermittelt werden
photoPort = serial.Serial('COM4', 9600, timeout = .1) 
glovePort = serial.Serial('COM8', 9600, timeout = .1)

# Ports schließen, für den Fall, dass das Programm abstürtzt
photoPort.close()
glovePort.close()

# und dann neu öffnen, um damit arbeiten zu können
photoPort.open()
glovePort.open()

# erstelle Objekt für Photoplatte
photoSensors = sensor.PhotoPlatte()

# erstelle Objekt für Sensorhandschuh
sensorGlove = sensor.Sensorhandschuh()

# eigentliche Programm-Schleife
while True
	
	####################################
	## lese Daten von der Photoplatte ##
	####################################
	
	# warten, bis sich was geändert hat (Anzahl Bytes im Input Buffer < 2)
	while photoPort.in_waiting() <= 2:
		sleep(0.1)
	
	# Auslesen der Sensordaten der Photoplatte, solange es noch Änderungen gibt
	# Annahme: newDataPhoto[0] = Sensornummer, newDataPhoto[1] = Wert
	# TODO: Gucken wie newDataPhoto aussieht
	while photoPort.in_waiting() >= 2:
		newDataPhoto = photoPort.read(2)
		photoSensors.sensorArray[newDataPhoto[0]].value = newDataPhoto[1]
		sleep(0.1) # warten bis neue Änderungen angekommen sind
	
	####################################
	## lese Daten vom Sensorhandschuh ##
	####################################
	
	# warten, bis sich was geändert hat (Anzahl Bytes im Input Buffer < 2)
	while glovePort.in_waiting() <= 2:
		sleep(0.1)
		
	# Auslesen der Sensordaten der Photoplatte, solange es noch Änderungen gibt
	# Annahme: newDataGlove[0] = Sensornummer, newDataGlove[1] = Wert
	# TODO: Gucken wie newDataGlove aussieht
	while glovePort.in_waiting() >= 2:
		# TODO: Wie viele Bytes müssen für den Sensorhandschuh gelesen werden?
		newDataGlove = glovePort.read(2)
		# TODO: Wie werden die Daten versendet?
		sleep(0.1) # warten bis neue Änderungen angekommen sind
	
	# schreibe Daten in die gewünschte Datei
	# todo ...