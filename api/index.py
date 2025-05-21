import json
import os

def handle_request(name):
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    marks = []
    
    for n in name:
        for row in data:
            if row["name"] == n:
                marks.append(row["marks"])

    
    return { "marks" : marks }