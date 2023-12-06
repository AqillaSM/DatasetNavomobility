#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import library
import pandas as pd
import numpy as np


# In[4]:


#load dataset
package = pd.read_csv('package_tourism.csv')
rating = pd.read_csv('tourism_rating.csv')
tourism = pd.read_csv('tourism_with_id.csv')
user = pd.read_csv('user.csv')


# In[5]:


tourism


# # Hanya mengambil data pada Kota Surabaya dikarenakan prototype dijalankan di Kota Surabaya

# In[8]:


tourism = tourism.loc[tourism['City'] == 'Surabaya']
tourism

