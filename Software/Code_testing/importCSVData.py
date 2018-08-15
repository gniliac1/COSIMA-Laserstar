
# coding: utf-8

# # Read from .csv data and store in a matrix/tensor

# In[1]:


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


# In[18]:


a = np.genfromtxt('../data/TestDatabase.csv', delimiter=';',skip_header=1)


# In[19]:


a


# In[20]:


a.shape


# In[21]:


a_reshaped = a.reshape(a.shape[0],2,3)


# In[22]:


a_reshaped.shape


# In[23]:


a_reshaped

