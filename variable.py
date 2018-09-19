#%%
var1=10
var2=4
var3=10.0 #double /float 
Var7=78 #buyuk harfle değişken ataması uygun değildir
#%%
#string
s="buun pazartesi"
variable_type=type(s)#str string
print(s)
var1="ankara"
var2="ins"
var3=var1+var2
var4="100"
var5="345"
var6=var4+var5
uzunluk = len(var6)
#%%
#numbers
#int double 
int_deneme=-50
#double=float=ondalikli sayi
float_deneme=-30
float=10
#%% bulilt function
str1="deneme"
float1=10.5
round(float1)
float(10)
int(float1)
str2="1230"
#%% user defined function
#fonk parameresi =input
var1 = 3
var2 = 5
def  my_fuction(var1,var2):
    """ bun benim ilk denemeler 
    parametre
    return:
        """
        output = (((var1+var2)*50)/100.0)*var1/var2
        return output 
 sonuc=my_function(var1,var2)
#%%defaoult ve flexibele function
 #çemberin cevre uzunlugu=2*pi*r
 #default
 def cember_cev(r,pi=3.14):
     """
     cemberin cevresini hesapla 
     input(parametre):r,pi
         output=cemberin cevresi
     """
     output = 2*pi*r
     return output
 #flexible
 def hesaplama(boy,kilo,*args):
     print(len(args))
     print(args)
     output=(boy+kilo)*args[0]
     return output
 
  #  def hesaplama(boy,kilo,yas):
   #  output=(boy+kilo)*yas
   #  return output
   
   
   #%%quiz
   #int variable  yas
   #string name isim
   #fonksiyonu
   #fonk print(type(),len,float())
   #*args soyisim 
   #default parametre ayakkabı numarası
yas = 10
name = "railly"
soyisim = "dr"
def func_quiz(yas,name,*args,ayakkabi_numarasi=30):
    print("cocugun ismi:",name,"yasi:",yas,"ayakkabıno:",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
       output = args[0]*yas
    return output
sonuc = func_quiz(yas,name,soyisim)
print("args[0]*yas:",sonuc)
 #%%
 yas = 10
name = "ali"
soyisim = "veli"

def function_quiz(yas,name,*args,ayakkabi_numarasi=35):
    print("Cocugun ismi: ",name, " yasi: ",yas," ayak numarasi: ",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    
    return output

sonuc = function_quiz(yas,name,soyisim)

print("args[0]*yas: ",sonuc)
#%%lambda function 
def hesaplama(x):
    output =x*x
    return output
sonuc = hesaplama(3)
sonuc2 = lambda x: x*x
print(sonuc2(3))



