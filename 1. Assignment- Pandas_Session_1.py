#!/usr/bin/env python
# coding: utf-8

# ## Assignment -  1

# ###  Import the necessary libraries

# In[48]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[49]:


get_ipython().system('pip install pyforest')


# ###  Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). <br>
# Use sep= "|" while reading the data

# In[2]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# ### Assign it to a variable called users and use the 'user_id' as index

# In[50]:


user = data = pd.read_csv(url,sep = '|',index_col='user_id')


# In[ ]:





# ### See the first 10 and last 10 entries 

# In[51]:


user.head(10)


# In[52]:


user.tail(10)


# ### What is the number of observations in the dataset?

# In[53]:


user.shape[0]


# ### What is the number of columns in the dataset?

# In[54]:


user.shape[1]


# ### Print the name of all the columns.

# In[55]:


user.columns


# ### How is the dataset indexed?

# In[57]:


dataset.set_index(column name)


# ### What is the data type of each column?

# In[24]:


user.dtypes


# ### Print only the occupation column

# In[25]:


user['occupation']


# ### How many different occupations are in this dataset?

# In[26]:


user['occupation'].value_counts()


# ### What is the most frequent occupation?

# In[27]:


user['occupation'].mode()[0]


# ###  DataFrame Info.

# In[28]:


user.info()


# ### Describe all the columns

# In[29]:


user.describe(include='all')


# ### Summarize only the occupation column

# In[58]:


data_pivot = pd.pivot_table(user,
         index='occupation')
data_pivot


# ###  What is the mean age of users?

# In[40]:


user['age'].mean()


# ###  What is the age with least occurrence?

# In[47]:


user['age'].min()


# In[ ]:




