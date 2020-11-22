#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


data = pd.read_excel('stationdata.xlsx')

dataset = data['Station Names']
datalist = dataset.values.tolist()





