
import json
 
data = {
    "people": [
        {
            "name": "Donald Duck",
            "age": 40,
            "city": "Duckburg"
        },
        {
            "name": "Mickey Mouse",
            "age": 42,
            "city": "Mouseton"
        },
    ]
}

json_object = json.dumps(data, indent=4)
 
with open("people.json", "w") as outfile:
    outfile.write(json_object)
