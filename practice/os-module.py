import os

user = input('Введите путь к файлу: ')
if os.path.exists(user):
    print('Указанный путь есть!')
else:
    print('Нету такого')
