#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:58:40 2018

@author: linux
"""

import pandas as pd
dictionary = {"name":["ali","kenan","evren","veli","ayse","hilal"],
              "age":[15,16,13,17,78,49],
              "sales":[100,4230,48657859,456,12,3]}
dataFrame1 = pd.DataFrame(dictionary) #

head = dataFrame1.head(3) #ilk uc
tail = dataFrame1.tail(2) #son iki
#%%
#pandas basic method 
print(dataFrame1.columns) #sutunlar
print(dataFrame1.info) #frame hakkında bilgi verir
print(dataFrame1.dtypes) #obkect =string hersutuunu turunu verir
print(dataFrame1.describe()) #sadece numeric feature(ozellik) =sutunlar
#%%
#indexing and slicing


print(dataFrame1["age"]) #indeks bilgileri pandast aherzamn gosterirlir
print(dataFrame1.age) #herikiside yasları verir
dataFrame1["yeni_ozellik"]= [-1,-2,-3,-5,-6,-4]
#print(dataFrame1["yeni_ozellik "])
print(dataFrame1.loc[:,"age"]) #butun satırları al  ve age sutununu al
print(dataFrame1.loc[:3,"age"]) # 3 satir ve age sutunu alir, pandasta 3.indekte dahildir
print(dataFrame1.loc[:3,"age":"name"])
print(dataFrame1.loc[:3,["age","name"]])
print(dataFrame1.loc[::-1,:]) #tersten yazdırma
print(dataFrame1.loc[:,:"sales"])#butun satırları sales kadar sales dahil sutnları
print(dataFrame1.loc[:,"name"])
print(dataFrame1.iloc[:,1])#integerlocatiton,indeksi veriryoruz
#%%

#filtering   
filtre1= dataFrame1.sales<200
print(type(filtre1))
filterli_veri =dataFrame1[filtre1]
filtere2 = dataFrame1.age<20
dataFrame1[filtre1 & filtere2] #maasi 20den kucuk ve yası 20den kucukleri filtreler
dataFrame1[dataFrame1.age>60]# yasi 60dan buyuk olanı secer

#%%
#list comprehensio
import numpy as np
ortlama_maas =dataFrame1.sales.mean()
#ort_maas_np=np.mean(dataFrame1.sales)
dataFrame1["sales status"]= ["dusuk"if ortlama_maas >each else "yuksek"  for each in dataFrame1.sales]
#for each in dataFrame1.sales :
 #   if(ortlama_maas >each):
  #      print("yuksek")
   # else:
    #    print("dusuk")
dataFrame1.columns = [each.upper() for each in dataFrame1.columns]
dataFrame1.columns = [each.lower() for each in dataFrame1.columns]
dataFrame1.columns = [each.split() [0] +"_"+ each.split()[1] if len(each.split ()) >1 else each for each in dataFrame1.columns]


#%%
#drop and concatenating(iki dataframi birleştirmek)
#dataFrame1.drop(["yeni_ozellik"],axis=1,inplace=True) #axis=1 yukarıdan asagıya bir sutun yani
                                                     #inplace=true demek drop et ve dataframe esitle
                                                     
data1=dataFrame1.head()                                               
data2 = dataFrame1.tail()
#vertical birleştirme
data_concat =pd.concat([data1,data2],axis=0)

#horizontal
sales=dataFrame1.sales
age=dataFrame1.age
data_h_concat =pd.concat([sales,age],axis=1)
#%%
#tranforming dataomp

dataFrame1["list_comp"] = [each*2 for each in dataFrame1.age ]
#apply()
def multiply(age):
    return age*2
dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)