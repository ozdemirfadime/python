#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#gorsellestirme kutuphanesi

#line plot, scatter plot,bar plot ,subplots,histogram
import pandas as pd
iriscsv = pd.read_csv("/home/linus/python/Python/mathplot/iris.csv ")
#cvs virgül ile ayrılmış değerler
print(iriscsv.columns)
print(iriscsv.Species.unique())#benzersiz turleri listeler
print(iriscsv.info())#dataframe hakkinda bilgiler
print(iriscsv.describe()) #numeric degerleri karsilastırmanızı
setosa =iriscsv[iriscsv.Species == "  Iris-setosa" ]
versicolor =iriscsv[iriscsv.Species == "Iris-versicolor  " ]
virginica = iriscsv[iriscsv.Species == "Iris-virginica"   ]
print(setosa.describe())
print(versicolor.describe()) 
print(virginica.describe())
#%% line plot
import matplotlib.pyplot as plt

iriscsv1 =iriscsv.drop(["Id"],axis =1) # id satirini siliyoruz

#iriscsv1.plot() #default metodu line 
#plt.show() #cizile plotun gosterilmesi
setosa =iriscsv[iriscsv.Species == "Iris-setosa"]
versicolor =iriscsv[iriscsv.Species == "Iris-versicolor"]
virginica = iriscsv[iriscsv.Species == "Iris-virginica"]
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa",grid =True)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label="virginica")
plt.xlabel("Id")
plt.ylabel("petalLengthCm")
plt.legend() #plt.legend plot üzerinde labelların gözükmesini sağlıyor.
plt.show()

#iriscsv1.plot(grid=True,linesytle = ":",alpha = 0.1) #izgara :grid,alpha saydamlık artırır sıfır yaklastikce
#plt.show()

#%% scatter plot
setosa =iriscsv[iriscsv.Species == "Iris-setosa" ]
versicolor =iriscsv[iriscsv.Species == "Iris-versicolor"]
virginica = iriscsv[iriscsv.Species == "Iris-virginica"]
plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color= "red",label ="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color= "blue",label ="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color= "green",label ="virginica")
plt.legend()
plt.xlabel("PetalLenghtCm") 
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()
#%%histogram
plt.hist(setosa.PetalLengthCm,bins=20) #bins barların sayisisi
plt.xlabel("PetalLengthCm degerleri")
plt.ylabel("frekansi")
plt.title("histogram")
#%% bar plot 
import numpy as np
#x =np.array([1,2,3,4,5,6])
#y = x*2+5
#plt.bar(x,y)
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()

x = np.array([1,2,3,4,5,6])
a = ["turkey","us","uk","f","q","w","e"]
y = x*2+5
plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("a")
plt.ylabel("y")
plt.show()