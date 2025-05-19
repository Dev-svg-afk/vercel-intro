from fastapi import FastAPI, Query
from typing import List
from api import index

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "changed text!"}

@app.get("/api")
def read_index(name: List[str] = Query(...)):
    return index.handle_request(name=name)