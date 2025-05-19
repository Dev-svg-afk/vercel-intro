from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "changed text!"}

@app.get("/api")
def read_api():
    return "Hello, world!"