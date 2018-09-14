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
	"and an output layer that returns two continuous values"

	# activation functions
	# - tf.nn.relu
	# - tf.sigmoid
	model = keras.Sequential([
		keras.layers.Dense(128, activation=tf.nn.relu, input_shape=(shape,)),
		keras.layers.Dense(128, activation=tf.nn.relu),
		keras.layers.Dense(64, activation=tf.nn.relu),
		keras.layers.Dense(64, activation=tf.nn.relu),
		keras.layers.Dense(2)
		])

	
	optimizer = tf.train.RMSPropOptimizer(0.001)

	# loss function is 'mean square error'
	# metrics is 'mae' ('mean absolute error')
	# metrics is 'mape' ('mean absolute percentage error')
	model.compile(loss='mse', optimizer=optimizer, metrics=['mape'])
	
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
trainingData = np.loadtxt("trainingData.out")
trainingLabels = np.loadtxt("trainingLabels.out")
testData = np.loadtxt("testData.out")
testLabels = np.loadtxt("testLabels.out")
[nTrain,nTest,xmin,xmax,ymin,ymax,zmin,zmax] = np.loadtxt("config.out",dtype='int')


#################
# preprocessing #
#################

print('\nPreprocessing data ...')
print('----------------------\n')

# scale the data to the range of [0,1]
for i in range(nTrain):
	trainingData[i,] = transform(trainingData[i,], np.array([xmin,xmax,ymin,ymax,zmin,zmax]) )

print('shape of scaled training data: ',trainingData.shape)
print('scaled training data [0,] = ',trainingData[0,])
print('shape of scaled training labels: ',trainingLabels.shape)
print('scaled training label [0,] = ',trainingLabels[0,])
	
for i in range(nTest):
	testData[i,] = transform(testData[i,], np.array([xmin,xmax,ymin,ymax,zmin,zmax]) )

print('shape of scaled test data: ',testData.shape)
print('scaled test data [0,] = ',testData[0,])
print('shape of scaled test labels: ',testLabels.shape)
print('scaled test label [0,] = ',testLabels[0,])


###################
# build the model #
###################

print('Building up the model...')
combinedModel = build_model(trainingData.shape[1])


###################
# train the model #
###################

nEpochs = 500;

print('Training the model...')
combinedModel.fit(trainingData, trainingLabels, epochs=nEpochs)
print('Saving the model...')
combinedModel.save('combinedModel.h5')


#################################
# evaluate the model's accuracy #
#################################

print('\nAccuracy of the models ...')
print('--------------------------\n')

loss, mape = combinedModel.evaluate(testData, testLabels)
print('Accuracy of the model:')
print('- loss function value:',loss)
print('- mean absolute percentage error:',mape)


####################
# make predictions #
####################

print('\nPredicting some labels of the test data ...')
print('-------------------------------------------\n')

prediction = combinedModel.predict( testData )

for i in range(5):
	print('Data point:',testData[i,])
	print('Target value:',testLabels[i,])
	print('Prediction:',prediction[i,])
	print('-------------------------------------------\n')