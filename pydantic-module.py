
from pydantic import BaseModel,EmailStr,field_validator
import json

class User(BaseModel):
    id: int
    name: str
    email: EmailStr                  #str tipinde email olduğunu gösteren özel tip

    @field_validator("id")
    def validate_id(cls,v):
        if v<0:
            raise ValueError(f"id cannot be negative: {v}")
        return v



'''
user = User(id=1, name="John Doe", email="john.doe@example.com")

print(user)
'''





'''
user_data={
    "id":2,
    "name":"Jane Doe",
    "email":"jane"                          #emailStr ile hata verir
}

user_model=User(**user_data)

print(user_model)

'''




'''

user=User(id=-2345,name="John Doe",email="john.doe@example.com")    #id negatif olduğu için hata verir

print(user)

'''










'''
user = User(id=1, name="John Doe", email="john.doe@example.com")

userJson=user.model_dump_json(indent=4)
print(userJson)                                 #sereliaze to jsonString



with open("user.json", "w") as file:
    file.write(user.model_dump_json(indent=4))      #sereliaze to json file

'''




'''
user = User(id=1, name="John Doe", email="john.doe@example.com")

with open("user.json", "r") as file:                # deserialize from JSON file
    json_data = json.load(file)
    loaded_user = User.model_validate(json_data)  # For Pydantic v2
    # OR use User.parse_obj(json_data)  # For older Pydantic v1

print(loaded_user)  # Will print the loaded user model
print(json_data)

#print(type(loaded_user))  # Will show it's a User instance

'''



'''
json_string = user.model_dump_json(indent=4)        # Deserialize from JSON string
print("JSON String:", json_string)

                                                    
loaded_user = User.model_validate_json(json_string)  # For Pydantic v2
print("\nDeserialized User:", loaded_user)
'''



