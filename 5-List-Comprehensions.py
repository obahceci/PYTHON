

'''
sayilar =[i for i in range(10)]             #bu şekilde listemizi initilaize edebiliriz 
print(sayilar)

sayilar = [i**2 for i in range(10)]         #istersek değişkenimizin bizim istediğimiz sonuçlarıyla liste çıkartabiliriz
print(sayilar)

'''


'''
liste=[10,4,7,9,70]
sayilar = [i*2 for i in liste]
sonuc =[str(sayi) for sayi in liste]
print(sayilar)
print(sonuc)
'''


'''
isim="Ahmet"

sonuc = [c.upper() for c in isim]
print(sonuc)
'''

'''
#koşullu ifadeler

sayilar=[1,5,8,9,15,44]                     #[expression for item in lise if koşul]
sonuc=[i for i in sayilar if i%2==0]
print(sonuc)

'''


'''
fiyatlar=[1000,3000,5000,0,4000]

vergi=[fiyat* 1.18 for fiyat in fiyatlar if fiyat>0 else]

print(vergi)
'''

'''
sonuc=[(x,y) for x in range(3) for y in range(3)]
print(sonuc)
'''




'''
isimler =["Ahmet","ali","Çınar","DeNiz"]
string="Hello 12345 World"
yillar=[1983,1999,2008,1956,1986]
dereceler=[20,5,15,-2,0,-6]

#1

#sonuc= [sayi for sayi in range(1,101) if sayi%12==0]
#print(sonuc)

#2

#x=[isim.lower()[::-1] for isim in isimler]      #[alt:üst:artış miktarı]        
#print(x)

#3
#y=[i for i in string if i.isdigit()]
#print(y)

#4

#import datetime
#n=datetime.datetime.now().year

#sonuc =[n-x for x in yillar]
#print(sonuc)

#5
#sonuc= [i if i>0 else " buzlanma tehlikesi" for i in dereceler]
#print(sonuc)


'''

