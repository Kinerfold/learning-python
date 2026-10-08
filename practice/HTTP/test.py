import requests

url = 'https://jsonplaceholder.typicode.com/users'

params = {
    'id': 1
}

response = requests.get(
    url,
    params=params
)

data = response.json()

user_data = {
    'name': data[0]['name'],
    'email': data[0]['email'],
    'username': 'egor123'
}

response = requests.put(
    f'{url}/8',
    json=user_data
)

print(response.raise_for_status())

print(response.json())