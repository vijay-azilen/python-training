import json

employee_data = {
    "name": "Vijay",
    "role": "Technical Project Leader",
}

json_string = json.dumps(employee_data)
print(json_string)