db = {
    "users": {
        "sadikturan": {
            "firstName":"Sadık",
            "lastName":"Turan"
        },
        "cinarturan": {
            "firstName":"Çınar",
            "lastName":"Turan"
        }
    },
    "products": {
        "1": {
            "productName":"IPhone 8",
            "price":5000
        },
        "2": {
            "productName":"IPhone 12",
            "price":8000
        }
    }
}

import json

with open("db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)

with open("db.json") as file:
    db = json.load(file)



db["products"].update({
    "3": {
            "productName":"IPhone 11",
            "price":7600
        }
})

db["users"].update({
    "senaturan": {
            "firstName":"Sena",
            "lastName":"Turan"
        }
})

with open("db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)

