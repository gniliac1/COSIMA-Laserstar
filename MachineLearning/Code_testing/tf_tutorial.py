'''
    code taken from
	    https://www.tensorflow.org/tutorials/keras/basic_classification

    This script trains a neural network model to classify images of clothing, like sneakers and shirts.
    It serves as a fast-paced overview of a complete TensorFlow program.
'''

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


########
# data #
########

'''
    load the data set with the clothing images, which is already divided into
    - a part which will be used to train the model 
    - and an additional part to test the newly created model
    
    The data consists of a bunch of grayscale images - represented as matrices - and their corresponding labels (target values).
    There are 60,000 clothing images in the training set, with each image represented as 28 x 28 pixels as well as 60,000 labels, 
    where each label is an integer between 0 and 9, corresponding to the type of clothing shonw in the associated image.
    There are 10,000 images in the test set, again, each image is represented as 28 x 28 pixels as well as 10,000 labels.
'''

print('Loading data set ...')

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# class names associated with the different numbers of the labels
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


#################
# preprocessing #
#################

'''
    The data must be preprocessed before training the network. If you inspect the first image in the training set (the lines below), 
    you will see that the pixel values fall in the range of 0 to 255. These values are scaled to a range of 0 to 1 before feeding to the neural 
	network model. For this, the datatype of the image components is casted from an integer to a float, and divided by 255.
    It's important that the training set and the testing set are preprocessed in the same way.
'''

# display the first image to show, that the pixels range from 0 to 255
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.gca().grid(False)
plt.show()

print('Preprocessing data ...')

# scale the images (the actual preprocessing step)
train_images = train_images / 255.0
test_images = test_images / 255.0

# plot the first images and the corresponding labels to check the dataset
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


###################
# build the model #
###################

'''
    The basic building block of a neural network is the layer. Layers extract representations from the data fed into them. Most of deep learning 
    consists of chaining together simple layers. Most layers, like tf.keras.layers.Dense, have parameters that are learned during training.
    The first layer in this network, tf.keras.layers.Flatten, transforms the format of the images from a 2d-array (of 28 by 28 pixels), to a 1d-array 
    of 28 * 28 = 784 pixels. This layer simply unstacks rows of pixels in the image and lines them up. This layer has no parameters to learn, since 
    it only reformats the data.
    After the pixels are flattened, the network consists of a sequence of two tf.keras.layers.Dense layers. These are densely-connected, or fully-connected,
    neural layers. The first Dense layer has 128 nodes (or neurons). The second (and last) layer is a 10-node softmax layer—this returns an array of 10 
    probability scores that sum to 1. Each node contains a score that indicates the probability that the current image belongs to one of the 10 digit classes.

    Before the model is ready for training, it needs a few more settings. These are added during the model's compile step:
    - Loss function:	This measures how accurate the model is during training. Minimizing this function "steers" the model in the right direction.
    - Optimizer: 		This is how the model is updated based on the data it sees and its loss function.
    - Metrics:			Used to monitor the training and testing steps. The example uses accuracy, the fraction of the images that are correctly classified
'''

print('Building up the model...')

# create the layers
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

# compile the model
model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


###################
# train the model #
###################

'''
    Training the neural network model requires the following steps:

    1) Feed the training data to the model—in this example, the train_images and train_labels arrays.
    2) The model learns to associate images and labels.
    3) Ask the model to make predictions about a test set — in this example, the test_images array - and verify that the predictions match the labels from the test_labels array.

'''

print('Training the model...')

# start the training
model.fit(train_images, train_labels, epochs=5)


#################################
# evaluate the model's accuracy #
#################################

'''
    It turns out, the accuracy on the test dataset is a little less than the accuracy on the training dataset. This gap between training accuracy and test accuracy is an 
    example of overfitting. Overfitting is when a machine learning model performs worse on new data than on their training data.
'''

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)


####################
# make predictions #
####################

'''
    A prediction is an array of 10 numbers. These describe the "confidence" of the model that the image corresponds to each of the 10 different articles of clothing. 
	The image will most likely belong to the label associated with the highest confidence value.
'''

print('Predicting the labels of the test data ...')

predictions = model.predict(test_images)

# Plot the first 25 test images, their predicted label, and the true label
# Color correct predictions in green, incorrect predictions in red
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions[i])
    true_label = test_labels[i]
    if predicted_label == true_label:
      color = 'green'
    else:
      color = 'red'
    plt.xlabel("{} ({})".format(class_names[predicted_label], 
                                class_names[true_label]),
                                color=color)
plt.show()
