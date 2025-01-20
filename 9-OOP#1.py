'''
class Person:
    pass

ogrenci1=Person()

print(ogrenci1)

'''


# __init__ method

'''
class Product:
    def __init__(self,_name,_price,_isActive):
        self.name=_name
        self.price=_price
        self.isActive= _isActive
        print("Product nesnesi üretildi")


p=Product("Iphone 16",85000,True)
print(p.name,p.price,p.isActive)

'''


#uygulama


'''
class Comment:
    def __init__(self, username, text, likes, dislikes):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

a = int(input("How many comments do you want to enter? "))

person = []

for i in range(a):
    username = input("Username: ")
    text = input("Comment: ")
    likes = int(input("Likes: "))
    dislikes = int(input("Dislikes: "))
    person.append(Comment(username, text, likes, dislikes))


for comment in person:
    print(f"\n{comment.username}: {comment.text}\nLikes: {comment.likes} \tDislikes: {comment.dislikes}\n")
'''


#INSTANCE METHOD
'''
class Person:
    def __init__(self,name,surname,year):
        self.name=name 
        self.surname=surname
        self.year=year
    
    def intro(self):
        
        return f"Benim adım {self.name} {self.surname}"

    def age(self):
        import datetime
        current=datetime.datetime.now().year
        
        return f"{current-self.year} Yaşındayım"




p1=Person("Sadık","Turan",1983)
print(p1.intro(),p1.age())

p2=Person("Sena","Turan",1996)
print(p2.intro(),p2.age())

'''



'''
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money  
        return f"Deposit successful. New balance: {self.balance:.2f}"

    def withdraw(self, money):
        if money > self.balance:
            return "Insufficient funds for withdrawal."
        self.balance -= money  
        return f"Withdrawal successful. New balance: {self.balance:.2f}"


hesap = BankAccount("Sadık Turan")


print(f"Account owner: {hesap.owner}")


print(hesap.deposit(100))  
print(hesap.withdraw(50))  
print(hesap.withdraw(100))  

'''

#CLASS ATTRIBUTES

'''
class Users:
    active_users=0

    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

        Users.active_users +=1
        
    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        Users.active_users -=1
        return f"{self.full_name()} uygulamadan çıktı"

print(Users.active_users)

a=Users("a","b",2)
b=Users("e","f",2)
c=Users("v","y",2)

print(Users.active_users)
c.logout()

print(Users.active_users)

'''



#CLASS METHODS


'''
class Users:
    active_users=0

    @classmethod
    def display_acvtive_users(cls):
        return f"{Users.active_users} tane aktif kullanıcı vardır"

    @classmethod
    def from_string(cls,data_str):
        first,last,age=data_str.split(" ")
        return cls(first,last,age)

    def __init__(self,first,last,age):
       
        self.first=first
        self.last=last
        self.age=age

        Users.active_users +=1
        
    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        Users.active_users -=1
        return f"{self.full_name()} uygulamadan çıktı"

print(Users.display_acvtive_users())

a=Users("a","b",2)
b=Users("e","f",2)
c=Users("v","y",2)

d=Users.from_string("Ali Korkmaz 20")
print(d.first)

print(Users.display_acvtive_users())

print(c.logout())

print(Users.display_acvtive_users())
'''


#ornek

'''
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices 
        self.answer=answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("Seçenek disi")
        elif(answer!= self.answer):
            return False
        else:
            return True


q1 = Question("en iyi prog dili ?",["pyhton","c#","java","dart"],"python")

print(q1.text)
print(q1.choices)

sonuc = input("Cevabınız: ")

if(q1.checkAnswer(sonuc)==True):
    print("Doğru bildiniz")
else:
    print("Yanlış bildiniz")
'''
