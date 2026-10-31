import requests
import json
from datetime import datetime

url = 'https://api.github.com/search/repositories'

def sort_history_repositories(data):
    try:
        if not data:
            print('\nИстория запросов пуста')
        
        sort = int(input('''Сортировать по:\n
                     | 1. Количеству звёзд\n
                     | 2. Названию\n
                     | 3. Количеству форков\n
                     '''))
        
        if sort == 1:
            choice = int(input('| 1. По возрастанию\n| 2. По убыванию\n'))
            
            if choice == 1:
                pass
            
            elif choice == 2:
                pass
        
        elif sort == 2:
            pass
    
    except ValueError:
        print('Нужно ввести целое число')

def save_repositories(repositories):
    try:
        repositories = load_search_history()

        if not repositories:
            print('Список репозиториев пуст')
            
            return
        
        try:
            with open('repositories.json', 'r', encoding='utf=8') as file:
                saved = json.load(file)
        
        except FileNotFoundError:
            saved = [] # создаётся пустой список, если нету файла
        
        if isinstance(saved, dict): # которая проверяет, относится ли объект (saved) к определённому типу данных (dict)
                saved = [saved] # если saved - словарь, то мы помещаем его внутрь списка
        
        for number, j in enumerate(repositories, start=1): # функция enumerate добавляет счётчик (start=) к объекту (repositories)
            print(f'{number}: {j['query']}')
        
        choice = int(input('Номер репозитория для сохранения в файл: '))

        if 1 <= choice <= len(repositories):
            selected = repositories[choice - 1]
            
            saved.append({
                'name': selected['query'],
                'searched_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
                        
            with open('repositories.json', 'w', encoding='utf-8') as file:
                json.dump(saved, file, ensure_ascii=False, indent=4)
                
                print('\tРепозиторий сохранён!\n')
    
    except FileNotFoundError:
        repositories = [] # если json файл не найден, мы создаём переменную с пустым список, что потом не было ошибок при добавлении данных в переменную history

    except json.JSONDecodeError:
        print('Файл repository.json повреждён')
        
        repositories = []

def delete_search_history(): # удаляет отдельную историю или же всю историю запросов
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

def old_search_history(): # просмотр СТАРОЙ истории запросов
    try:
        history = load_search_history()

        if not history:
            print('История поиска пуста')
            
            return # останавливаем функцию, т.к. при not history, функция продолжвет выполнятся дальше
        
        print(history)
        
        choice = int(input('Номер запроса: '))
        
        if 1 <= choice <= len(history):
            selected = history[choice - 1]
            
            query = selected['query']
            
            search_repositories(query)
                
    except ValueError:
        print('Нужно ввести целое число')

def show_search_history(): # показ всей истории запросов
    history = load_search_history()

    if not history:
        print('История поиска пуста')
        return

    print('\nИстория поиска:')

    for number, entry in enumerate(history, start=1):
        print(f'{number}. Запрос: {entry["query"]}')
        print(f'Дата: {entry["searched_at"]}')

def load_search_history(): # загружает историю запросов из файла json
    try:
        with open('search_history.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        return False # возвращаем false, чтобы понимать, что функция сработала неправильно

    except (json.JSONDecodeError, OSError) as error:
        print(f'Не удалось прочитать историю: {error}')

def save_search_history(query): # сохраняет историю запросов в json файле
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

def search_repositories(query=None): # поиск репозиториев
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

def get_repository_details(repository): # подробная информация репозиториев
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

def show_repositories(repositories): # показывает подробную информацию о выбранном репозитории
    try:
        choice = int(input('Выбери номер репозитория: '))

        if 1 <= choice <= len(repositories): # если choice больше/равно 1 и, если choice больше/равно длине repositories
            selected = repositories[choice - 1]

            get_repository_details(selected)
        else:
            print('Такого номера нет')
    
    except ValueError:
        print('Нужно ввести целое число')

def menu(): # консольное меню
    while True:
        choice = input('\n\t1. Поиск репозиториев\n\t'
                       '2. Сохранение репозиториев\n\t'
                       '\n'
                        '\t3. Показать историю\n\t'
                      '4. Повторить поиск из истории\n\t'
                      '5. Удаление поиска из истории\n\t'
                      '6. Вывод и сортировка репозиториев из истории запросов\n\t'
                       '\n7. Выход\n\n')

        if choice == '1':
            repositories = search_repositories()

            if repositories:
                show_repositories(repositories)
        
        elif choice == '2':
            repositories = load_search_history()
            
            if repositories:
                save_repositories(repositories)

        elif choice == '3':
            show_search_history()
        
        elif choice == '4':
            old_search_history()
        
        elif choice == '5':
            delete_search_history()

        elif choice == '6':
            data = load_search_history()
            
            if data:
                sort_history_repositories(data)

        elif choice == '7':
            break

        else:
            print('Неизвестная команда')

if __name__ == '__main__': # файл запускается напрямую. можно добавить if
    menu()