import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': "hvhvhj",
    'content': "jjjhhgb",
    'price': 56,
}
get_response = requests.put(endpoint, json=data)  # sent as data

print(get_response.json())
