import numpy as np
import matplotlib.pyplot as plt
import os

# to make DLIPR available put 'software community/dlipr' in your ~/.profile
import dlipr


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical
#from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier

# ----------------------------------------------
# Data
# ----------------------------------------------
data = dlipr.mnist.load_data()

# plot some examples
data.plot_examples(fname='examples.png')

# reshape the image matrices to vectors
X_train = data.train_images.reshape(-1, 28**2)
X_test = data.test_images.reshape(-1, 28**2)
print('%i training samples' % X_train.shape[0])
print('%i test samples' % X_test.shape[0])

# convert integer RGB values (0-255) to float values (0-1)
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

# convert class labels to one-hot encodings
Y_train = to_categorical(data.train_labels, 10)
Y_test = to_categorical(data.test_labels, 10)


# ----------------------------------------------
# Model and training
# ----------------------------------------------

batch_size_ = [100, 1000, 2000, 5000] #np.array([10, 100, 1000, 10000]) *100
epochs_ = [2, 4, 6] #[5, 10, 50, 100, 500]
val_loss=[]
val_acc=[]
acc = []


# make output directory
folder = 'results/'
if not os.path.exists(folder):
    os.makedirs(folder)

for i in range(len(batch_size_)):
    for j in range(len(epochs_)):
        model = Sequential([
            Dense(64, input_shape=(784,)),
            Activation('relu'),
            Dropout(0.5),
            Dense(10),
            Activation('softmax')])
        
        print(model.summary())
        
        model.compile(
            loss='categorical_crossentropy',
            optimizer=Adam(lr=1e-3),
            metrics=['accuracy'])
        
        fit = model.fit(
            X_train, Y_train,
            batch_size=batch_size_[i],
            epochs=epochs_[j],
            verbose=2,
            validation_split=0.1,  # split off 10% training data for validation
            callbacks=[])
        acc.append(np.array([epochs_[j], batch_size_[i], fit.history["acc"][-1]]))
        val_loss.append(np.array([epochs_[j], batch_size_[i], fit.history["val_loss"][-1]]))
        val_acc.append(np.array([epochs_[j], batch_size_[i], fit.history["val_acc"][-1]]))
        
        
val_acc = np.array(val_acc)   
val_loss = np.array(val_loss)
print (val_acc)
print (val_loss)
"""
for j in range(len(epochs_):
    for i in range(len(batch_size_)):
        Valacc[i,j] = val_acc[
"""



# ----------------------------------------------
# Some plots
# ----------------------------------------------

# predicted probabilities for the test set
Yp = model.predict(X_test)
yp = np.argmax(Yp, axis=1)

# plot some test images along with the prediction
for i in range(20):
    dlipr.utils.plot_prediction(
        Yp[i],
        data.test_images[i],
        data.test_labels[i],
        data.classes,
        fname=folder + 'test-%i.png' % i)

# plot the confusion matrix
dlipr.utils.plot_confusion(yp, data.test_labels, data.classes,
                           fname=folder + 'confusion.png')
