import requests

respose = requests.get('https://jsonplaceholder.typicode.com/users/5')

print(respose.status_code)

payload = {'id': 5, 'name': 'Chelsey Dietrich'}

requests.get('https://jsonplaceholder.typicode.com/users/5',
             params=payload)

