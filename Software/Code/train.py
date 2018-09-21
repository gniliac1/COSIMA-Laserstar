########################
# function definitions #
########################

def readData( filename, trainingData = [], trainingLabels = [] ):
	"This functions reads in the data files which have been created by the recordData.py script"
	"and stores their content into two seperate lists"
	# open file for reading
	file = open(filename, "r")
	# read in all lines
	lines = file.readlines()
	# initialize some variables
	currentLine = 0
	# parse each line 
	while currentLine < len(lines):
		# read in training values, remove the '\n' of each line and split at ','
		temp = lines[currentLine][:-1].split(",")
		# convert to int and append to list of training values
		trainingData.append(list(map(int, temp)))
		# read in training labels and remove the '\n' of each line
		temp = lines[currentLine+1][:-1]
		# convert to int and append to list of training labels
		trainingLabels.append(list(map(int, temp)))
		# increment the line counter
		currentLine = currentLine + 2
	# close the file
	file.close()
	# return the read in data
	return trainingData, trainingLabels
	
def unison_shuffled_copies(a, b):
	"This functions permutes the rows of the numpy arrays a and b in the same order"
	assert len(a) == len(b)
	p = np.random.permutation(len(a))
	return a[p], b[p]

def transform( vector, ranges ):
	"This function takes a 3 dimensional vector as input and scales it such that each component only ranges from 0 to 1"
	"ranges contains the ranges of the x,y and z coordinates: ranges = [xmin, xmax, ymin, ymax, zmin, zmax]"
	assert vector.size == 3
	for i in range(3):
		vector[i] = 1.0 / (ranges[2*i+1] - ranges[2*i]) * ( vector[i] - ranges[2*i] )
	return vector

def build_model(shape):
	"Creates a sequential model with two densely connected hidden layers"
	"and an output layer that returns two continuous values"

	# activation functions
	# - tf.nn.relu
	# - tf.sigmoid
	model = keras.Sequential([
		keras.layers.Flatten(input_shape=(shape,)),
		keras.layers.Dense(128, activation=tf.nn.relu),
		keras.layers.Dense(2, activation=tf.nn.softmax)
	])

	# compile the model
	model.compile(optimizer=tf.train.AdamOptimizer(), 
				  loss='sparse_categorical_crossentropy',
				  metrics=['accuracy'])
	
	model.summary()
				
	return model

#################
# configuration #
#################

print('\nLoading libraries ...')
print('---------------------\n')
# import the TensorFlow library
import tensorflow as tf
# import the Keras API, which is a high-level API to build and train deep learning models
from tensorflow import keras

# library for using numpy arrays
import numpy as np
# library for creating plots
import matplotlib.pyplot as plt
# library for random numbers
import random as rand


########
# data #
########

print('\nLoading data ...')
print('----------------\n')

# load generated data
trainingData, trainingLabels = readData("photoData_flach.csv")
# print so that the user can see, whether everything has worked properly
print(np.shape(trainingData))
print(np.shape(trainingLabels))
# load generated data
trainingData, trainingLabels = readData("photoData_links.csv",trainingData,trainingLabels)
# print so that the user can see, whether everything has worked properly
print(np.shape(trainingData))
print(np.shape(trainingLabels))
# convert the read-in data structures into numy arrays
trainingData = np.array(trainingData)
trainingLabels = np.array(trainingLabels)
# shuffle both arrays in unison
trainingData, trainingLabels = unison_shuffled_copies(trainingData, trainingLabels)
print(trainingData.shape)
print(trainingLabels.shape)


#################
# preprocessing #
#################

print('\nPreprocessing data ...')
print('----------------------\n')

trainingData = trainingData / 1300.0
trainingLabels = trainingLabels / 1300.0


###################
# build the model #
###################

print('\nBuilding up the model...')
print('------------------------\n')
model = build_model(trainingData.shape[1])


###################
# train the model #
###################

nEpochs = 5;

print('\nTraining the model...')
print('---------------------\n')
model.fit(trainingData, trainingLabels, epochs=nEpochs)
print('\nSaving the model...')
print('-------------------\n')
model.save('model.h5')