import json

python_dict = {"name": "mind & mon", "age": 21, "city": "chonburi"}

json_string = json.dumps(python_dict)

print(json_string)
