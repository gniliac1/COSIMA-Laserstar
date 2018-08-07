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
	# metrics is 'mae' ('mean absolute error')
	# metrics is 'mape' ('mean absolute percentage error')
	model.compile(loss='mse',optimizer=optimizer,metrics=['mape'])
	
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

print('\nCreating data ...')
print('-----------------\n')

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
trainingData = np.zeros((nTrain, 3))
trainingLabels = np.zeros((nTrain, 2))
for i in range(nTrain):
	# generate random points
	currentX = rand.uniform(xmin,xmax)
	currentY = rand.uniform(ymin,ymax)
	currentZ = rand.uniform(zmin,zmax)
	currentData = np.array( [currentX, currentY, currentZ] )
	trainingData[i,] = currentData
	# create the corresponding label
	currentLabel = eval( currentData )
	trainingLabels[i,] = currentLabel 
	
print("shape of training data: ",trainingData.shape)
print("training data [0,] = ",trainingData[0,])
print("shape of training labels: ",trainingLabels.shape)
print("training label [0,] = ",trainingLabels[0,])

# create the test data
testData = np.zeros((nTest, 3))
testLabels = np.zeros((nTest, 2))
for i in range(nTest):
	# generate random points
	currentX = rand.uniform(xmin,xmax)
	currentY = rand.uniform(ymin,ymax)
	currentZ = rand.uniform(zmin,zmax)
	currentData = np.array( [currentX, currentY, currentZ] )
	testData[i,] = currentData
	# create the corresponding label
	currentLabel = eval( currentData )
	testLabels[i,] = currentLabel
	
print("shape of test data: ",testData.shape)
print("test data [0,] = ",testData[0,])
print("shape of test labels: ",testLabels.shape)
print("test label [0,] = ",testLabels[0,])


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

print('Building up the model for the first output...')
firstComponentModel = build_model(trainingData.shape[1])
print('Building up the model for the second output...')
secondComponentModel = build_model(trainingData.shape[1])


###################
# train the model #
###################

nEpochs = 500;

print('Training the model for the first output...')
firstComponentModel.fit(trainingData, trainingLabels[:,0], epochs=nEpochs)
print('Saving the model for the first output...')
firstComponentModel.save('firstComponentModel.h5')

print('Training the model for the second output...')
secondComponentModel.fit(trainingData, trainingLabels[:,1], epochs=nEpochs)
print('Saving the model for the second output...')
secondComponentModel.save('secondComponentModel.h5')


#################################
# evaluate the model's accuracy #
#################################

print('\nAccuracy of the models ...')
print('--------------------------\n')

first_loss, first_mae = firstComponentModel.evaluate(testData, testLabels[:,0])
print('Accuracy of the model of the first output:')
print('- loss function value:',first_loss)
print('- mean absolute error:',first_mae)

second_loss, second_mae = secondComponentModel.evaluate(testData, testLabels[:,1])
print('Accuracy of the model of the second output:')
print('- loss function value:',second_loss)
print('- mean absolute error:',second_mae)


####################
# make predictions #
####################

print('\nPredicting some labels of the test data ...')
print('-------------------------------------------\n')

FirstComponentPrediction = firstComponentModel.predict( testData )
SecondComponentPrediction = secondComponentModel.predict( testData )

for i in range(5):
	print('Data point:',testData[i,])
	print('Target value:',testLabels[i,])
	print('Prediction:',[FirstComponentPrediction[i,0],SecondComponentPrediction[i,0]])
	print('-------------------------------------------\n')