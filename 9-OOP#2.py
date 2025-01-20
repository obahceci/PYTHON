#INHERITANCE

#temel sınıf ortaktır #alt sınıflarda gruba özeldir 


'''
class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("person nesnesi üretildi")

    def intro(self):
         print(self.name, self.surname, self.age)
    
class Student(Person):                 # person sınıfının alt sınıfıdır
    pass

class Teacher(Person):
    pass


p1=Person("Ahmet","Turan",20)
p1.intro()

s1=Student("Ali","Yılmaz",19)
s1.intro()

t1=Teacher("Mustafa","Okur",30)
t1.intro()

'''

#alt snıfların genişletilmesi 

'''


class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("\nperson nesnesi üretildi")

    def intro(self):
         print(self.name, self.surname, self.age)
    
class Student(Person):                 
    def __init__(self, name, surname, age,number):
        super().__init__(name, surname, age)
        print("student nesnesi türetildi")
        self.number=number

    def study(self):
        print(f"{self.number} numaralı öğrenci ders çalışıyor")
    
    def intro(self):
         print(self.name, self.surname, self.age,self.number)

class Teacher(Person):
    def __init__(self, name, surname, age,branch):
        super().__init__(name, surname, age)
        self.branch=branch
        print("teacher nesnesi türetildi")
    
    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} dersini veriyor")
    
    def intro(self):
         print(self.name, self.surname, self.age,self.branch)

p1=Person("Ahmet","Turan",20)
p1.intro()

s1=Student("Ali","Yılmaz",19,151220212164)
s1.intro(),
s1.study()

t1=Teacher("Mustafa","Okur",30,"English")
t1.intro()
t1.teach()

'''

#uygulama
'''
class User:
    active_users=0
    
    @classmethod
    def display_users(cls):
        return f"şu anda aktif {cls.active_users} kullanıcı var"

    def __init__(self,first,last):
        self.first=first
        self.last=last
        User.active_users+=1

    def fullname(self):
        return f"{self.first} {self.last}"
    

class Mod(User):
    active_mods=0
   
    @classmethod
    def display_mods(cls):
        return f"şu anda aktif{Mod.active_mods} moderatör var"

    def __init__(self, first, last,community):
        super().__init__(first, last)
        self.community=community
        Mod.active_mods+=1
    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan bir post sildi"
    def update_post(self):
        return f"{self.fullname()} {self.community} grubunda bir post güncelledi"


print("aktif kullanıcı: ",User.active_users)
print(f"aktif mod: {Mod.active_mods}")

u1= User("Ali","Korkmaz")
m1=Mod("Yağmur","Koru","Yazılım")

print("aktif kullanıcı: ",User.active_users)
print(f"aktif mod: {Mod.active_mods}")

print(m1.remove_post())
print(m1.update_post())

'''

#properties


'''
class Product:
    def __init__(self,name,price):
        self.name=name
        if price>=0 :
            self._price=price
        else: 
            raise ValueError("Fiyat sıfırdan küçük olamaz")
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value >=0:
            self._price=value
        else:
            raise ValueError("Fiyat için negatif değer atayamazsınız")

    

    #def set_price(self,value):
    #    if value >=0:
    #        self._price=value
    #    else:
    #        raise ValueError("Fiyat için negatif değer atayamazsınız")
            
    #def get_price(self):
    #    return print(f" Fiyat: {self._price}")
    
    

p=Product("iphone 12",9000)
#p.get_price()

print(p.price)
p.price=-9000
print(p.price)

#p.set_price(-800)
#p.get_price()

'''





