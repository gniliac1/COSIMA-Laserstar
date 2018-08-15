
# coding: utf-8

# # Store data in a matrix and write in a .csv file 
# -> 10% testdata and 90% traindata

# In[90]:


import numpy as np


# In[91]:


a = np.zeros((1,9))


# In[92]:


a


# In[93]:


for i in range(1,30):
    a = np.insert(a, a.shape[0], [i,i,i,i,i,i,i,i,i], 0)


# In[94]:


a


# In[96]:


a.shape


# In[115]:


testCount = round(a.shape[0]/10)


# In[116]:


testCount


# In[117]:


testArray = a[np.arange(testCount,a.shape[0],testCount),:]
trainArray = a
trainArray = np.delete(trainArray, np.arange(testCount,a.shape[0],testCount), 0)


# In[118]:


testArray


# In[119]:


trainArray


# In[121]:


np.savetxt("..\data\ExportedDatabase.csv", a, delimiter=";")


# In[125]:


np.savetxt("..\data\ExportedDatabaseTrain.csv", trainArray, delimiter=";", fmt='%4d')


# In[123]:


np.savetxt("..\data\ExportedDatabaseTest.csv", testArray, delimiter=";", fmt='%4d')

