from typing import Union
from fastapi import FastAPI
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import unittest, requests

#USE VENV ( shift+ctrl+P => interpreter)
#Uvicorn to run local host using uvicorn main:app --reload

app = FastAPI()
client = MongoClient("mongodb://root:example@localhost:27017")
db = client["auto_products"]
collection = db["auto"]


@app.get("/")
def read_root():
    return {"Avaliable": "Commands",
            "/getSingleProdcut/{product_id}":"Gets one product",
            "/getAll": "Gets every product",
            "/addNew/{product_id}/{name}/{price}/{quantity}/{description}":"makes new entry",
            "/deleteOne/{product_id}": "Removes specific product",
            "/startsWith/{letter}": "Gets products that start with letter",
            "/panginate/{start_id}/{end_id}": "Gets range of product",
            "/convert/{product_id}": "Coverts currency from $ to Euro"
            }


@app.get("/getSingleProduct/{product_id}")
def getSingleProduct(product_id: str, q: Union[str, None] = None):

    # Query the product
    product = collection.find_one({"Product ID": product_id})

    # Convert BSON to JSON correctly
    return json.loads(dumps(product))



@app.get("/getAll")
def getAll():
    results = dumps(collection.find({}))
    print(results)

    return json.loads(results)


@app.get("/addNew/{product_id}/{name}/{price}/{quantity}/{description}")
def addNew(product_id:str, name:str, price:float, quantity:int, description:str):
    new_product = {
        "Product ID": product_id,
        "Name": name,
        "Price": price,
        "Quantity": quantity,
        "Description": description
    }
    collection.insert_one(new_product)

    return {"New product added": str(new_product)}


@app.get("/deleteOne/{product_id}")
def deleteOne(product_id: str):

    collection.delete_one({"Product ID": product_id})

    return {"Successfully Deleted" : product_id}
    


@app.get("/startsWith/{letter}")
def startsWith(letter: str):

    products = dumps(collection.find({"Name": {"$regex": f"^{letter}", "$options": "i"}}))

    return json.loads(products)

@app.get("/panginate/{start_id}/{end_id}")
def paginate(start_id: str, end_id: str):

    products = dumps(collection.find({"Product ID": {"$gte": start_id, "$lte": end_id}}))

    return json.loads(products)


@app.get("/convert/{product_id}")
def convert(product_id: str, price:float):
    product = collection.find_one({"Product ID": product_id, "Price:": price})
    api = "fxr_live_8ee9857d6b38492ea6c451478161ab7c2ceb"
    url = requests.get("https://api.fxratesapi.com/latest?currencies=EUR&base=USD&amount={price}")
    


    # Convert BSON to JSON correctly
    return json.loads(dumps(product))
