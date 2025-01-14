
'''
if(1):
    print("Merhaba")          #koşul her zaman sağlandiği durum 

'''


'''
username ="oguzhan"

if(username=="oguzhan"):                    #koşullarda and ve or ifadeleri kullanılabilir 
    print("dogru kullanici adi")
else:
    print("Yanlis kullanici adi")
'''


'''
x=10
y=20

if(x>y):
    print("x y den büyüktür")
elif(x==y):
    print("x y ye eşittir")
else:
    print("x yden küçük")

'''


'''
x= int(input("Bir sayı giriniz:"))

if(x>50 and x<100):
    print(f"{x}, 50 ile 100 arasındadır")
else:
    print(f"{x}, 50 ile 100 arasında değildir")

'''

'''
x= int(input("Bir sayı giriniz:"))

if(x>0):
    if(x%2==1):
        print(f"{x}, pozitif tek sayıdır")
    else:
        print(f"{x},pozitif çift sayıdır")

else:
    print(f"{x},negatif sayıdır")

'''


'''
age= int(input("enter your age:"))
edu = input("enter your graduation level: ")

if(age>=18):
    if(edu.lower().strip()=="high school" or edu.lower().strip()=="university" ):
        print("available to take driver lisence")
    else:
        print("unavaiable to take lisence not having adequate graduate level")
else:
    print("can't take driver lisence under 18 ")

'''
'''
x,y=float(input("1. quiz note: ")),float(input("2. quiz note: "))

grad=(x+y)/2
gpa={};

if(grad>0 and grad<=24):
    gpa=0
if(grad>24 and grad<=44):
    gpa=1
if(grad>44 and grad<=54):
    gpa=2
if(grad>54 and grad<=69):
    gpa=3
if(grad>69 and grad<=84):
    gpa=4
if(grad>84 and grad<=100):
    gpa=5

print(f"gpa ={gpa}")

'''

#datetime modulü ile şimdiki zamanın tarihini alırız
# obje türünde işlem yapmamız gerektiği için girilen tarihi de obje türüne çeviririz
'''                 

import datetime
tarih= input("Araç trafiğe çıkış tarihini giriniz: ")
tarih=tarih.split("/")

simdi=datetime.datetime.now()
tarih=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark= simdi - tarih
gun = fark.days

if(gun<=365):
    print("1. servis bakımı")
elif(gun>365):
    print("2. servis bakımı")

'''



