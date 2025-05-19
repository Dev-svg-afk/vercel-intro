from fastapi import FastAPI, Query
from typing import List
from api import index

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "changed text!"}

@app.get("/api")
def read_index(names: List[str] = Query(None)):
    return index.handle_request(names=names)