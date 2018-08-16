# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:48:19 2018

@author: Cailing

"""

import gestiFuncs as gesti
import sensor
import numpy as np
import serial

# Variablen initialisieren
oldCommand = np.array([0,0])

# Laden der User-datei zum laden der Modelle, erstellen der NutzerConfig und co
myUserModel = gesti.loadUser()

# Erstellen von Sensoren in einem array der Länge nSensoren (darin enthalten 
# sollten alle nötigen Sensoren sein wie Photodioden und Abstandssensor)
nSensoren = 10
sensorArray = np.array([])
for i in range(nSensoren):
    sensorArray = np.insert(sensorArray, sensorArray.shape[0], sensor.Sensor)

# Öffnen der Ports für die Photoplatte und das Oktoauto
# COMx is used COM-Port x must be checked on PC
photoPort = serial.Serial('COM5', 9600, timeout = .1)
photoPort.open() 
oktoPort = serial.Serial('COM8', 9600, timeout = .1)
oktoPort.open()

# TODO: Anfang Loop ---> 

# TODO: Auslesen von Sensordaten der Photoplatte vom Port, solange es noch Änderungen 
# gibt und Speichern in diejeweilige Klasse Photodiode

# Auslesen aller Sensordaten des Photodioden-Arrays
curData = np.array([])
for i in range(nSensoren):
    curData = np.insert(curData, curData.shape[0], sensorArray.getValue())

# TODO: Bereinigen der Daten, falls nötig. Der Teil muss noch geguckt werden...

# Erkennen der Geste durch die Daten und das Model des Nutzers 
# sowie zuordnung zu einem Steuerungsbefehl
newCommand = myUserModel.getCrontrolCommand(curData)

# Senden des Steuerungsbefehls an das Oktoauto 
if np.array_equal(newCommand, oldCommand) == 0:
    oktoPort.write(newCommand[0])
    oktoPort.write(newCommand[1])

oldCommand = newCommand

# <--- Ende loop