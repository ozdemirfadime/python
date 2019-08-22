#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:06:19 2019

@author: linus
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("data.csv")
print(data.info())
data.drop(["Unnamed: 32","id"],axis =1,inplace=True) # biyi we dont use unmade and id feature
#data.diagnosis = [  1 if  each = "M" else 0 for each in data.diagnosis] #1:bad ,0:good
print(data.info()) # diagnosis  wasint64
y =data.diagnosis.values
x_data = data.drop(["diagnosis"],axis =1)
#normalization 0 ile 1 arasına yerleştirmek features arasında fark çok olmasın
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data)).values
# (x - min(x))/(max(x)-min(x))
#%% train test split 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)
#%80:train ,%20 :test
x_train =x_train.T
x_test=x_test.T
y_train =y_train.T
y_test=y_test.T
print("x_train:",x_train.shape)
print("y_train:",y_train.shape)
print("x_test:",x_test.shape)
print("y_test:",y_test.shape)np.
#%% parameter initialize and sigmund  function
def initialize_weights_bias(dimension): #30 featuees is dimension
  w =np.full((dimension,1),0.01)    #dimesion*1  0.01 matrix
  b =0.0
  return w,b
#w,b =initialize_weights_bias(30)
#sigmund function  f(x)=1/(1+e^-(x))
def sigmund(z):
    y_head = 1/(1+np.exp(-z))
    return y_head
#print(sigmund(0))
#%%
def forward_backward_propagation(w,b,x_train,y_train) 
#y_train =karşılaştırma
#forward propagation
z=np.dot(w.T,x_train) +b #30,1 *30,455
#This function returns the dot product of two arrays.
#For 2-D vectors, it is the equivalent to matrix multiplication. 
y_head =sigmund(z)
loss =-y_train*np.log(y_head)-(1-y_train)*np.log(1-y_head) #−(ylog(p)+(1−y)log(1−p))
cost=(np.sum(loss))/x_train.shape[1] #x_train.shape[1] is fro scaling normalize
#backward propagation
derivative_weigth =(np.dot(x_train,((y_head-y_train).T)))/x_train.shape[1] #x_train.shape[1] is fro scaling
derivative_bias =np.sum(y_head-y_train)/x_train.shape[1] #x_train.shape[1] is fro scaling
gradient ={"derivative_weight:",derivative_weigth,"derivative_bias:",derivative_bias}
#gradient :store features dic
return cost,gradient

def update(w, b, x_train, y_train, learning_rate,number_of_iterarion): #number_of_iterarion many agin
    cost_list = []
    cost_list2 = []
    index = []
    # updating(learning) parameters is number_of_iterarion times
    for i in range(number_of_iterarion):
        # make forward and backward propagation and find cost and gradients
        cost,gradients = forward_backward_propagation(w,b,x_train,y_train)
        cost_list.append(cost)
        # lets update
        w = w - learning_rate * gradients["derivative_weight"]
        b = b - learning_rate * gradients["derivative_bias"]
        if i % 10 == 0:
            cost_list2.append(cost)
            index.append(i)
            print ("Cost after iteration %i: %f" %(i, cost))
    # we update(learn) parameters weights and bias
    parameters = {"weight": w,"bias": b}
    plt.plot(index,cost_list2)
    plt.xticks(index,rotation='vertical')
    plt.xlabel("Number of Iterarion")
    plt.ylabel("Cost")
    plt.show()
    return parameters, gradients, cost_list 

def predict(w,b,x_test):
    z = sigmund(np.dot(w.T,x_test)+b)
    Y_predict =np.zeros((1,x_test.shape[1])
    for i in range(z.shape[1]):
       if z[0,i]<=0.5 :
           Y_predict[0,i]=0
       else: 
           Y_predict[0,i]=1
           
           return Y_predict
       # %% logistic_regression
def logistic_regression(x_train, y_train, x_test, y_test, learning_rate ,  num_iterations):
    # initialize
    dimension =  x_train.shape[0]  # that is 30
    w,b = initialize_weights_and_bias(dimension)
    # do not change learning rate
    parameters, gradients, cost_list = update(w, b, x_train, y_train, learning_rate,num_iterations)
    
    y_prediction_test = predict(parameters["weight"],parameters["bias"],x_test)

    # Print test Errors
    print("test accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_test - y_test)) * 100))
    
logistic_regression(x_train, y_train, x_test, y_test,learning_rate = 1, num_iterations = 300)    
