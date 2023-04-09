from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def test():
  return "running"

@app.get("/collections")
async def getCollectionList():
  client = MongoClient("172.19.0.3", 27017)
  db = client.crawling
  now = datetime.now()
  return {"time": now, "collections": db.list_collection_names()}


@app.get("/collection/{collection_name}")
async def getCollection(collection_name):
  client = MongoClient("172.19.0.3", 27017)
  db = client.crawling
  now = datetime.now()
  collection = db[collection_name]

  docs = list()
  for doc in collection.find():
    doc["_id"] = str(doc["_id"])
    docs.append(doc)

  return {"time": now, "data": docs}
