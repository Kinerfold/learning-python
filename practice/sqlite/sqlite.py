import sqlite3

con = sqlite3.connect('test.db') # подключение к бд (если нету, то будет создана)

cursor = con.cursor() # Для выполнения выражений SQL и получения данных из БД, необходимо создать курсор

# Создаем таблицу people
cursor.execute("""CREATE TABLE people
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER)
               """)

