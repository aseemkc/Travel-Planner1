#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_excel('Dataset.xlsx', index = None)
df.head()
G=nx.from_pandas_edgelist(df, 'Departure Station', 'Arrival Station','Time of Travel')
nx.draw(G, with_labels=False)
df['Route'] = df['Departure Station'].map(str) + ' - ' + df['Arrival Station'].map(str)
df.head()
df2 = df[['Route','Tube Line', 'Time of Travel']]
df3=df2.drop_duplicates()
df3['Route Reversed'] = df['Arrival Station'].map(str) + ' - ' + df['Departure Station'].map(str)
df6 = df3[['Route Reversed', 'Tube Line', 'Time of Travel']]
df6.rename(columns = {'Route Reversed' : 'Route'}, inplace = True)
df3 = df3.append(df6, ignore_index = True)
del df3['Route Reversed']



def route_calculator(source,target):

    d, p = nx.single_source_dijkstra(G,source=source, target=target, weight='Time of Travel')
    route=[]
    for i in range(len(p)-1):
        route.append(str(p[i]+" - "+p[i+1]))
    df4 = pd.DataFrame(route, columns=["Route"])
    df5 = pd.merge(df4,df3,"left", left_on="Route", right_on="Route")
    df5.to_excel('Result.xlsx')
    



    print(df5)
    print("Total time for Travel", d+ len(p) -2 , "Mins (Includes 1 min wait time at each station :))")









