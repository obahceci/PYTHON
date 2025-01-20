import requests
import json


response=requests.post("https://jsonplaceholder.typicode.com/posts",data={
    "title":"deneme",
    "body":"deneme",
    "userId":1
    }
)

sonuc=response
#sonuc=response.text         #str tipinde
sonuc=response.json()          #dict tipinde 

print(sonuc)

