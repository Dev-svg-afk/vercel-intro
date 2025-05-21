import json
import os

def handle_request(name):
    file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    if not name:
        marks = []
    else:
        marks = [data[x]["marks"] for x in name]
    return { "marks" : [marks] }
