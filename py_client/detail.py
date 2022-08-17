import requests


endpoint = "http://localhost:8000/api/products/2"

get_response = requests.get(
    endpoint, json={"content": "hi from request"})  # sent as data

print(get_response.json())
