import json

with open('code/files/people.json') as f:
    d = json.load(f)
    print(d["people"][1]["age"])
