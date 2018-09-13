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
photoPort = serial.Serial('COM4', 9600, timeout = .1) 
glovePort = serial.Serial('COM8', 9600, timeout = .1)

# Ports schlie�en, f�r den Fall, dass das Programm abst�rtzt
photoPort.close()
glovePort.close()

# und dann neu �ffnen, um damit arbeiten zu k�nnen
photoPort.open()
glovePort.open()

# erstelle Objekt f�r Photoplatte
photoSensors = sensor.PhotoPlatte()

# erstelle Objekt f�r Sensorhandschuh
sensorGlove = sensor.Sensorhandschuh()

# eigentliche Programm-Schleife
while True
	
	####################################
	## lese Daten von der Photoplatte ##
	####################################
	
	# warten, bis sich was ge�ndert hat (Anzahl Bytes im Input Buffer < 2)
	while photoPort.in_waiting() <= 2:
		sleep(0.1)
	
	# Auslesen der Sensordaten der Photoplatte, solange es noch �nderungen gibt
	# Annahme: newDataPhoto[0] = Sensornummer, newDataPhoto[1] = Wert
	# TODO: Gucken wie newDataPhoto aussieht
	while photoPort.in_waiting() >= 2:
		newDataPhoto = photoPort.read(2)
		photoSensors.sensorArray[newDataPhoto[0]].value = newDataPhoto[1]
		sleep(0.1) # warten bis neue �nderungen angekommen sind
	
	####################################
	## lese Daten vom Sensorhandschuh ##
	####################################
	
	# warten, bis sich was ge�ndert hat (Anzahl Bytes im Input Buffer < 2)
	while glovePort.in_waiting() <= 2:
		sleep(0.1)
		
	# Auslesen der Sensordaten der Photoplatte, solange es noch �nderungen gibt
	# Annahme: newDataGlove[0] = Sensornummer, newDataGlove[1] = Wert
	# TODO: Gucken wie newDataGlove aussieht
	while glovePort.in_waiting() >= 2:
		# TODO: Wie viele Bytes m�ssen f�r den Sensorhandschuh gelesen werden?
		newDataGlove = glovePort.read(2)
		# TODO: Wie werden die Daten versendet?
		sleep(0.1) # warten bis neue �nderungen angekommen sind
	
	# schreibe Daten in die gew�nschte Datei
	# todo ...