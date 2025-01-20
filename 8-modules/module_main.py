'''
import module       #module içindeki verileri referansla kullanırız 

sonuc=module.sayi
sonuc=module.ogrenci["notlar"]
sonuc= module.topla(10,20)

print(sonuc)
'''

'''
import module as m          #kısaltma yapabiliriz

sonuc1=m.sayilar
print(sonuc1)

'''

'''
from module import ogrenci          #modulden istenilen veriyi kullanabiliriz
sonuc2 = ogrenci 
print(sonuc2)
'''


'''
from module import *         #module içindeki verileri direkt olarak kullanabiliriz
sonuc4=sayi
print(sonuc4)
'''
