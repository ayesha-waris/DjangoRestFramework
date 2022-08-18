import requests


endpoint = "http://localhost:8000/api/products/"
headers = {'authorization': 'Bearer 3c8a67a8fa5a4977e5f9daa9713fc8f7415b7835'}

data = {
    'title': "macbook",
    'content': "M1",
    'ptice': 4546.6,
}
get_response = requests.post(endpoint, json=data, headers=headers)  # sent as data

print(get_response.json())
