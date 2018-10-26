# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:26:23 2018

@author: Cailing
"""

import gestiFuncs as funcs

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Aulesen der Daten könnte man noch über XML-Dateien machen
class UserModel :

	name = "MaxMustermann"
	gestureToCommand = np.array([1,2,3,4])
	
	def __init__(self, fileName = "data/test.usr"):
		userData = np.genfromtxt( fileName, dtype='str' )
		self.name = userData[0]
		# load the model
		print("Loading Model")
		#self.model = keras.models.load_model(userData[1])
		# compile the model once again
		#print("Compiling Model")
		#self.model.compile(optimizer=tf.train.AdamOptimizer(), 
		#				   loss=userData[2],
		#				   metrics=[userData[3]])
		#self.model.summary()
		self.model = funcs.create_model()
		self.model.load_weights("data/testWeights")
		print("Done")
		#if userData[4] != 'NONE':
		#	self.gestureToCommand = np.genfromtxt( userData[4], delimiter=';', dtype='int')
	
	def getControlCommand(self, PhotoPlatte):
		data = PhotoPlatte.sensorArray / 1300.0
		print("\n\n")
		print(data)
		gesture = self.model.predict(data)
		print(gesture)
		gesture = np.argmax( gesture )
		if gesture == 0:
			print("flach")
		elif gesture == 1:
			print("links")
		elif gesture == 2:
			print("rechts")
		print("\n\n")
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
	
	def saveModel(self, fileName = "data/unnamedUserModel.h5"):
		self.model.save(fileName)
            
	def trainModel(self, fileName):
		# TODO: Trainingsdaten auslesen und damit model trainieren
		return 0
	
	def saveUser(self, fileName):
		# TODO: Speichern des Nutzers
		return 0