from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

@app.get("/")
def test():
  client = MongoClient("172.19.0.3", 27017)
  db = client.dbsparta
  now = datetime.now()
  data = list(db.users.find({}))
  return {"time": now, "db": data}



