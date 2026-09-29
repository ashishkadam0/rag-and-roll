import json

person = {"name":"Komal", "age":25}
print(f"Name: {person['name']}, Age: {person['age']}")
json_string = json.dumps(person)
print(json_string)