########################
# function definitions #
########################

def eval( x ):
	"This function evaluates a mapping from R3 to R2 at the point specified by x"
	assert x.size == 3
	y = np.zeros(2)
	y[0] = x[0] * x[1] * x[2]
	y[1] = x[1]*x[2] + x[0]*x[2] + x[0]*x[1]
	return y

def transform( vector, ranges ):
	"This function takes a 3 dimensional vector as input and scales it such that each component only ranges from 0 to 1"
	"ranges contains the ranges of the x,y and z coordinates: ranges = [xmin, xmax, ymin, ymax, zmin, zmax]"
	assert vector.size == 3
	for i in range(3):
		vector[i] = 1.0 / (ranges[2*i+1] - ranges[2*i]) * ( vector[i] - ranges[2*i] )
	return vector

def build_model(shape):
	"Creates a sequential model with two densely connected hidden layers"
	"and an output layer that returns a single, continuous value"

	model = keras.Sequential([
		keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(shape,)),
		keras.layers.Dense(64, activation=tf.nn.relu),
		keras.layers.Dense(1)
		])

	
	optimizer = tf.train.RMSPropOptimizer(0.001)

	# loss function is 'mean square error'
	# metrics is 'mean absolute error'
	model.compile(loss='mse',optimizer=optimizer,metrics=['mae'])
	
	model.summary()
				
	return model

#################
# configuration #
#################

print('Loading libraries ...')
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

print('Creating data ...')

# number of points for training and testing
nTrain = 10000;
nTest = 1000;

# set ranges for the x, y and z coordinates
xmin = -5.0;
xmax = 5.0;
ymin = -0.5;
ymax = 6.0;
zmin = -3.5;
zmax = 2.0;

# create the training data
trainingData = []
trainingLabels = np.zeros((nTrain, 2))
for i in range(nTrain):
	# generate random points
	currentX = rand.uniform(xmin,xmax)
	currentY = rand.uniform(ymin,ymax)
	currentZ = rand.uniform(zmin,zmax)
	currentData = np.array( [currentX, currentY, currentZ] )
	trainingData.append( currentData )
	# create the corresponding label
	currentLabel = eval( currentData )
	trainingLabels[i,] = currentLabel 
	
print("training data [0] = ",trainingData[0])
print("training label [0] = ",trainingLabels[0])

# create the test data
testData = []
testLabels = np.zeros((nTest, 2))
for i in range(nTest):
	# generate random points
	currentX = rand.uniform(xmin,xmax)
	currentY = rand.uniform(ymin,ymax)
	currentZ = rand.uniform(zmin,zmax)
	currentData = np.array( [currentX, currentY, currentZ] )
	testData.append( currentData )
	# create the corresponding label
	currentLabel = eval( currentData )
	testLabels[i,] = currentLabel


#################
# preprocessing #
#################

print('Preprocessing data ...')

# scale the data to the range of [0,1]
for i in range(nTrain):
	trainingData[i] = transform(trainingData[i], np.array([xmin,xmax,ymin,ymax,zmin,zmax]) )

for i in range(nTest):
	testData[i] = transform(testData[i], np.array([xmin,xmax,ymin,ymax,zmin,zmax]) )
	
print("scaled training data [0] = ",trainingData[0])
print("scaled training label [0] = ",trainingLabels[0])


###################
# build the model #
###################

# to be continued