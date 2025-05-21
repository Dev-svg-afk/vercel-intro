from fastapi import FastAPI, Query
from typing import List
from api import index
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ["https://your-frontend-domain.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "CORS is working!"}

@app.get("/api")
def read_index(name: List[str] = Query(None)):
    return index.handle_request(name=name)