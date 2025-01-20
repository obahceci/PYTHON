data=[
    {
        "userName":"sadikturan",
        "firstName":"Sadik",
        "lastName": "Turan"
    },
    {   
        "userName":"aturan",
        "firstName":"Arda",
        "lastName": "Turan"
    }
]
import json

with open("users.json","w")as file:
  json.dump(data,file,ensure_ascii=False,indent=2)


user={
    "userName":"selimturan",
    "firstName":"Selim",
    "lastName": "Turan"
  
}


with open("users.json","r")as file:
    users=json.load(file)


users.append(user)

with open("users.json","w")as file:
  json.dump(users,file,ensure_ascii=False,indent=2)