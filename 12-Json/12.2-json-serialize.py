
import json 

#uygulamada json stringi kullanmak için yaparız
'''
person={
    "firstName":"Oguzhan",
    "lastName":"Bahceci",
    "hobiler":["spor","sinema"],
     "age":37,
    "children":[ {
        "firstName":"Cinar",
        "age":3

        }
    ]
}

sonuc=json.dumps(person,ensure_ascii=False,indent=2)
print(sonuc)
'''


#dosyaya aktarmak istiyorsak    
person={
    "firstName":"Oguzhan",
    "lastName":"Bahceci",
    "hobiler":["spor","sinema"],
     "age":37,
    "children":[ {
        "firstName":"Cinar",
        "age":3

        }
    ]
}

with open("12-person.json","w")as file:
    json.dump(person,file,ensure_ascii=False,indent=2)

#serialize -------> dict yapısından str yapısına
