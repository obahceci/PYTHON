

##################################################    LİSTELER

'''

msg ="python kursu oğuzhan bahçeci".split()
print(msg)

print(msg[0])

print(msg[0][0])


'''



'''
sayilar = [1,2,3,4,5]

print(sayilar[0])

'''



'''
isimler =["oğuz","ali","mustafa"]
print(isimler[1])
'''





'''
Ali= ["ali",22,1.78,]
Efe = ["efe",21,1.94]

ogrenci=[Ali,Efe]

print(ogrenci[0])

'''






'''
dil=["python","c#","java","javascript","react"]

#sonuc=dil
#sonuc = dil[0:2]
#sonuc = dil[2:]
#sonuc= dil[-1]
#sonuc =dil[-4:-1]

#dil[0]="html"
#sonuc=dil

#sonuc =len(dil)   #uzunluk 

#sonuc =dil + ["assembly","php"]


#print(sonuc)


#if "python" in dil:
    #print("elemanıdır")


del dil[0]
sonuc =dil 
print(sonuc)



'''


'''

isimler =["Ada","Yiğit","Hasan","Beril"]
yaslar = [1998,2000,1998,1987]

isimler = isimler + ["Cenk"]

isimler.insert(0,"Sena")

#sonuc = isimler
#sonuc.remove("Yiğit")



#print(isimler.index("Yiğit"))

#if "Beril" in isimler:
 #       print("evet")




#yaslar.sort()
#yaslar.reverse()
#print(yaslar)

#sonuc=yaslar.count(1998)
#print(sonuc)


markalar=[]
marka=input()
markalar.append(marka)
print(markalar)

'''


##################################################    TUPLE

'''
_tuple1 = (1,2,3)
_tuple2 = (3,4,5)
print(type(_tuple1)) 
print(_tuple1 + _tuple2)


_t= tuple([3,4,5])     #listeyti tuple yapmak 

##### tuple elemanlarını değiştiremeyiz
### tuple append olmaz 

'''

##################################################    Dictionary

'''
car ={
"brand" : "Ford",
"model" : "Mustang",
"year"  : 1964
}

print(car)
'''
#  key : value

'''
plakalar = {
    "Kocaeli": 41,
    "İstanbul": 34
}

plakalar["Rize"]=53
plakalar["İzmir"]=36

print(plakalar)

plakalar["İzmir"]=35
print(plakalar)
'''




'''
ogrenciler = {


    100:{
        "ad" : "Oğuzhan",
        "soyad":"Bahçeci",
        "tarih": "04.08.2003",
        "notlar" : [20,30,40]
    },
    
    101 :{
        "ad"  :  "Ali",
        "soyad": "Kabak",
        "tarih": "31.10.2002",
        "notlar" : [100,60,25]
    }

}

#sonuc=ogrenciler[100]
#sonuc=ogrenciler[100]["ad"]
sonuc=ogrenciler[100]["notlar"][0]
print(sonuc)

'''




'''
products={}



id = input("id: ")
name=input("name: ")
price=input("price: ")

products[id]={
    "name": name,
    "price": float(price)
}

print(f"ID: {id} , Name: {products[id]["name"]}, Price: {products[id]["price"]}")

'''





'''
opelobj = {
    "marka":"Opel",
    "model":" Corsa",
    "yil": 2020
}

#sonuc= opelobj["marka"] 
#sonuc=opelobj.get("marka")      #aynı sonucu verir

#print(sonuc)



#for x in opelobj:
#   print(opelobj[x])               #sözlükteki her malzemeyi yazdırır


#for x in opelobj.values():              #aynı sonuc 
#    print(x)


#for x,y in opelobj.items() :        # sırayla her elemanı ve malzemeleri yazdırır
#   print(x,y)


#sonuc=len(opelobj)              #eleman sayısı 
#print(sonuc)

#opelobj["renk"]="kirmizi"
#opelobj.pop("renk")                 #seçilmiş elemanı siler
#opelobj.popitem()                   #sonuncu elemanı siler



#obj=opelobj             #referans eklemiş oluruz
#obj["marka"]="Mazda"
#print(obj)
#print(opelobj)          #referans eklersek yapacağımız değişiklik asıl objeyi de etkiler 


#obj=opelobj.copy()      #kopyalama yapar 

'''

'''
player={}


id =input("Numara giriniz")
name= input("ad giriniz")
birth= input("doğum yılı")
team =input("takım giriniz")

player.update({
    id:{
        "name": name,
        "birth": birth,
         "team": team
    }
})

print(player[id])

'''


###############################################   SETS

'''
meyveler ={"elma","kiraz","kavun","üzüm"}

print(meyveler)   ## indekse dikkat edilmeksizin yazdırır   #setler indekslenemez

meyveler.add("karpuz")
meyveler.add["vişne","muz"] #eğer aynı elemandan eklenirse bir değişiklik olmaz 
meyveler.remove["karpuz"]
meyveler.clear
                                #   .union ile iki set birleştirilebilir 

'''




# LİSTELERDE REFERENCE TYPE OLDUĞU İÇİN YAPILAN DEĞİŞİKLİKLER İKİ DEĞİŞKENİ DE ETKİLER
# ÇÜNKÜ a=b işlemi iki dğeişkene de aynı adresi verir.



