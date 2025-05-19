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
    # a = data[name[0]]
    # b = data[name[1]]
    # return { "marks" : [a,b] }
    return { data[0]["name"] }
