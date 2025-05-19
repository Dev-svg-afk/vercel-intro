import json

def get_file():
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)
    print(data)

def handle_request(names):
    with open('q-vercel-python.json', 'r') as f:
        data = json.load(f)
        a = data[names[0]]
        b = data[names[1]]
        return { "marks" : [a,b]}
