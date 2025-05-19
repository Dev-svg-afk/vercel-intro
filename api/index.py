import json
import os

def get_file():
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def handle_request(name):
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    a = data[0]["marks"]
    b = data[0]["marks"]
    return { "marks" : [a,b] }
