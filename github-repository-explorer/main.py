import requests
import json
from datetime import datetime

url = 'https://api.github.com/search/repositories'

def sort(): # СОРТИРОВКА по языку программирования
    quantity = int(input('Количество страниц с репозиториями: '))
    
    name = input('\nСортировать по Названию: ')
    
    language = input('\nСортировать по ЯП: ')
    
    url = f"https://api.github.com/search/repositories?q={name}+language:{language}"
    
    response = requests.get(
        url, 
        timeout=10,
        params={'per_page': quantity}
        )
    response.raise_for_status()

    history = response.json()
    
    data = history['items']
    
    for number, j in enumerate(data, start=1):
        print(f'\n{number}. \n| Название: {j['full_name']}\n')
        print(f'| Описание: {j['description']}')
        print(f'| ЯП: {j['language']}')
        print(f'| Звёзды: {j['stargazers_count']}')
        print(f'| Форки: {j['forks_count']}')
        print(f'| Дата создания: {j['created_at']}')
        print(f'| Просмотрено: {j['watchers']}\n')
        print(f'| Ссылка: {j['html_url']}')

def save_repositories(): # СОХРАНЯЕТ РЕПОЗИТОРИИ в файл
    try:
        history = load_search_history()

        if not history:
            print('\nИстория запросов пуста!')
            return

        print('\nИстория запросов:')

        for number, entry in enumerate(history, start=1):
            print(f'{number}. Запрос: {entry["query"]}')
            print(f'Дата: {entry["searched_at"]}\n')

        choice = int(input('Выберите номер запроса: '))

        selected_history = history[choice - 1]

        query = selected_history['query']

        repositories = search_repositories(query) # передаётся query, поэтому внутри функции уже записывается в params и делает запрос на сервер

        repo_choice = int(input('Выберите номер репозитория: '))

        selected_repository = repositories[repo_choice - 1]

        repository_data = get_repository_details(selected_repository)
        
        try:    
            with open('repositories.json', 'r', encoding='utf-8') as file:
                    data = json.load(file)
        
        except (json.JSONDecodeError, FileNotFoundError):
            print('Файл json был повреждён')
            
            data = []
        
        if type(data) is dict:
            data = [data]
        
        data.append(repository_data)
            
        with open('repositories.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        print('\nРепозиторий сохранён!')

    except ValueError:
        print('Нужно ввести целое число')

def delete_search_history(): # УДАЛЯЕТ отдельную ИСТОРИЮ или же всю историю запросов
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

def old_search_history(): # ПРОСМОТР СТАРОЙ истории запросов
    try:
        history = load_search_history()

        if not history:
            print('История поиска пуста')
            
            return # останавливаем функцию, т.к. при not history, функция продолжвет выполнятся дальше
        
        show_search_history()
        
        choice = int(input('Номер запроса: '))
        
        if 1 <= choice <= len(history):
            selected = history[choice - 1]
            
            query = selected['query']
            
            search_repositories(query)
                
    except ValueError:
        print('Нужно ввести целое число')

def show_search_history(): # ПОКАЗ всей ИСТОРИИ запросов
    history = load_search_history()

    if not history:
        print('История поиска пуста')
        return

    print('\nИстория поиска:')

    for number, entry in enumerate(history, start=1):
        print(f'{number}. Запрос: {entry["query"]}')
        print(f'Дата: {entry["searched_at"]}')

def load_search_history(): # ЗАГРУЖАЕТ ИСТОРИЮ запросов из файла json
    try:
        with open('search_history.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        return False # возвращаем false, чтобы понимать, что функция сработала неправильно

    except (json.JSONDecodeError, OSError) as error:
        print(f'Не удалось прочитать историю: {error}')

def save_search_history(query): # СОХРАНЯЕТ ИСТОРИЮ запросов в json файле
    try:
        with open('search_history.json', 'r', encoding='utf-8') as file:
            history = json.load(file)

    except FileNotFoundError:
        history = [] # если json файл не найден, мы создаём переменную с пустым список, что потом не было ошибок при добавлении данных в переменную history

    except json.JSONDecodeError:
        print('\nФайл истории повреждён')
        
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

def search_repositories(query=None): # ПОИСК репозиториев
    if query is None:
        query = input('Поиск репозиториев: ').strip() # .strip() очищает ответ пользователя от пробелов, чтобы строка не была пустой

        if not query:
            print('Поисковый запрос пуст')
            return

    try:
        pages = int(input('Количество страниц с репозиториями: '))
        
        response = requests.get(
            url,
            timeout=3,
            params={'q': query, 
                    'per_page': pages}
        )

        print(response.status_code)

        response.raise_for_status()

        data = response.json()
        repositories = data['items']

        if not repositories:
            print('Репозитории не найдены')
            return
        
        # передаём параметры в функцию для сохранения в файл.json
        save_search_history(query)

        for number, rep in enumerate(repositories, start=1):
            print(number, '|', f'Название: {rep["full_name"]}')
            print(f'Язык: {rep["language"]}')
            print(f'Описание: {rep["description"]}\n')

        return repositories # возвращаем repositories, чтобы использовать его за пределами функции

    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')

    except (ValueError, KeyError) as e:
        print(f'Ошибка ответа: {e}')

def get_repository_details(repository):# ПОКАЗЫВАЕТ ПОДРОБНУЮ ИНФОРМАЦИЮ про репозиториев
    full_name = repository['full_name']
    
    url = f'https://api.github.com/repos/{full_name}'

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

        return repository_data

    except requests.exceptions.HTTPError as e:
        print(f'Ошибка HTTPError: {e}')

    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')

    except requests.exceptions.HTTPError as e:
        print(f'Ошибка HTTPError: {e}')

    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')

def show_repositories(repositories): # ВЫБИРАЕМ репозиторий для показа подробной инфы
    try:
        choice = int(input('Выбери номер репозитория: '))

        if 1 <= choice <= len(repositories): # если choice больше/равно 1 и, если choice больше/равно длине repositories
            selected = repositories[choice - 1]

            get_repository_details(selected)
        else:
            print('Такого номера нет')
    
    except ValueError:
        print('Нужно ввести целое число')

def menu(): # МЕНЮ
    while True:
        choice = input('\n\t1. Поиск репозиториев\n\t'
                       '2. Сохранение репозиториев\n\t'
                       '3. Фильтрация по Параметрам\n'
                       '\n'
                        '\t4. Показать историю\n\t'
                      '5. Повторить поиск из истории\n\t'
                      '6. Удаление поиска из истории\n\t'
                       '\n7. Выход\n\n')

        if choice == '1':
            repositories = search_repositories()

            show_repositories(repositories)
        
        elif choice == '2':
            save_repositories()

        elif choice == '3':            
            sort()
        
        elif choice == '4':
            show_search_history()
        
        elif choice == '5':
            old_search_history()

        elif choice == '6':
            delete_search_history()
            
        elif choice == '7':
            break

        else:
            print('Неизвестная команда')

if __name__ == '__main__': # Файл запускается напрямую. Можно добавить if
    menu()