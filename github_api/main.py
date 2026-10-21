import requests

url = 'https://api.github.com/search/repositories'

query = input('Поиск: ')

try:
    response = requests.get(
        url,
        timeout=3,
        params={'q': query,
                'per_page': 5}
    )

    print(response.status_code)

    response.raise_for_status()

    data = response.json()

    repositories = data['items']

    if repositories:
        for rep in repositories:
            for number, rep in enumerate(repositories, start=1):
                print(number, rep['full_name'])
                print(number, rep['language'])
                print(number, rep['description'])
                print(number, rep['stargazers_count'])
                print(number, rep['html_url'])
                
                choice = int(input('Выбери номер репозитория: '))
                
                if choice:
                    selected = repositories[choice - 1]
                    
                    print('Репозиторий: ', selected)
                    
                elif 1 <= choice <= len(repositories):
                    print('Такого номера нет')
    else:
        print('Репозитории отсутствуют')

except requests.exceptions.HTTPError as e:
    print(f'Ошибка HTTPError: {e}')

except ValueError:
    print('Нужно ввести целое число')