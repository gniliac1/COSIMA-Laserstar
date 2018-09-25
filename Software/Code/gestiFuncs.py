# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:06:09 2018

@author: Cailing
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras

def create_model():
	"Creates a sequential model with two densely connected hidden layers"
	"and an output layer that returns two continuous values"

	# activation functions
	# - tf.nn.relu
	# - tf.sigmoid
	model = keras.Sequential([
		keras.layers.Flatten(input_shape=(16,)),
		keras.layers.Dense(8, activation=tf.nn.relu),
		keras.layers.Dense(8, activation=tf.nn.relu),
		keras.layers.Dense(3, activation=tf.nn.softmax)
	])

	# compile the model
	model.compile(optimizer=tf.train.AdamOptimizer(), 
				  loss='sparse_categorical_crossentropy',
				  metrics=['accuracy'])
	
	model.summary()
				
	return model
	
def readIntgersFromSerialPort(port,nIntegers):
	"This function reads in a message consisting of nIntegers integer data from a specified serial port"
	# wait for valid data
	while True:
		# try to read data
		newData = port.readline()
		# if data has been received
		if newData:
			# try to decode the string
			newData = newData.decode("ascii").split(" ")
			# check whether the data is valid and consists of nIntegers integers
			if len(newData) == nIntegers:
				# received data is valid, so leave the loop and process the data
				break
	return newData

def unison_shuffled_copies(a, b):
	"This functions permutes the rows of the numpy arrays a and b in the same order"
	assert len(a) == len(b)
	p = np.random.permutation(len(a))
	return a[p], b[p]