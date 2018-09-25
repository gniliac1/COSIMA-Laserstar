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
	

#################
# configuration #
#################

print('\nLoading libraries ...')
print('---------------------\n')

# import custom functions
import gestiFuncs as funcs

# library for using numpy arrays
import numpy as np


########
# data #
########

print('\nLoading data ...')
print('----------------\n')

# load generated data
trainingDataFlach, trainingLabelsFlach = readData("data/flach_neu.csv",[],[])
# print so that the user can see, whether everything has worked properly
print(np.shape(trainingDataFlach))
print(np.shape(trainingLabelsFlach))
# load generated data
trainingDataLinks, trainingLabelsLinks = readData("data/links_neu.csv",[],[])
# print so that the user can see, whether everything has worked properly
print(np.shape(trainingDataLinks))
print(np.shape(trainingLabelsLinks))
# load generated data
trainingDataRechts, trainingLabelsRechts = readData("data/rechts_neu.csv",[],[])
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
trainingData, trainingLabels = funcs.unison_shuffled_copies(trainingData, trainingLabels)

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
testData, testLabels = funcs.unison_shuffled_copies(testData, testLabels)

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
model = funcs.create_model()


###################
# train the model #
###################

nEpochs = 25;

print('\nTraining the model...')
print('---------------------\n')
model.fit(trainingData, trainingLabels, batch_size=5, epochs=nEpochs, validation_split=0.1)

print('\nSaving the model...')
print('-------------------\n')
model.save('data/model.h5')

#################################
# evaluate the model's accuracy #
#################################

print('\nEvaluating the model...')
print('-----------------------\n')

test_loss, test_acc = model.evaluate(testData, testLabels)

print('Test loss:', test_loss)
print('Test accuracy:', test_acc)

#############

print("\n\n")
#print(trainingData[234])
bla = model.predict(np.reshape(trainingData[234],[1,16]))
print(bla)
print(trainingLabels[234])
print("\n\n")
#print(testData[25])
bla = model.predict(np.reshape(testData[25],[1,16]))
print(bla)
print(testLabels[25])
print("\n\n")

model.save_weights("data/testWeights")

model = funcs.create_model()
#print(trainingData[234])
bla = model.predict(np.reshape(trainingData[234],[1,16]))
print(bla)
print(trainingLabels[234])
print("\n\n")
#print(testData[25])
bla = model.predict(np.reshape(testData[25],[1,16]))
print(bla)
print(testLabels[25])
print("\n\n")

model.load_weights("data/testWeights")
#print(trainingData[234])
bla = model.predict(np.reshape(trainingData[234],[1,16]))
print(bla)
print(trainingLabels[234])
print("\n\n")
#print(testData[25])
bla = model.predict(np.reshape(testData[25],[1,16]))
print(bla)
print(testLabels[25])
print("\n\n")
