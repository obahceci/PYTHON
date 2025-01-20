
'''
def selamla() :
    print("selam")

selamla()
'''

'''
def toplam():
    return f"toplam: {10+20}"

print(toplam())
'''


'''
def simdi():
    import datetime
    return datetime.datetime.now().year

def hesapla():
    return simdi()-2003

print(hesapla())

'''

#parametre gönderme 

'''
def cubic(x):
    return x*x*x

a=int(input("x: "))
print(f"cube of {a} is {cubic(a)}")
'''

'''
def currentYear():
    import datetime
    return datetime.datetime.now().year

def calculateAge(yearOfBirth):
    return currentYear()-yearOfBirth

age=int(input("Enter your year of birth : "))

print(f"Your current age is {calculateAge(age)}")

'''


'''
kelime=input("yazdırmak istediğin kelime: ")
tekrar = int(input("Kaç defa yazdırmak istiyorsun: "))

def yazdır(word,iter):
    for i in range(iter):
        print(word)
    
yazdır(kelime,tekrar)
'''


'''
def calculate(a,b):
    return print(f" alan: {a*b}\n cevre: {2*a + 2*b}")

x=int(input("kısa kenar giriniz: "))
y=int(input("uzun kenar giriniz: "))

calculate(x,y)

'''




'''

def CoinToss(x):
    import random
    return random.choice(x)

coin = ["yazı","tura"]

print(CoinToss(coin))

'''

'''
def prime(a, b):
    if a < 2:  
        a = 2

    for num in range(a, b):  
        is_prime = True
        for i in range(2, num):  
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number")


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
prime(start, end)

'''


'''
def divisor(x):

    div=[]
    for sayi in range(1,x+1):
        if(x%sayi==0):
            div.append(sayi)
    
    return div

num= int(input("enter number to determine divisors: "))

print(divisor(num))
'''

#default parametre 

# non default olmayan parametrenin default parametreden önce gelmesi gerekir 
'''
def selamla(isim ="Kullanıcı", mesaj="Merhaba"):
    print(f"{mesaj} {isim}")

selamla()
selamla("Oğuzhan")
selamla("Oğuzhan","İyi Günler")
#eğer parametrenin default halini kullanmak istiyorsdak fonksiyon tanımlşarken paramtreye de tanımlama yapmöalıyız

'''

#default argument
'''
def selamla(isim,mesaj):
    print(f"{mesaj} {isim}")

selamla(mesaj="Merhaba",isim="Oğuz")
'''

#değişken sayıda parametre 
'''
def toplam(*args):              # *args tuple yapısında olur
    sonuc = 0
    for i in args:              #istenilen sayıda parametre girmemize yarar
        sonuc+=i
    return sonuc 

print(toplam(10,20,30))
print(toplam(10,20,30,40))
'''


'''
def displayUser(**kwargs):          # **kwargs dictionary yapısında olur
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

displayUser( username="oğuzhan", email="info@obahceci.com",gender="male")
'''


'''
def karakter(s):                        # bir karakterden ifade içinde kaç tane bulunur hesaplamak için 
    return {letter: s.count(letter) for letter in s}

sonuc =print(karakter("ahdsbfjkladhbgjlıegnsuıghalrıughaerılgsb"))

'''


'''
def update(liste,command,position,value=None):
    if(command=="remove" and position=="end"):
        return liste.pop()

    elif(command=="remove"and position=="beginning"):
        return liste.pop(0)
    
    elif(command=="add" and position=="end"):
        return liste.append(value)
    
    elif(command=="add" and position=="beginning"):
        return liste.insert(0,value)
'''

'''
def contain(*args):
    if "blue" in args:
        return True
    return False

sonuc=print(contain("blue","yellow","red"))
'''


 
#global ve local değişkenler 
'''
x=50
def change():
    global x                        #değişkenş global yapar fonksiyonda yapılan işlemler değişkeni etkiler 
    print(f"x: {x}")

    x=100
    print(f"x ----> {x}")

change()
print(x)
'''


#LAMBDA FONKSİYONU

'''
def multiply(a):
    return a**2
print(multiply(4))

sonuc= ( lambda a: a**2)(4)
print(sonuc)
'''


'''
topla= lambda a,b,c : a+b+c
sonuc =topla(1,2,3)
print(sonuc)
'''


'''
def myFunc(n):
    return lambda a: a*n

multip2=myFunc(2)
multip3=myFunc(3)

sonuc1= multip2(10)
print(sonuc1)

sonuc2=multip3(10)
print(sonuc2)
'''


#MAP FONKSİYONU

'''
sayilar=[1,2,5,7,9]
kareler=[]

for i in sayilar:
    kareler.append(i**2)                #normalde yaptığımız 

print(kareler)


kareler =[i**2 for i in sayilar]        #comprehension methodu 
print(kareler)


def kareAl(sayi):
    return sayi**2

sonuc=list(map(kareAl,sayilar))                 #map methodu 
print(sonuc)                                    #map türünde sonuc verir listeye cevirmemiz gerekir 
sonuc2=list(map(lambda sayi: sayi**2, sayilar))                                   
print(sonuc2)
'''


#FİLTER
 
'''
yas=[5,12,18,24,45]

def age(x):
    if x<18:
        return False
    return True

sonuc=list(filter(age,yas))
print(sonuc)    
sonuc1=list(filter(lambda x: x>=18,yas))
print(sonuc1)    

'''


#ANY / ALL 
'''
sonuc = all([True,True,False])      #hepsi true olmalı 
print(sonuc)

sonuc = any([True,True,False])      # en az bir tane true olması yeter 
print(sonuc)
'''

#SORTED 

'''
sayilar=[1,53,45,67,97,5,7]

#sayilar.sort()             #orjinal liste değişir 

sonuc=sorted(sayilar)          # orijinal liste değişmez

sonuc1=sorted(sayilar, reverse=True)

sonuc2=tuple(sorted(sayilar))

print(sayilar)
print(sonuc)
print(sonuc1)
print(sonuc2)

'''


#MİN / MAX
'''
sayilar=[1,5,7,45,25,89]                #stringlerde de kullanılır 
sonuc= print(min(sayilar))
'''


'''
urunler = [
    {"name":"iphone x","price":5000},
    {"name":"iphone xr","price":6000},
    {"name":"iphone 11","price":7000}
]
sonuc = min(urunler,key=lambda urun: urun["price"])
print(sonuc)
'''


#SUM
'''
sayilar=[1,5,7,45,25,89]

sonuc=print(sum(sayilar))

urunler = [
    {"name":"iphone x","price":5000},
    {"name":"iphone xr","price":6000},
    {"name":"iphone 11","price":7000}
    ]
sonuc = sum([urun["price"]for urun in urunler])
print(sonuc)
'''


#ROUND

'''
print(round(10.2))

print(round(1.283728749274023,4))
'''
