
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


from tensorflow import keras


# In[3]:


import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


fashion_mnist = keras.datasets.fashion_mnist


# In[6]:


(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# In[7]:


print(tf.__version__)


# In[8]:


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# In[9]:


train_images.shape


# In[10]:


plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.gca().grid(False)

