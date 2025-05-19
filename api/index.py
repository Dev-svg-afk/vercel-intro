import json
import os

def get_file():
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def handle_request(names):
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    a = data[names[0]]
    b = data[names[1]]
    return { "marks" : [a,b] }
