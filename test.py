import requests
import json

url = "http://127.0.0.1:5000/processdata"
filepath = "sample_data.csv"
column_name = "score"

with open(filepath, "rb") as file:
    files = {"file": file}
    data = {"column_name": column_name}
    response = requests.post(url, files=files, data=data)

print(json.dumps(response.json(), indent=2))
