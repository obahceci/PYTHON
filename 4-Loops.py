
'''
sayilar =[1,2,3,4,5,6]              #array

for i in sayilar :
    print(i)
print("\n")
 '''   

'''
isim = "Oğuzhan Bahçeci"            #string array

for j in isim:
    print(j)
print("\n")
'''

'''
_tuple=[(1,2),(4,5),(6,7)]             #tuple    

for k,l in _tuple:
    print(k,l)
'''


'''
d={                                     #dictionary
    "k1":1,
    "k2":2,
    "k3":3,
}

# for x in d.values()   ile sadece değerleri yazdırabiliriz

for x in d:
    print(f"{x} : {d[x]}")           

    for x,y in d.items():               #ikisi de aynı sonucu verir 
    print(x,y)


'''

'''
numbers = [1,5,15,35,57,72]
total=0

for i in numbers:
    if(i%2==0):
        total += (i**2)

print(total)
'''


'''
products=["iphone 8","iphone X","iphone XR","samsung S10"]


for x in products:
    print(x[1])



for x in products:
   print( x.lower().strip().find("iphone"))

    #ürünlerin hangilerinde iphone geçiyor diye sorgulamak için 

'''



'''
product=[
    {"name":"iphone 8",
     "price": "4000"
     },

    {"name":"iphone 8 plus",
     "price": "5000"
     },

     {"name":"iphone X",
     "price": "6000"
     },

     {"name":"iphone XR",
     "price": "7000"
     },

     {"name":"iphone 11",
     "price": "8000"
     },
]

'''


'''
for i in product:
    for x in i:
        print(f"{x}: {i[x]}")
'''

'''
for i in product:
    for x,y in i.items():
        print(x,y)
'''

'''
for i in product:
    print(f"{i["name"]}: {i["price"]} TL")
'''


'''
total = 0 
for x in product:
    total+= int(x["price"])
print(f"Total value of products : {total} TL")
'''

'''
for x in product:
    if( int(x["price"]) <= 6000):
        print(f"{ x["name"] } : { x["price"] } ")
'''

'''
kelime=input("aramak istediğiniz ürün: ")
for x in product:
  if(  x["name"].find(kelime.lower()) > -1  ) :
    print(x["name"])
'''


#while döngüleri
'''
i=0
while(i<10) :
    print(i)
    i+=1
'''

'''
username=""
while not username:
    username =input("kullanıcı adınız: ")
'''
'''
sayilar =[4,6,9,10,35,57,39,125,244]

i=0

while(i<len(sayilar)):
    if(sayilar[i]%2==1):
        print(sayilar[i])
    i+=1
print("\n")

while sayilar:
    print(sayilar.pop())
'''


'''
i=0
adet =int(input("kaç adet ürün eklenecek: "))
urunler=[]
while(i<adet):
    urun=input("ürün adı: ")
    fiyat=input("fiyatı: ")
    urunler.append({
        "Ürün": urun,
        "Fiyat": fiyat
    })
    i+=1

print("\n")

for i in urunler:
    print(f"{i["Ürün"]} : {i["Fiyat"]} TL")
'''

#break continue

'''
isim ="Oğuzhan Bahçeci"

for i in isim:
    if(i=="z"):
        continue
    print(i)
'''


'''
i=0
total=0

while(i<=100):
    if(i%2==1):
        i+=1
        continue
    else:
        total+=i
        i+=1
print(total)
'''

#range() metotu 
'''
r = range(10)               #range(alt sınır,üst sınır,artış mik)

sonuc=list(r)
 
print(sonuc)
'''

'''for i in range(50,100,10):
    print(i)
'''



# enumarate

'''
markalar = ["opel","bmw","mercedes"]

obj1 = enumerate(markalar)

print(type(obj1))
print(list(obj1))


for index,value in enumerate(markalar,1):
    print(f"{index}-{value}")
'''


#zip

'''
liste1 = [1,2,3,4,5]
liste2 = ['a','b','c','d','e','f']
liste3 = [100,200,300,400,500]


print(list(zip(liste1,liste2,liste3)))

for item in zip(liste1,liste2):
    print(item)

for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c)
'''


