#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:31:45 2018

@author: linus
"""
#import ettme
import numpy as np 
#numpy basic
array = np.array([1,2,3,6,6,9,7,8,5,4,13,78,96,31,64])

print(array.shape)

a = array.reshape (3,5) 
print("shape",a.shape)
print("dimesion",a.ndim)
print("data type",a.dtype.name)
print("size",a.size)
print("type:t",type(a))
array1 = np.array([[1,2,3],[7,8,9,6,4],[4,5,9,8,708]])
zeros= np.zeros((3,4)) #oluşsan sifirlardan  matris oluşturur.yer ayırmak
zeros[0,0]  =5
np.ones((3,4)) #birlerden oluşan 3*4 matrisi
np.empty((3,4)) #3*4lük bos bir matris
a = np.arange(10,50,5)
print(a)
print("****************")
a = np.linspace(1,10,20)# 1 ila 10 arasında 20 tane sayi urrettti
print(a)