import requests
import json
from datetime import datetime

url = 'https://api.github.com/search/repositories'

def delete_search_history():    
    try:
        history = load_search_history()
        
        if not history:
            print('История поиска пуста')
            
            return

        print('\n\t1. Удаление отдельной записи\n\t2. Очистка всей истории\n\t')
        
        number = int(input('Выберите действие: '))
        
        if number == 1:
            print(history)
            
            choice = int(input('Номер записи: '))
            
            if choice:
                deleted = history.pop(choice - 1)
                
                with open('search_history.json', 'w', encoding='utf-8') as file:
                    json.dump(history, file, ensure_ascii=False, indent=4)
                
                print(f'Запрос: {deleted['query']} был удалён')
            else:
                print('Такого номера нету')
                    
        elif number == 2:
            history = [] # т.к. удаляем всю историю, создаём новую переменну и сохраняем данные через json.dump(history)
            
            with open('search_history.json', 'w', encoding='utf-8') as file:
                json.dump(history, file, ensure_ascii=False, indent=4)
                
            print('История поиска полностью очищена')
        
        else:
            print('Такого действия нету')
        
    except ValueError:
        print('Нужно ввести целое число')

def old_search_history():
    try:
        history = load_search_history()

        if not history:
            print('История поиска пуста')
            
            return # останавливаем функцию, т.к. при not history, функция продолжвет выполнятся дальше
        
        choice = int(input('Номер запроса: '))
        
        if 1 <= choice <= len(history):
            selected = history[choice - 1]
            
            query = selected['query']
            
            search_repositories(query)
                
    except ValueError:
        print('Нужно ввести целое число')

def show_search_history():
    history = load_search_history()

    if not history:
        print('История поиска пуста')
        return

    print('\nИстория поиска:')

    for number, entry in enumerate(history, start=1):
        print(f'{number}. Запрос: {entry["query"]}')
        print(f'Дата: {entry["searched_at"]}')

def load_search_history():
    try:
        with open('search_history.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        return False # возвращаем false, чтобы понимать, что функция сработала неправильно

    except (json.JSONDecodeError, OSError) as error:
        print(f'Не удалось прочитать историю: {error}')

def save_search_history(query):
    try:
        with open('search_history.json', 'r', encoding='utf-8') as file:
            history = json.load(file)

    except FileNotFoundError:
        history = [] # если json файл не найден, мы создаём переменную с пустым список, что потом не было ошибок при добавлении данных в переменную history

    except json.JSONDecodeError:
        print('Файл истории повреждён')
        
        history = []

    history.append({
        'query': query,
        'searched_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

    try:
        with open('search_history.json', 'w', encoding='utf-8') as file:
            json.dump(history, file, ensure_ascii=False, indent=4)

    except OSError as error:
        print(f'Не удалось сохранить историю: {error}')

def search_repositories(query=None):
    if query is None:
        query = input('Поиск репозиториев: ').strip()
        
        if not query:
            print('Поисковый запрос пуст')
            
            return

        save_search_history(query)
    
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

        if not repositories:
            print('Репозитории не найдены')
        
        for number, rep in enumerate(repositories, start=1): # подсчёт начинается с 1
            print(number, '|', f'Название: {rep['full_name']}')
            print(f'Язык: {rep['language']}')
            print(f'Описание: {rep['description']}')
            print(f'Звёзды: {rep['stargazers_count']}\n')
            print(f'Ссылка: {rep['html_url']}\n')
        
        return repositories              

    except requests.exceptions.RequestException as e: # хранит в себе сетевые ошибки, тайм-ауты и HTTP-ошибки
        print(f'Ошибка зарпоса: {e}')
    
    except (ValueError, KeyError) as e:
        print(f'Ошибка ответа: {e}')

def get_repository_details(repository):
    owner, repo_name = repository['full_name'].split('/')
    
    url = f'https://api.github.com/repos/{owner}/{repo_name}'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        repository_data = response.json()
        
        print('\nПодробная информация о репозитории:\n')
        print(f'Название: {repository_data["full_name"]}')
        print(f'Описание: {repository_data["description"]}')
        print(f'Язык: {repository_data["language"]}')
        print(f'Звёзды: {repository_data["stargazers_count"]}')
        print(f'Форки: {repository_data["forks_count"]}')
        print(f'Дата создания: {repository_data["created_at"]}\n')
        print(f'Ссылка: {repository_data["html_url"]}\n')

    except requests.exceptions.HTTPError as e:
        print(f'Ошибка HTTPError: {e}')

    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')

def show_repositories(repositories):
    try:
        choice = int(input('Выбери номер репозитория: '))

        if 1 <= choice <= len(repositories): # если choice больше/равно 1 и, если choice больше/равно длине repositories
            selected = repositories[choice - 1]

            get_repository_details(selected)
        else:
            print('Такого номера нет')
    
    except ValueError:
        print('Нужно ввести целое число')

def menu():
    while True:
        choice = input('\n\t1. Поиск репозиториев\n\t'
                        '2. Показать историю\n\t'
                      '3. Повторить поиск из истории\n\t'
                      '4. Удаление поиска из истории\n\t'
                       '\n5. Выход\n')

        if choice == '1':
            repositories = search_repositories()

            if repositories:
                show_repositories(repositories)

        elif choice == '2':
            show_search_history()
        
        elif choice == '3':
            old_search_history()
        
        elif choice == '4':
            delete_search_history()

        elif choice == '5':
            break

        else:
            print('Неизвестная команда')

if __name__ == '__main__': # файл запускается напрямую. можно добавить if
    menu()