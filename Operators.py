
'''
a=5
b=10
c=20
print(a,b,c)

a+=5

'''


'''
values =(1,2,3)
a,b,c=values
print(a,b,c)
'''


'''
values =(1,2,3,4,5,6)
a,b,*c =values
print(a,b,c)

'''


'''
x=int(input("x: "))
y=int(input("y: "))

a,b,c=2,5,10

sonuc= (x * y) - (a+b+c)
print(sonuc)

'''
# karşılaştırma operatörlerinde koşul sağlanırsa true 
# sağlanmazsa false dönütü verir (==,!=,>=,<=,>,<)



'''
x=int(input("x: "))
y=int(input("y: "))

sonuc= x>y

print(f"{x},{y}'den büyüktür {sonuc}")

'''



'''
_email="info@obahceci.com"
_password="12345"

email= input("email: ")
password= input("password: ")

isEmail= (email.lower().strip() == _email)
print(isEmail)
'''


#mantıksal operatörler


'''
#and operatörü

x=13
sonuc =5 < x < 15 
sonuc = (x>5) and (x<15)
print(sonuc)

'''

'''
#or operatörü

x=13
sonuc = (x>0) or (x%2==0)
print(sonuc)
'''


'''
#not operatörü

x=13
sonuc =not(x>0)   #kosulun tersini alir 
print(sonuc)

'''

'''
# is / is not  operatörü 

x=y= [1,2,3]
z=[1,2,3]


print(x==y) 
print(x==z)   #aynı sonuclara sahip olduğu için true döndürür


print(x is y) #is operatörü objeleri karşılaştırır 
print(x is z) #değerler aynı olsa bile adresler faklıdır.

'''


# in operatörü 
x=["apple","banana"]
print("banana" in x)
print("cherry" not in x)