from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

@app.get("/")
async def test():
  client = MongoClient("172.19.0.3", 27017)
  db = client.crawling
  now = datetime.now()
  return {"time": now, "collections": db.list_collection_names()}


@app.get("/collection/{collection_name}")
async def test(collection_name):
  client = MongoClient("172.19.0.3", 27017)
  db = client.crawling
  now = datetime.now()
  collection = db[collection_name]

  docs = list()
  for doc in collection.find():
    doc["_id"] = str(doc["_id"])
    docs.append(doc)

  return {"time": now, "data": docs}
