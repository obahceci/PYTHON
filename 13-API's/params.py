
#query string ile filtreleme

#url?key1=value1&key2=value2  formatıyla filtreleme

import requests

# response=requests.get("https://jsonplaceholder.typicode.com/todos?completed=true&userId=1")

response=requests.get("https://jsonplaceholder.typicode.com/todos",params={
    "userId":1,
    "completed":"true" 
})


liste=response.json()       #direkt olarak json formatında alır

print(liste)



