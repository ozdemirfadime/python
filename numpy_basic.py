#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:31:45 2018

@author: linus
"""
#import ettme
import numpy as np 
#numpy basic
#%%
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
#%% numpy basic operation
import numpy as np 
a =np.array([1,2,3,4])
b = np.array([2,3,4,5])
print(a+b)
print(a-b)
print(a**2)
print(np.sin(a)) # a'nin sinus  degerlerini hesaplar
print(np.tan(b))
print(a<2)# a matrisinin içinde 2 kücükler true doner

a = np.array([[1,2,6],[1,5,4]])
b = np.array([[1,2,6],[8,5,4]])
print(a)
print(a*a)
print(a*b)

a.dot(b.T) 
#a *b yapmanız için (2,3)*(3,2) matrisleri olmasi gerekir 
#bunun icin b'nşn transpazonu aldık
print(np.exp(a))

a =np.random.random((6,6))# 0 ile 1 arasında 6*6 lik matris uretti random
print(a.sum()) #toplam dnegeri
print(a.max()) #max eleman
print(a.min()) #min elema
print(a)
print(a.sum(axis=0)) #satirlari topla
print(a.sum(axis=1)) #sutunları topla

print(np.sqrt(a)) #karakok
print(np.square(a)) #a**2
print(np.add(a,a)) #=a+a

#%% indexin and slicing
import numpy as np
array = np.array([1,8,2,3,7,9]) #tek boyutlu vector
print(array[0])
print(array[0:4]) #1,8,2,3 4.indeksi almaz
ters_array= array[::-1]
print(ters_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,11]]) #2 boyutlu
print(array1[1,1]) #1.satirin 1.sutunu #7
print(array1[:,1]) #satirların 1.sutunun al yanı 0 ve 1. sutun #2,7  
#:satırların hepsini al demek
print(array1[1,1:4]) #1.satrıın 1,2,3 degerleri
print(array1)
print(array1[-1,:]) #sonsatır
print(array1[:,-1]) #son sutun


#%%
#shape manipulation
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
#flatten
a =array.ravel() #matrisin vector haline getirdi
array2 = a.reshape(3,3) # 3*3 eski haline dondu
arrayT = array2.T #transpozu
print(arrayT.shape)
array3= np.array([[1,2],[7,8],[6,4]])
print(array3.shape)
print(array3.reshape(2,3)) #tutmak için  degere esitlemek gerekir
print(array3.resize(2,3)) # direkt degistirir
array3 = np.column_stack((array,array2))
#%%stacking arrays :dizilerin birleştirmenp
import numpy as np 
array1 = np.array([[1,2,],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
#[1, 2],[-1, -2],yatay birlestirme
 # [3, 4], [-3, -4]])
array3 = np.vstack((array1,array2))
 
#[1, 2],dikey birleştirme
#[3, 4]])
#-1, -2],
#[-3, -4]
array4 = np.hstack((array1,array2))


#%%convert and copy
liste=[1,2,3,4]
dizi=np.array([5,6,7,8,9])
array= np.array(liste)#listeden diziye gecmis oluyorsunuz
liste2 =list(array) #diziden listeye cevirme

a =np.array([1,2,3]) # a,b,c hepsi aynı yerde tutuldugun biri değisirse hepsi degişir
b =a
b[0]=5
c =a
d=np.array([1,2,3]) # cpy ile hesine farklı alan oluşruldu
e =d.copy()
e[1]=6
f =d.copy()