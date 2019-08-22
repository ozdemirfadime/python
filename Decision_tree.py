#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:29:05 2019

@author: linus
"""
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
df =pd.read_csv("Decision_tree.csv",sep=";",header =None)
x =df.iloc[:,0].values.reshape(-1,1)
y =df.iloc[:,1].values.reshape(-1,1)
#%%decision tree
 from sklearn.tree import  DecisionTreeRegressor
 tree_reg =DecisionTreeRegressor()
 tree_reg.fit(x,y)
 tree_reg.predict(5.5)
 x_ =np.arange(min(x),max(x),0.01).reshape(-1,1)
 y_head =tree_reg.predict(x_)
 #%% visulazion
 plt.scatter(x,y,color="red")
 plt.plot(x_,y_head,color="green")
 plt.xlabel("tribun")
 plt.ylabel("ucret")
 plt.show()