import requests

url = 'https://api.github.com/search/repositories?q'

query = input('Поиск: ')

response = requests.get(
    url,
    timeout=3,
    params={'q': query}
)

response.raise_for_status()

data = response.json()

repository = data['items'][0]

print(repository['full_name'])
print(repository['stargazers_count'])
print(repository['url'])

