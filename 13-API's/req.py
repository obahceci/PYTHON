
import requests
import json

response =requests.get("https://jsonplaceholder.typicode.com/todos",params={
    "userId":1,
    "completed":"false" 
})

#sonuc=response

#sonuc=response.status_code

#sonuc=response.headers

#sonuc=response.headers["Content-Type"]

sonuc=response.text   #str tipinde sonuc verir sorgulama yapamayız dict taypında olması lazımdır

todos=json.loads(response.text)  #json-str to dict fromatı  

for item in todos:
    
    print(item["title"])

#print(sonuc)





