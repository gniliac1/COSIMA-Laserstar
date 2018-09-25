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

def build_model():
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


########
# data #
########

print('\nLoading data ...')
print('----------------\n')

# load generated data
trainingDataFlach, trainingLabelsFlach = readData("photoData_flach.csv",[],[])
# print so that the user can see, whether everything has worked properly
print(np.shape(trainingDataFlach))
print(np.shape(trainingLabelsFlach))
# load generated data
trainingDataLinks, trainingLabelsLinks = readData("photoData_links.csv",[],[])
# print so that the user can see, whether everything has worked properly
print(np.shape(trainingDataLinks))
print(np.shape(trainingLabelsLinks))
# load generated data
trainingDataRechts, trainingLabelsRechts = readData("photoData_rechts.csv",[],[])
# print so that the user can see, whether everything has worked properly
print(np.shape(trainingDataRechts))
print(np.shape(trainingLabelsRechts))

# all data sets have different lengths, determine the minimum
minLen = min( [len(trainingDataFlach) , len(trainingDataLinks) , len(trainingDataRechts)] )
print(minLen)
# compute the number of trainings data points per data set
numTrainData = round( 0.9 * minLen )
print(numTrainData)

# combine the training data set into numpy arrays
trainingData = np.array( trainingDataFlach[0:numTrainData][:] )
print(trainingData.shape)
trainingData = np.vstack( ( trainingData , np.array(trainingDataLinks[0:numTrainData][:]) ) )
print(trainingData.shape)
trainingData = np.vstack( ( trainingData , np.array(trainingDataRechts[0:numTrainData][:]) ) )
print(trainingData.shape)
# combine the training labels
trainingLabels = np.array( trainingLabelsFlach[0:numTrainData] )
print(trainingLabels.shape)
trainingLabels = np.vstack( ( trainingLabels , np.array(trainingLabelsLinks[0:numTrainData]) ) )
print(trainingLabels.shape)
trainingLabels = np.vstack( ( trainingLabels , np.array(trainingLabelsRechts[0:numTrainData]) ) )
print(trainingLabels.shape)

# shuffle both arrays in unison (this could maybe change something...?)
trainingData, trainingLabels = unison_shuffled_copies(trainingData, trainingLabels)

print(trainingData.shape)
print(trainingLabels.shape)


# combine the test data set into numpy arrays
testData = np.array( trainingDataFlach[numTrainData:minLen][:] )
print(testData.shape)
testData = np.vstack( ( testData , np.array(trainingDataLinks[numTrainData:minLen][:]) ) )
print(testData.shape)
testData = np.vstack( ( testData , np.array(trainingDataRechts[numTrainData:minLen][:]) ) )
print(testData.shape)
# combine the test labels
testLabels = np.array( trainingLabelsFlach[numTrainData:minLen] )
print(testLabels.shape)
testLabels = np.vstack( ( testLabels , np.array(trainingLabelsLinks[numTrainData:minLen]) ) )
print(testLabels.shape)
testLabels = np.vstack( ( testLabels , np.array(trainingLabelsRechts[numTrainData:minLen]) ) )
print(testLabels.shape)

# shuffle both arrays in unison (this should actually change nothing...!)
testData, testLabels = unison_shuffled_copies(testData, testLabels)

print(testData.shape)
print(testLabels.shape)


#################
# preprocessing #
#################

print('\nPreprocessing data ...')
print('----------------------\n')

trainingData = trainingData / 1300.0
trainingLabels = trainingLabels - 1
testData = testData / 1300.0
testLabels = testLabels - 1


###################
# build the model #
###################

print('\nBuilding up the model...')
print('------------------------\n')
model = build_model()


###################
# train the model #
###################

nEpochs = 25;

print('\nTraining the model...')
print('---------------------\n')
model.fit(trainingData, trainingLabels, batch_size=5, epochs=nEpochs, validation_split=0.1)

print('\nSaving the model...')
print('-------------------\n')
model.save('train/model.h5')

#################################
# evaluate the model's accuracy #
#################################

print('\nEvaluating the model...')
print('-----------------------\n')

test_loss, test_acc = model.evaluate(testData, testLabels)

print('Test loss:', test_loss)
print('Test accuracy:', test_acc)