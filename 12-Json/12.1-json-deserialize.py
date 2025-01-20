
import json



#DESERİASLİZE

#json dosyasından ise 
'''
with open("12-person.json","r") as file:
    data= json.load(file)       #bu şekilde with bloğunun dışında erişebiliriz
                                #dışarıdan bir json dosyasından alınan bilgiler
print(data)
print(data["hobiler"])
'''




#json-string ise


data= '''
    {
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
    '''

#data=json.loads(data)           

#print(data)



#deserialize -------> str yapısından dict yapısına

