from fastapi import FastAPI
from pydantic import BaseModel
# from typing import Union
app = FastAPI()

@app.get("/")
def root_file():
    return {"Hello ": "World!"}

class Item(BaseModel):
    name:str
    price:float
    available:bool
    
@app.post("/items/")
def items(item:Item):
    return {"Message" : "Item posted", "item" : item}