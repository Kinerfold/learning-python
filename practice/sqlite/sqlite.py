import sqlite3

 # подключение к бд (если нету, то будет создана)
con = sqlite3.connect('test.db')

# Для выполнения выражений SQL и получения данных из БД, необходимо создать курсор
cursor = con.cursor() 

# -----------------------------------------------------------------------

# Создаем таблицу people CREATE TABLE

# cursor.execute("""CREATE TABLE people
#                (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT,
#                age INTEGER)
#                """)


# Добавляем строку в таблицу people INSERT INTO (делать ПОСЛЕ создания таблицы)
# name = TOM, age = 38

# Выражение INSERT открывает транзакцию. Для закрытия транзакции используем commit()
# cursor.execute("INSERT INTO people (name, age) VALUES ('TOM', 38)")


# Кортеж хранения данных
# bob = ('Bob', 42)

# cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", bob)


# Метод executemany() позволяет вставить набор строк
# people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]

# cursor.executemany("INSERT INTO people (name, age) VALUES (?, ?)", people)


# Получаем все данные из таблицы people
# cursor.execute("SELECT * FROM people")

# -----------------------------------------------------------------------

# fetchall() (возвращает список со всеми строками), 
# fetchmany() (возвращает указанное количество строк)
# fetchone() (возвращает одну в наборе строку)
# print(cursor.fetchall())


# Можно перебрать строки через цикл for
# for person in cursor:
#     print(f"{person[1]} - {person[2]}")


# cursor.execute("SELECT * FROM people")
# извлекаем первые 3 строки в полученном наборе
# print(cursor.fetchmany(3))


# извлекаем первые 3 строки в полученном наборе
# print(cursor.fetchmany(3))  # [(1, 'Tom', 38), (2, 'Bob', 42), (3, 'Sam', 28)]

# извлекаем следующие 3 строки в полученном наборе
# print(cursor.fetchmany(3))  # [(4, 'Alice', 33), (5, 'Kate', 25)]


# cursor.execute("SELECT * FROM people")
# извлекаем одну строку
# print(cursor.fetchone())  


# cursor.execute("SELECT name, age FROM people WHERE id=2")
# раскладываем кортеж на две переменных
# name, age = cursor.fetchone()
# print(f"Name: {name}    Age: {age}")    # Name: Bob   Age: 42

# -----------------------------------------------------------------------

# Для обновления в SQL выполняется команда UPDATE


# обновляем строки, где name = Tom
# cursor.execute("UPDATE people SET name ='Tomas' WHERE name='Tom'")

# con.commit()
# вариант с подстановками
# cursor.execute("UPDATE people SET name =? WHERE name=?", ("Tomas", "Tom"))


# cursor.execute("SELECT * FROM people")


# Выполняем cursor.execute
# con.commit()


# print(cursor.fetchall())


# -----------------------------------------------------------------------

# Для удаления в SQL выполняется команда DЕLETE


# Удаляем "Bob", т.к name=?
# cursor.execute("DELETE FROM people WHERE name=?", ("Bob",))
# con.commit()

# cursor.execute("SELECT * FROM people")
# print(cursor.fetchall())



