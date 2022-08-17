import requests


# endpoint = 'http://httpbin.org/status/200/'
# endpoint = "http://httpbin.org"
endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint)
# get_response = requests.get(endpoint, params={"abc": 123}, json={"query":"hi from request"}) #sent as data

get_response = requests.post(
    endpoint, json={"content": "hi from request"})  # sent as data
# get_response = requests.get(endpoint, data = {'query': "hey there"}) #sent as form
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
