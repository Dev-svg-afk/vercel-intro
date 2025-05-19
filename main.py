from fastapi import FastAPI
from api import index

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "changed text!"}

@app.get("/api")
def read_index():
    index.handle_request()