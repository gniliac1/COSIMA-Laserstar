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


#################
# program start #
#################

# library for using numpy arrays
import numpy as np
# library for random numbers
import random as rand
# library for command line arguments
import sys

if len(sys.argv) != 3:
	print("### Wrong number of arguments! Usage:\n###\tpython generateTestData.py numberOfTrainingData numberOfTestData")
else:

	nTrain = int(sys.argv[1]);
	nTest = int(sys.argv[2]);

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
	
	# save generated data
	np.savetxt("trainingData.out", trainingData)
	np.savetxt("trainingLabels.out", trainingLabels)
	np.savetxt("testData.out", testData)
	np.savetxt("testLabels.out", testLabels)
	np.savetxt("config.out", np.array([nTrain,nTest,xmin,xmax,ymin,ymax,zmin,zmax]))