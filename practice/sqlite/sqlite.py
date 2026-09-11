import sqlite3

 # подключение к бд (если нету, то будет создана)
# con = sqlite3.connect('test.db')

# Для выполнения выражений SQL и получения данных из БД, необходимо создать курсор
# cursor = con.cursor() 

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


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------



# Переименование таблицы

# Если таблица уже была ранее создана, и ее необходимо изменить, то для этого применяется команда ALTER TABLE


# ALTER TABLE users
# RENAME TO people


# Добавление нового столбца

# ALTER TABLE users
# ADD COLUMN email TEXT NOT NULL


# Переименование столбца


# ALTER TABLE users
# RENAME COLUMN email TO login


# Удаление столбца


# ALTER TABLE users
# DROP COLUMN login


# Удаление ТАБЛИЦЫ

# DROP TABLE IF EXISTS users
# CREATE TABLE users <- Удаляем таблицу, если существует и создаём новую


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Оператор DISTINCT выбирает уникальные значения (где нету одинаковых значений)


# SELECT DISTINCT company FROM products

# Если в нескольких строках  значение NULL, то оператор DISTINCT отберет из них только одну строку.


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Сортировка ORDER BY


# ORDER BY price - сортировка по цене

# SELECT * FROM products
# ORDER BY price


# ASC - по возрастанию. ASC означает ascending - по возрастанию
# ASC можно не писать, т.к ORDER BY уже его использует

# ELECT * FROM products
# ORDER BY price ASC


# DESC - по убыванию (descending). От большего к меньшему

# SELECT * FROM products
# ORDER BY price DESC


# SELECT name, price
# FROM products
# ORDER BY price DESC




# ORDER BY + WHERE

# Пример: нужны товары дороже 2000 рублей

# SELECT *
# FROM products
# WHERE price > 2000
# ORDER BY price


# Пример:

# SELECT *
# FROM products
# WHERE price > 2000
# ORDER BY price DESC



# ORDER BY + LIMIT

# LIMIT ограничивает колво результатов, то есть будет выведено определённое колво результата

# SELECT *
# FROM products
# ORDER BY price DESC
# LIMIT 2

# Вывод: Monitor - 120000 | Keyboard - 5000



# ORDER BY с вычислением

# SELECT name, price, quantity
# FROM products
# ORDER BY price * quantity DESC


# SQLite вычисляет price * quantity и сортирует по этому значению

# Keyboard | 5000 × 10 = 50000
# Mouse | 1500 × 25 = 37500
# Monitor | 12000 × 5  = 60000

# Вывод: Monitor, Keyboard, Mouse

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Агрегатные функции: AVG, SUM, MIN, MAX, COUNT

# Пример:
# SELECT price FROM products | Вывод: 5000, 2000, 15000, 3000

# SELECT MAX(price) FROM products | Вывод: 15000



# 1. COUNT() - Посчитать

# SELECT COUNT(*) FROM products | Вывод: 4

# * считает строки


# COUNT(column) - Можно указать конкретный столбец

# SELECT COUNT(price) FROM products

# Он посчитает строки, где price не является NULL. Значения NULL игнорируются.



# COUNT(DISTINCT) - DISTINCT убирает повторяющиеся строки


# product   | company
# ----------|---------
# Keyboard  | Logitech
# Mouse     | Logitech
# Monitor   | Samsung
# Headset   | HyperX

# SELECT COUNT(company) FROM products | Вывод: 3 строки



# SUM() - складывает значения столбца


# quantity - 2, 5, 1, 3

# SELECT SUM(quantity) FROM products | Вывод: 11

# Можно сделать вот так: SELECT SUM(price * quantity) FROM products




# AVG() - вычисляет среднее значение


# price - 5000, 2000, 15000, 3000

# SELECT AVG(price) FROM products | Вывод: 6250 т.к (5000 + 2000 + 15000 + 3000) / 4 = 6250


# Можно использовать WHERE

# SELECT AVG(price) FROM products WHERE quantity > 1 | Сначала отфильтруй товары, где количество больше 1, а потом посчитай их среднюю цену.

# WHERE → какие строки берём
# AVG   → что с ними считаем




# MIN() и MAX() - находят самое минимальное и максимальное значение

# SELECT MIN(price) FROM products

# SELECT MAX(price) FROM products




# Можно использовать несколько функций сразу


# SELECT
#     COUNT(*) AS total_products,
#     SUM(quantity) AS total_quantity,
#     MIN(price) AS min_price,
#     MAX(price) AS max_price,
#     AVG(price) AS average_price
# FROM products



# AS - задаёт название результата


# Без AS:

# SELECT AVG(price) FROM products | Вывод: AVG(price)

# С AS:

# SELECT AVG(price) AS average_price FROM products | Вывод: average_price - 6250

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# HAVING в GROUP BY
# HAVING фильтрует группы


# WHERE  → фильтрует отдельные строки
# HAVING → фильтрует группы



# SELECT company, COUNT(*)
# FROM products
# GROUP BY company
# HAVING COUNT(*) > 2

# Что делает: показывает только те компании, у которых больше 2 товаров.



# Можно использовать с WHERE, GROUP BY, HAVING

# SELECT company, COUNT(*)
# FROM products
# WHERE price > 30000
# GROUP BY company   # Какие строки оставить? Выводит по company
# HAVING COUNT(*) >= 2


# 1. WHERE → убираем товары с price <= 30000
# 2. GROUP BY → группируем оставшиеся товары по company
# 3. COUNT(*) → считаем товары каждой компании
# 4. HAVING → оставляем компании, где товаров >= 2



# Отличия WHERE от HAVING в том, что WHERE фильтрует отдельные строки, а HAVING фильтрует группы.

# HAVING фильтрует группы ПОСЛЕ группировки

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Подзапросы в SQLite

# Подзапрос — это один SQL-запрос внутри другого SQL-запроса.


# SELECT *
# FROM products
# WHERE price > (SELECT AVG(price) FROM products)


# (SELECT AVG(price) FROM products) - Подзапрос находит среднюю цену

# Подзапрос становится таким:

# SELECT *
# FROM products
# WHERE price > 45000


# Подзапросы также может быть в SELECT


# Подзапрос = сначала получить какое-то значение/данные отдельным запросом, а потом использовать их в основном запросе.

# Сверху был Некоррелирующей подзапрос. Он просто находит среднюю цену и всё.



# Дальше будут Коррелирующие подзапросы


# SELECT name, age
# FROM users AS user
# WHERE age > (
#     SELECT AVG(age)
#     FROM users AS subuser
#     WHERE subuser.company_id = user.company_id
# )

# Подзапрос смотрит на company_id текущего пользователя. 

# Поэтому такой подзапрос называется коррелирующим — его результат зависит от текущей строки основного запроса.


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


