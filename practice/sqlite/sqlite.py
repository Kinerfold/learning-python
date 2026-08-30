import sqlite3

 # подключение к бд (если нету, то будет создана)
con = sqlite3.connect('test.db')

# Для выполнения выражений SQL и получения данных из БД, необходимо создать курсор
cursor = con.cursor() 

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Создаем таблицу people CREATE TABLE


# Можно добавить IF NOT EXISTS, если её ещё нет
# cursor.execute("""CREATE TABLE people
#                (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT,
#                age INTEGER)
#                """)

# INTEGER PRIMARY KEY идентифицирует строку в таблице. То есть у нас не может быть таблице people более одной строки, где в столбце id было бы одно и то же значение.
# AUTOINCREMENT позволяет указать, что значение столбца будет автоматически увеличиваться при добавлении новой строки.

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# CREATE TABLE users
# (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     email TEXT UNIQUE
# );


# Ограничение UNIQUE указывает, что столбец может хранить только уникальные значения.



# CREATE TABLE users
# (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     email TEXT,
#     UNIQUE (name, email)
# );


# Ограничение для определенных столбцов: name и email


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# CREATE TABLE users
# (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     age INTEGER
# );


# NULL - отсутствие формального значения
# NOT NULL - столбец обязательно должен иметь какое то значение


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# CREATE TABLE users
# (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER DEFAULT 18
# );


# DEFAULT - ограничение. значение устанавливает для столбца изначальный вид. В данном случае - 18


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# CREATE TABLE users
# (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL CHECK(name !=''),
#     age INTEGER NOT NULL CHECK(age >0 AND age < 100)
# );


# CHECK - ограничение. задает ограничение для диапазона значений, которые могут храниться в столбце.
# AND - ключ. слово. соединяет ограничения

# Есть ещё OR - это ИЛИ в SQLite



# CHECK(category IN ('electronics', 'clothes', 'food'))

# IN - это как 'находится среди этих значений'


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# CREATE TABLE users
# (
#     id INTEGER,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     age INTEGER NOT NULL,
#     CONSTRAINT users_pk PRIMARY KEY(id),
#     CONSTRAINT user_email_uq UNIQUE(email),
#     CONSTRAINT user_age_chk CHECK(age >0 AND age < 100)
# );


# CONSTRAINT - оператор, задающий имена для ограничений

# Ограничение для PRIMARY KEY называется users_pk, для UNIQUE - user_phone_uq, а для CHECK - user_age_chk.

# Впоследствии через эти имена мы сможем управлять ограничениями - удалять или изменять их.

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Добавляем строку в таблицу people INSERT INTO (делать ПОСЛЕ создания таблицы)
# name = TOM, age = 38

# Выражение INSERT добавляет что то. Для закрытия транзакции используем commit()
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
# -----------------------------------------------------------------------

# Для удаления в SQL выполняется команда DЕLETE


# Удаляем "Bob", т.к name=?
# cursor.execute("DELETE FROM people WHERE name=?", ("Bob",))
# con.commit()

# cursor.execute("SELECT * FROM people")
# print(cursor.fetchall())



