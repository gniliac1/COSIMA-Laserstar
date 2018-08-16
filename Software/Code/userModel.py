# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:26:23 2018

@author: Cailing
"""
from tensorflow import keras
import numpy as np

# Aulesen der Daten könnte man noch über XML-Dateien machen
class UserModel :
    gestureToCommand = np.array([1,2,3,4])
    modus = 0 # 0 = sitting, 1 = upright
    def __init__(self, fileName):
        userData = np.genfromtxt( fileName, dtype='str' )
        self.name = userData[0]
        self.sitModel = keras.models.load_model(userData[1])
        self.upModel = keras.models.load_model(userData[2])
        if userData[3] != 'NONE':
            self.gestureToCommand = np.genfromtxt( userData[3], delimiter=';', dtype='int')
            
    def getCrontrolCommand(self, array):
        # TODO: Array in Model auswerten
        # TODO: Geste-Commando zuordnen
        # TODO: Commando zurückgeben
        return 0
        
    # Setzt Liste der Zuordnung Geste-Commando neu
    def setCommandList(self, array):
        self.gestureToCommand = array;
        
    # Gibt die Liste der Zuordnung Geste-Commando zurück
    def getCommandList(self):
        return self.gestureToCommand
    
    def getGestureList(self):
        # TODO: Liste der labels zurück geben
        return 0
        
    def saveModel(self, fileName = '../data/unnamedUserModel.h5'):
        if self.modus == 0:
            self.sitModel.save(fileName)
            
        if self.modus == 1:
            self.upModel.save(fileName)
            
    def trainModel(self, fileName):
        # TODO: Trainingsdaten auslesen und damit sitModel oder upModel trainieren
        return 0
        
    def saveUser(self, fileName):
        # TODO: Speichern des Nutzers
        return 0