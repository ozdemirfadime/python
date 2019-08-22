#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 21:18:58 2019

@author: linus
"""
#import library
import pandas as pd
import  matplotlib.pyplot as plt 
import numpy as np
#import data
df  = pd.read_csv("machineornek.csv")
#df  = pd.read_csv("machineornek.csv",sep =";")

 #plot data
plt.scatter(df.deneyim,df.maas)
plt.xlabel("deneyim")
plt.ylabel("maas")
plt.show()
#%%  linear regression
#sklear:machine learn library
from sklearn.linMear_model import LinearRegression
#lineear regression model
linear_reg= LinearRegression()
x=df.deneyim.values.reshape(-1,1)
y=df.maas.values.reshape(-1,1)
linear_reg.fit(x,y) 


#%% prediction
b0 =linear_reg.predict(0)
print("b0:",b0)
b0_= linear_reg.intercept_ # y eksennin kestiği nokta
print("b0:",b0_)
b1 =linear_reg.coef_  # eğim slope 
print("b1:",b1)
# maas = 1510+1151*deneyim
maas_15 =1510+1151*15
print(maas_15)
maas15 =linear_reg.predict(15) #15 yıllım deneyim 
print(maas15)
#visualize
from sklearn.metrics import r2_score
print("r square score:",r2_score(y,y_head))
array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)
plt.scatter(x,y)
plt.show()
y_head = linear_reg.predict(array) #maas
plt.plot(array,y_head,color="blue")
linear_reg.predict(100)
#%% r square
#sklear:machine learn library
from sklearn.linear_model import LinearRegression
#lineear regression model
linear_reg= LinearRegression()
x=df.deneyim.values.reshape(-1,1)
y=df.maas.values.reshape(-1,1)
linear_reg.fit(x,y) 
y_head =linear_reg.predict(x)
plt.plot (x,y_head,color="red")
from sklearn.metrics import r2_score
print("r square score:",r2_score(y,y_head))

