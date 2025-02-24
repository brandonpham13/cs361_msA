# Basic Data Analysis Service

## Overview
This is a microservice that processes a .csv file and returns basic analysis for a specific column via REST API. The data returned contains the min, max, and average (given that all values in the column are numeric).

## Communication Contract
- **Endpoint:** `POST /processdata`
- **Request Format:** .csv file with headers. For example:
```csv
name,location,age,score
Brandon,Texas,30,89.0
Lianne,Washington,29,97.5
Moe,Florida,50,51
Stewie,California,19,2000
```
- **Response Format:** .json response
```json
{
  "column name": "score",
  "min": 51.0,
  "max": 2000.0,
  "mean": 559.375
}
```
- **Example Usage:**
```python
import requests
import json

url = "http://127.0.0.1:5000/processdata"
filepath = "sample_data.csv" # Replace this with the path to your .csv file
column_name = "score" # Replace this with the column you would like to retrieve data for

with open(filepath, "rb") as file:
    files = {"file": file}
    data = {"column_name": column_name}
    response = requests.post(url, files=files, data=data)

print(json.dumps(response.json(), indent=2))
```

## UML Diagram
![umldiagram](https://github.com/brandonpham13/cs361_msA/blob/main/images/microserviceA_uml.drawio.png)

## Notes
- If a selected column contains at least one non-numeric value, this error will be returned:
```
{
  "error": "Column 'score' must contain numeric values"
}
```

