import shelve

FILENAME = 'movies.db'

user = input('Введите название фильма: ')
user2 = input('Введите жанр фильма: ')

with shelve.open(FILENAME) as file:
    file[user] = user2
    

with shelve.open(FILENAME) as file:
    print('\nВсе фильмы: ', file[user], '-', file[user2])
