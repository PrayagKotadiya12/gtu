#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
file = np.loadtxt("cric.tsv",skiprows=1)
print(file)


# In[24]:


np.mean(file)


# In[25]:


np.median(file)


# In[34]:


Sachin = file[:,1] 
Sachin


# In[35]:


Dravid = file[:,2]
Dravid


# In[36]:


India = file[:,3]
India


# In[37]:


def stats(a):
    median = np.median(a)
    mean = np.mean(a)
    return mean,median


# In[41]:


mean1, median1 = stats(Sachin)
print("Mean runs are {} and Median runs are {}".format(mean1,median1))


# In[42]:


mean2, median2 = stats(Dravid)
print("Mean runs are {} and Median runs are {}".format(mean2,median2))


# In[43]:


mean3, median3 = stats(India)
print("Mean runs are {} and Median runs are {}".format(mean3,median3))

