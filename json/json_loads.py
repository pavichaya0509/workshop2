import json

json_string = '{"name": "jim & min", "age": 21, "city": "chonburi"}'

python_dict = json.loads(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])