 
'''
def outer(num1):
    print("outer")

    def inner(num1):
        print("inner")
        return num1 + 1
    
    num2=inner(num1)
    print(num1,num2)


#outer(10)
#inner(10)
'''



#iç içe fonksiyon

'''
def factoriral(num):
   
   if not isinstance(num,int):
    raise TypeError("Number must be integer")
   
   if not num>=0:
    raise ValueError("Number must be at least zero")
   
   else:
    def inner_fac(num):
        if num<=1:
            return 1

        return num * inner_fac(num-1)
    
    return inner_fac(num)


try:
    print(factoriral(-5))
except Exception as e:
   print(e)

   '''


#fonksiyon döndürme


'''
def pow(number):

    def inner(power):
        return number**power
    return inner


two=pow(2)

print(two(3))

'''

#fonksiyonları parametre olarak gönderme 

'''
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bölme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):

    if islem_adi=="toplama":
        print(f1(2,3))
    elif islem_adi=="cikarma":
        print(f2(5,3))
    elif islem_adi=="carpma":
        print(f3(3,4))
    elif islem_adi=="bolme":
        print(f4(10,2))
    else:
        print("geçersiz işlem ")
'''




#decorator

'''
def selamlama(fn):
    def wrapper():
        print("\nhoş geldiniz")
        fn()
        print("görüşmek üzere\n")
    return wrapper

@selamlama
def gunaydin():
    print("günaydın")

@selamlama 
def iyigunler():
    print("İyi günler")


gunaydin()

iyigunler()

'''