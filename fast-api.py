
from fastapi import FastAPI,Path,Query
from typing import Optional
from pydantic import BaseModel
import datetime 


app = FastAPI()     #api nesnesi oluşturur

#endpoint oluşturmamız lazım  /sth


#cmd de öncelikle dosyamızın olduğu yere gitmemiz gerekiyor
#uvicorn main:app --reload yazıp çalıştırıyoruz

'''
@app.get("/")          
def home():
    return {"Data":"Test"}            #fastapi veriyi json formatında döndürüyor

@app.get("/about")
def about():
    return {"Data":"About"}
'''



class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None



inventory={
  
}


#path parametresi ile item_id'yi alıyoruz

@app.get("/get_item/{item_id}")
def get_item(item_id:int=Path(description="The ID of the item to get",gt=0,lt=4)):      #gt=greater than 0, lt=less than 4
    return inventory[item_id]
 


#query parametresi ile name'i alıyoruz

@app.get("/get-by-name")
def get_item(name:Optional[str]=None):
    for item_id in inventory:
        if inventory[item_id].name==name:
            return inventory[item_id]
   
    return {"Error":"Item not found"}





@app.post("/create-item/{item_id}")

def create_item(item_id:int,item: Item ):
    if item_id in inventory:
        return {"Error":"Item already exists"}
    else:
        inventory[item_id]=item
        return inventory[item_id]











