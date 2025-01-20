

import db

def urunEkle(name,price):
    db.products.append({
        "id":len(db.products)+1,
        "name": name,
        "price" :price
    }) 

def urunGuncelle(id,name,price):
    for urun in db.products:
        if urun["id"]==id:
            urun["name"]=name
            urun["price"]=price
        

def urunGetir():
    for urun in db.products:
        print(f" ID:{urun["id"]}  NAME:{urun["name"]}  PRICE:{urun["price"]}\n")
    print("\n")
    