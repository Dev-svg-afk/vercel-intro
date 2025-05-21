import json
import os

def handle_request(name):
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    if not name:
        marks = []
    else:
        for n in name:
            marks.append(row["marks"] for row in data if row["name"] == n)
    return { "marks" : marks }
