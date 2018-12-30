import json

f = open('data.json', 'r')

data = json.load(f)
print("HELLO FROM load_data.py", data)