
import json

def kayit(urunAdi,fiyat,satistami,kategori):
    hesap=[]
    
    hesap={
        "urunAdi":urunAdi,
        "Fiyat":fiyat,
        "Satista mi": satistami,
        "Kategori":kategori
    }

    with open("Urunler.json","w")as file:
        json.dump(hesap,file,ensure_ascii=False,indent=2)
    
def oku():
    with open("Urunler.json","r") as file:
       sonuc=json.load(file)
       print(sonuc)
       





kayit("elma",12,True,"Meyve")

oku()


