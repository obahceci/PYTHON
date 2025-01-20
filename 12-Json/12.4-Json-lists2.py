data={
    "sadikturan":{
        "firstName":"Sadık",
        "lastName":"Turan"
    },
    "cinarturan":{
        "firstName":"Cinar",
        "lastName":"Turan"
    }
}
import json

with open("users2.json","w")as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("users2.json","r")as file:
    users=json.load(file)

print(users)

print(users["sadikturan"])

users.update({
    "emelturan":
    {
        "firstName":"Emel",
        "lastName":"Turan"
    }
})

with open("users2.json","w")as file:
    json.dump(users,file,ensure_ascii=False,indent=2)

with open("users2.json","r")as file:
    users=json.load(file)
print(users)


#users.pop("Index")  ile veri de silebiliriz
