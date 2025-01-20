
#open( )methodu ile açılır
'''
f=open("msg.txt","r")
print(f)


print(f.read())

print(f.read())     #bütün dosyayı okuduktan sonra okuyacak bir şey kalmaz 

f.seek(0)           #cursorun konumunu ayarlar 
print(f.read())


f.seek(0)
print(f.readline())         #satır satır okuma yapar
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())


f.seek(0)
satirlar=f.readlines()              #satırları okur liste haline getirir
print(satirlar)


f.close()               #dosyayı kapatır


'''

#with metodu

'''
try:
    with open("msg.txt","r",encoding="utf-8") as file:
     #print(file.read(10))        #belirtilen yere kadar okur
     #print(file.tell())  #cursorun konumunu söyler
      for i in file:
          print(i, end="")

    #print(file.read())      #sadece with içindeyken işler dışına çıkınca kapanır
except FileNotFoundError as e:
   print("Dosya okuma hatası",e)
finally:
   print("Dosya kapandı")

   '''





#yazma işlemleri

'''
        #yazma işleminde dosyanın içeriği sıfırlanır sıfırdan yazmaya başlar
with open("msg1.txt","w",encoding="utf-8") as file:
    file.write("Sadık Turan\n")
    file.write("Ali Turan \n")
    print(file.tell())

with open("msg1.txt","r",encoding="utf-8") as file:
    print(file.read())  
    
'''

#dosyaya ekleme yapma appending
'''
with open("msg1.txt","a",encoding="utf-8") as file:
    file.write("Mustafa Turan\n")

with open("msg1.txt","r",encoding="utf-8") as file:
    print(file.read(),end="")
'''


# r+ modu 
'''
with open("msg.txt","r+",encoding="utf-8") as file:
    file.read()
    file.write("yeni satır")

'''


'''
with open("markalar.txt", "w", encoding="utf-8") as file:
    markalar = ["opel", "mazda", "mercedes"]
    j = 1
    for i in markalar:
        file.write(f"{j}-{i}\n")
        j += 1

with open("markalar.txt", "a", encoding="utf-8") as file:
    file.write(f"{j}-Bmw\n")

with open("markalar.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()  
    lines[0] = "1-Toyota\n"  
    file.seek(0)  
    file.writelines(lines)  
    file.seek(0)  
    print(file.read())
'''







     