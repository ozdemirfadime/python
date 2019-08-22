#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 22:33:38 2019

@author: linus
"""
 # loc gets rows (or columns) with particular labels from the index.
  #  iloc gets rows (or columns) at particular positions in the index (so it only takes integers).
   #ix usually tries to behave like loc but falls back to behaving like iloc if a label is not present in the index.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("Decision_tree.csv",sep =";",header =None)
x =df.iloc[:,0].values.reshape(-1,1)
y =df.loc[:,1].values.reshape(-1,1)
#%%
from sklearn.ensemble import RandomForestRegressor
rf= RandomForestRegressor(n_estimators=100 ,random_state=42) #100 tane tree 
rf.fit(x,y)
print("7.8 seviyesindeki:",rf.predict(7.8))
x_ =np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head=rf.predict(x_)
#visulazintimatorr
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun")
plt.ylabel("ucret")
plt.show()
#%% R-square
y1_head=rf.predict(x)
from sklearn.metrics import r2_score
print("r square:",r2_score(y,y1_head)) # 1 e ne kadar yakın olursa o kadar iyi demektir
