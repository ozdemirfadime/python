#!/usr/bin/enva python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:01:57 2019

@author: linus
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df =pd.read_csv("polynomial_regression.csv")
y =df.araba_max_hiz.values.reshape(-1,1)
x=df.araba_fiyat.values.reshape(-1,1)
plt.scatter(x,y)
plt.xlabel("araba_fiyat")
plt.ylabel("araba_max_hix")
plt.show()
#linear regression  y=b0+b1*x1
#multiple regression y=b0+b1*x1+b2*x2
#%%
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x,y)
#predict 
y_head =lr.predict(x)
plt.plot(x,y_head,color ="red",label="linnear")
plt.legend()
plt.show()
lr.predict(10000)
#%%##polyonom regression  y=b0+b1*x b2*x^2 +b3*x^3.....bn*x^n
from sklearn.preprocessing import PolynomialFeatures
polynomial_regression =PolynomialFeatures(degree =5)
 #degree =n neereye kadar sınırandırmak istediğin
x_polynomial = polynomial_regression.fit_transform(x)
 #x^2ecevirveuygula
 #%% fit
linear_regression2 =LinearRegression()
linear_regression2.fit(x_polynomial,y)
#%%
y_head2 =linear_regression2.predict(x_polynomial)
plt.plot(x,y_head2,color ="green",label="polynomial") # degreeartıkça daha yakın sonuç elde edilebilir(mse min)
plt.legend()
plt.show()