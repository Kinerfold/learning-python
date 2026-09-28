# ### Ограничения PostgreSQL

# **PRIMARY KEY** → уникальный идентификатор строки. Не может быть `NULL`.

# ```sql
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50)
# );
# ```

# **UNIQUE** → запрещает повторяющиеся значения.

# ```sql
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     email VARCHAR(100) UNIQUE
# );
# ```

# **NOT NULL** → поле обязательно должно иметь значение.

# ```sql
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL
# );
# ```

# **DEFAULT** → значение по умолчанию.

# ```sql
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     age INTEGER DEFAULT 18
# );
# ```

# **CHECK** → проверяет условие.

# ```sql
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     age INTEGER CHECK(age >= 18)
# );
# ```

# **CONSTRAINT** → позволяет дать ограничению имя.

# ```sql
# CREATE TABLE users (
#     id SERIAL,
#     age INTEGER,
#     CONSTRAINT age_check CHECK(age >= 18)
# );
# ```

# **Кратко:**

# ```text
# PRIMARY KEY → уникальный ID
# UNIQUE      → нельзя повторять
# NOT NULL    → нельзя NULL
# DEFAULT     → значение по умолчанию
# CHECK       → проверка условия
# CONSTRAINT  → имя ограничения
# ```


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Внешние ключи (FOREIGN KEY)

# Основная задача внешнего ключа: не дать создать ссылку на несуществующую запись.


### Внешние ключи PostgreSQL


# **FOREIGN KEY** → внешний ключ, связывает таблицы.

# ```sql
# CREATE TABLE orders (
#     id SERIAL PRIMARY KEY,
#     user_id INTEGER,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );
# ```

# **REFERENCES** → указывает, на какую таблицу и столбец ссылается внешний ключ.

# ```sql
# user_id INTEGER REFERENCES users(id)
# ```

# `user_id` ссылается на `users.id`.

# ---

# **ON DELETE CASCADE** → при удалении записи из главной таблицы удаляются связанные записи.

# ```sql
# FOREIGN KEY (user_id)
# REFERENCES users(id)
# ON DELETE CASCADE
# ```

# Удалили пользователя → его связанные заказы тоже удалились.

# ---

# **ON DELETE SET NULL** → при удалении записи внешний ключ становится `NULL`.

# ```sql
# FOREIGN KEY (user_id)
# REFERENCES users(id)
# ON DELETE SET NULL
# ```

# Удалили пользователя → `orders.user_id` становится `NULL`.

# ---

# **ON DELETE SET DEFAULT** → при удалении записи внешний ключ получает значение `DEFAULT`.

# ```sql
# user_id INTEGER DEFAULT 1,
# FOREIGN KEY (user_id)
# REFERENCES users(id)
# ON DELETE SET DEFAULT
# ```

# Удалили пользователя → `user_id` становится `1`.

# ---

# **ON UPDATE CASCADE** → при изменении ключа автоматически изменяются связанные внешние ключи.

# ```sql
# FOREIGN KEY (user_id)
# REFERENCES users(id)
# ON UPDATE CASCADE
# ```

# Изменили `users.id` → соответствующий `orders.user_id` тоже изменился.

# ---

# ### Кратко

# ```text
# FOREIGN KEY       → связывает таблицы
# REFERENCES        → указывает, с чем связать
# ON DELETE CASCADE → удалить связанные записи
# ON DELETE SET NULL → установить NULL
# ON DELETE SET DEFAULT → установить DEFAULT
# ON UPDATE CASCADE → изменить связанные ключи
# ```

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

### ALTER TABLE — изменение таблицы

# `ALTER TABLE` → изменить структуру существующей таблицы.

# ---

# **ADD** → добавить столбец или ограничение.

# ```sql
# ALTER TABLE users
# ADD phone VARCHAR(20);
# ```

# Добавили столбец `phone`.

# ---

# **DROP COLUMN** → удалить столбец.

# ```sql
# ALTER TABLE users
# DROP COLUMN phone;
# ```

# Удалили столбец `phone`.

# ---

# **ALTER COLUMN ... TYPE** → изменить тип столбца.

# ```sql
# ALTER TABLE users
# ALTER COLUMN age TYPE BIGINT;
# ```

# `age` был `INTEGER`, стал `BIGINT`.

# ---

# **SET NOT NULL** → добавить ограничение `NOT NULL`.

# ```sql
# ALTER TABLE users
# ALTER COLUMN name SET NOT NULL;
# ```

# Теперь `name` не может быть `NULL`.

# ---

# **DROP NOT NULL** → убрать ограничение `NOT NULL`.

# ```sql
# ALTER TABLE users
# ALTER COLUMN name DROP NOT NULL;
# ```

# Теперь `name` может быть `NULL`.

# ---

# **ADD CONSTRAINT** → добавить ограничение и дать ему имя.

# ```sql
# ALTER TABLE users
# ADD CONSTRAINT age_check CHECK (age >= 18);
# ```

# Добавили `CHECK`, который запрещает возраст меньше 18.

# ---

# **DROP CONSTRAINT** → удалить ограничение.

# ```sql
# ALTER TABLE users
# DROP CONSTRAINT age_check;
# ```

# Удалили ограничение `age_check`.

# ---

# **RENAME COLUMN ... TO** → переименовать столбец.

# ```sql
# ALTER TABLE users
# RENAME COLUMN name TO username;
# ```

# `name` → `username`.

# ---

# **RENAME TO** → переименовать таблицу.

# ```sql
# ALTER TABLE users
# RENAME TO customers;
# ```

# `users` → `customers`.

# ---

# ### Кратко

# ```text
# ALTER TABLE                  → изменить таблицу

# ADD                          → добавить
# DROP COLUMN                  → удалить столбец
# ALTER COLUMN ... TYPE        → изменить тип
# SET NOT NULL                 → добавить NOT NULL
# DROP NOT NULL                → убрать NOT NULL
# ADD CONSTRAINT               → добавить ограничение
# DROP CONSTRAINT              → удалить ограничение
# RENAME COLUMN ... TO         → переименовать столбец
# RENAME TO                    → переименовать таблицу
# ```

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

### UPDATE — изменение существующих данных

# `UPDATE` → изменяет данные в уже существующих строках.

# **Базовый синтаксис:**

# ```sql
# UPDATE таблица
# SET столбец = значение
# WHERE условие;
# ```

# ---

# **Изменить одно значение:**

# ```sql
# UPDATE users
# SET age = 25
# WHERE name = 'Алексей';
# ```

# Изменит `age` только у Алексея.

# ---

# **Изменить несколько столбцов:**

# ```sql
# UPDATE users
# SET age = 25,
#     name = 'Алекс';
# ```

# Изменит сразу `age` и `name` у всех строк.

# ---

# **Изменить значение с использованием его текущего значения:**

# ```sql
# UPDATE products
# SET price = price + 1000;
# ```

# Увеличит цену каждого товара на `1000`.

# ---

# **Изменить только определённые строки:**

# ```sql
# UPDATE products
# SET price = price + 500
# WHERE company = 'Samsung';
# ```

# Увеличит цену только товаров Samsung.

# ---

# **Изменить несколько столбцов с `WHERE`:**

# ```sql
# UPDATE products
# SET price = price + 500,
#     quantity = quantity + 10
# WHERE name = 'Наушники';
# ```

# Изменит `price` и `quantity` только у наушников.

# ---

# **Важно:**

# ```sql
# UPDATE products
# SET price = 1000;
# ```

# Без `WHERE` изменятся **все строки** таблицы.

# ### Кратко:

# ```text
# UPDATE → изменить данные
# SET    → указать, что изменить
# WHERE  → указать, какие строки изменить

# UPDATE без WHERE → изменяет все строки
# ```

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

### DELETE — удаление данных

# `DELETE` → удаляет существующие строки из таблицы.

# **Базовый синтаксис:**

# ```sql
# DELETE FROM таблица
# WHERE условие;
# ```

# ---

# **Удалить одну строку:**

# ```sql
# DELETE FROM users
# WHERE id = 5;
# ```

# Удалит пользователя с `id = 5`.

# ---

# **Удалить строки по условию:**

# ```sql
# DELETE FROM products
# WHERE price < 1000;
# ```

# Удалит все товары дешевле `1000`.

# ---

# **Удалить по нескольким условиям:**

# ```sql
# DELETE FROM products
# WHERE company = 'Samsung'
# AND price < 30000;
# ```

# Удалит товары Samsung дешевле `30000`.

# ---

# **Удалить все строки:**

# ```sql
# DELETE FROM products;
# ```

# Удалит **все строки** из таблицы, но сама таблица останется.

# ---

# ### Важно

# `DELETE` удаляет **строки**, а не саму таблицу.

# ```text
# DELETE FROM products; → удалить данные
# DROP TABLE products;  → удалить таблицу
# ```

# Без `WHERE`:

# ```sql
# DELETE FROM products;
# ```

# будут удалены **все строки**.

# ### Кратко:

# ```text
# DELETE → удалить строки
# FROM   → из какой таблицы
# WHERE  → какие строки удалить

# DELETE без WHERE → удалить все строки
# ```

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# DISTINCT — уникальные значения

# DISTINCT используется, чтобы убрать повторяющиеся значения из результата SELECT.

# Синтаксис:
# SELECT DISTINCT столбец
# FROM таблица;

# Пример:
# SELECT DISTINCT company
# FROM products;

# Было:
# Apple
# Apple
# Samsung
# Samsung
# LG

# С DISTINCT:
# Apple
# Samsung
# LG

# DISTINCT с несколькими столбцами:
# SELECT DISTINCT company, price
# FROM products;

# Уникальной считается комбинация значений всех указанных столбцов.

# Например:
# Apple    50000
# Apple    70000
# Apple    50000
# Samsung  50000

# Результат:
# Apple    50000
# Apple    70000
# Samsung  50000

# DISTINCT + WHERE:
# SELECT DISTINCT company
# FROM products
# WHERE price > 50000;

# Сначала WHERE отбирает строки, затем DISTINCT убирает повторения.

# DISTINCT + ORDER BY:
# SELECT DISTINCT company
# FROM products
# ORDER BY company;

# Простые примеры:

# -- Уникальные компании
# SELECT DISTINCT company
# FROM products;

# -- Уникальные возраста
# SELECT DISTINCT age
# FROM users;

# -- Уникальные города
# SELECT DISTINCT city
# FROM users;

# -- Уникальные компании товаров дороже 1000
# SELECT DISTINCT company
# FROM products
# WHERE price > 1000;

# -- Уникальные комбинации компании и цены
# SELECT DISTINCT company, price
# FROM products;

# Важно:
# DISTINCT не удаляет данные из таблицы. Он только убирает повторения из результата SELECT.

# Кратко:
# SELECT DISTINCT company
# FROM products;

# DISTINCT → каждое значение показывается только один раз.

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# LIMIT и OFFSET

## LIMIT

# `LIMIT` ограничивает количество строк, которое вернёт запрос.

# ```sql
# SELECT *
# FROM products
# LIMIT 5;
# ```

# Вернёт максимум **5 строк**.

# Можно использовать вместе с `ORDER BY`:

# ```sql
# SELECT *
# FROM products
# ORDER BY price
# LIMIT 3;
# ```

# Вернёт 3 товара с самой маленькой ценой.

# ---

# ## OFFSET

# `OFFSET` указывает, сколько строк **пропустить** в начале результата.

# ```sql
# SELECT *
# FROM products
# OFFSET 2;
# ```

# Пропустит первые 2 строки и покажет остальные.

# ---

# ## LIMIT + OFFSET

# Можно пропустить несколько строк и затем получить определённое количество:

# ```sql
# SELECT *
# FROM products
# LIMIT 3 OFFSET 2;
# ```

# Значит:

# * `OFFSET 2` → пропустить 2 строки
# * `LIMIT 3` → после этого взять 3 строки

# Например:

# ```text
# 1. Телефон
# 2. Ноутбук
# 3. Мышь
# 4. Клавиатура
# 5. Монитор
# 6. Наушники
# ```

# ```sql
# LIMIT 3 OFFSET 2
# ```

# Результат:

# ```text
# 3. Мышь
# 4. Клавиатура
# 5. Монитор
# ```

# ---

# ## LIMIT + ORDER BY

# Обычно `LIMIT` используют вместе с `ORDER BY`, чтобы сначала отсортировать данные:

# ```sql
# SELECT *
# FROM products
# ORDER BY price DESC
# LIMIT 5;
# ```

# Получим **5 самых дорогих товаров**.

# ```sql
# SELECT *
# FROM products
# ORDER BY price
# LIMIT 5;
# ```

# Получим **5 самых дешёвых товаров**.

# ---

# ## OFFSET + ORDER BY

# ```sql
# SELECT *
# FROM products
# ORDER BY price
# OFFSET 3;
# ```

# Сначала товары сортируются по цене, затем первые 3 строки пропускаются.

# ---

# ## Пагинация

# `LIMIT` и `OFFSET` часто используются для разбиения большого количества данных на страницы.

# Например, на странице показываем по 5 товаров.

# ### 1-я страница

# ```sql
# SELECT *
# FROM products
# LIMIT 5 OFFSET 0;
# ```

# ### 2-я страница

# ```sql
# SELECT *
# FROM products
# LIMIT 5 OFFSET 5;
# ```

# ### 3-я страница

# ```sql
# SELECT *
# FROM products
# LIMIT 5 OFFSET 10;
# ```

# Формула:

# ```text
# OFFSET = (номер_страницы - 1) * количество_строк
# ```

# Например:

# ```text
# Страница 1 → OFFSET 0
# Страница 2 → OFFSET 5
# Страница 3 → OFFSET 10
# Страница 4 → OFFSET 15
# ```

# ---

# ## LIMIT ALL

# `LIMIT ALL` означает, что ограничение по количеству строк отсутствует.

# ```sql
# SELECT *
# FROM products
# LIMIT ALL OFFSET 2;
# ```

# То есть пропустить 2 строки и показать всё остальное.

# Можно просто написать:

# ```sql
# SELECT *
# FROM products
# OFFSET 2;
# ```

# ---

# ## Кратко

# ```text
# LIMIT  → сколько строк получить
# OFFSET → сколько строк пропустить
# ```

# Пример:

# ```sql
# SELECT *
# FROM products
# ORDER BY price
# LIMIT 5 OFFSET 10;
# ```

# Читаем так:

# ```text
# 1. Отсортировать товары по цене
# 2. Пропустить первые 10
# 3. Получить следующие 5
# ```


# ODER BY - столбцы для сортировки
# GROUP BY - столбцы для группировки
# HAVING - условия фильтрации групп

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# PostgreSQL — Массивы (ARRAY)

## Что такое массив

# Массив позволяет хранить несколько значений в одном столбце.

# Обычный столбец:

# ```sql
# name TEXT
# ```

# Хранит одно значение:

# ```text
# Телефон
# ```

# Столбец-массив:

# ```sql
# tags TEXT[]
# ```

# Может хранить несколько значений:

# ```text
# {sql, postgres, database}
# ```

# ---

# ## Создание таблицы с массивом

# ```sql
# CREATE TABLE posts (
#     id SERIAL PRIMARY KEY,
#     title TEXT,
#     tags TEXT[]
# );
# ```

# `TEXT[]` означает массив значений типа `TEXT`.

# ---

# ## Добавление массива

# ```sql
# INSERT INTO posts (title, tags)
# VALUES (
#     'PostgreSQL',
#     '{"sql", "postgres", "database"}'
# );
# ```

# Можно добавить несколько записей:

# ```sql
# INSERT INTO posts (title, tags)
# VALUES
# ('PostgreSQL', '{"sql", "database"}'),
# ('Python', '{"python", "backend"}'),
# ('Django', '{"python", "web", "backend"}');
# ```

# Массив записывается внутри `{}`.

# ---

# ## Получить весь массив

# ```sql
# SELECT tags
# FROM posts;
# ```

# Результат:

# ```text
# {sql,database}
# {python,backend}
# {python,web,backend}
# ```

# ---

# ## Получить отдельный элемент

# К элементу массива можно обратиться по индексу:

# ```sql
# SELECT tags[1]
# FROM posts;
# ```

# В PostgreSQL первый элемент массива имеет индекс `1`.

# ```text
# tags[1] → первый элемент
# tags[2] → второй элемент
# tags[3] → третий элемент
# ```

# Например:

# ```sql
# SELECT tags[2]
# FROM posts;
# ```

# Если массив:

# ```text
# {python,web,backend}
# ```

# результат:

# ```text
# web
# ```

# ---

# ## Получить диапазон элементов

# Можно получить несколько элементов сразу:

# ```sql
# SELECT tags[1:2]
# FROM posts;
# ```

# `1:2` означает:

# ```text
# с 1-го элемента по 2-й
# ```

# Например:

# ```text
# {python,web,backend}
# ```

# Результат:

# ```text
# {python,web}
# ```

# ---

# ## Изменение всего массива

# Можно заменить весь массив:

# ```sql
# UPDATE posts
# SET tags = '{"sql", "postgres"}'
# WHERE id = 1;
# ```

# Теперь у записи будет:

# ```text
# {sql,postgres}
# ```

# ---

# ## Изменение отдельного элемента

# Можно изменить только один элемент:

# ```sql
# UPDATE posts
# SET tags[2] = 'database'
# WHERE id = 1;
# ```

# Было:

# ```text
# {sql,postgres}
# ```

# Стало:

# ```text
# {sql,database}
# ```

# ---

# ## Добавление элемента

# Можно добавить значение в конец массива с помощью `array_append()`:

# ```sql
# UPDATE posts
# SET tags = array_append(tags, 'backend')
# WHERE id = 1;
# ```

# Было:

# ```text
# {sql,database}
# ```

# Стало:

# ```text
# {sql,database,backend}
# ```

# ---

# ## Удаление элемента

# Функция `array_remove()` удаляет значение из массива:

# ```sql
# UPDATE posts
# SET tags = array_remove(tags, 'database')
# WHERE id = 1;
# ```

# Было:

# ```text
# {sql,database,backend}
# ```

# Стало:

# ```text
# {sql,backend}
# ```

# ---

# ## Пустой массив

# Пустой массив:

# ```sql
# UPDATE posts
# SET tags = '{}'
# WHERE id = 1;
# ```

# Результат:

# ```text
# {}
# ```

# ---

# ## Проверка наличия элемента

# Оператор `ANY` позволяет проверить, есть ли значение среди элементов массива.

# ```sql
# SELECT *
# FROM posts
# WHERE 'python' = ANY(tags);
# ```

# Запрос найдёт записи, в которых среди `tags` есть:

# ```text
# python
# ```

# Например:

# ```text
# {python,backend}
# {python,web,backe
# ```


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Тип данных ENUM


# -- Создать ENUM
# CREATE TYPE status_enum AS ENUM (
#     'new',
#     'processing',
#     'done'
# );

# -- Использовать
# CREATE TABLE tasks (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100),
#     status status_enum
# );

# -- Добавить
# INSERT INTO tasks(title, status)
# VALUES ('Изучить PostgreSQL', 'new');

# -- Изменить
# UPDATE tasks
# SET status = 'done'
# WHERE id = 1;

# -- Добавить новое значение
# ALTER TYPE status_enum
# ADD VALUE 'cancelled';

# -- Удалить весь тип
# DROP TYPE status_enum;

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# PostgreSQL — INNER JOIN и работа с несколькими таблицами

## 1. INNER JOIN

# `INNER JOIN` соединяет строки из двух таблиц по определённому условию.

# ```sql
# SELECT users.name, orders.product
# FROM users
# JOIN orders
#     ON users.id = orders.user_id;
# ```

# Здесь:

# ```text
# users.id = orders.user_id
# ```

# SQL находит заказы, которые принадлежат конкретным пользователям.

# `JOIN` без уточнения = `INNER JOIN`.

# ```sql
# JOIN orders
# ```

# то же самое, что:

# ```sql
# INNER JOIN orders
# ```

# ---

# ## 2. ON

# `ON` задаёт условие, по которому таблицы соединяются.

# Например:

# ```sql
# SELECT *
# FROM users
# JOIN orders
#     ON users.id = orders.user_id;
# ```

# Условие:

# ```sql
# ON users.id = orders.user_id
# ```

# означает:

# > id пользователя должен совпадать с user_id заказа.

# ---

# ## 3. Соединение трёх таблиц

# Можно соединять не только две, но и несколько таблиц.

# Например:

# ```text
# users
#   ↓
# orders
#   ↓
# products
# ```

# Связи:

# ```text
# users.id = orders.user_id
# orders.product_id = products.id
# ```

# SQL:

# ```sql
# SELECT u.name, p.name, p.price
# FROM users AS u
# JOIN orders AS o
#     ON u.id = o.user_id
# JOIN products AS p
#     ON p.id = o.product_id;
# ```

# Здесь:

# ```sql
# users → orders
# ```

# связываются через:

# ```sql
# u.id = o.user_id
# ```

# А:

# ```sql
# orders → products
# ```

# через:

# ```sql
# o.product_id = p.id
# ```

# ### Важно запомнить

# ```sql
# ON u.id = o.user_id
# ON p.id = o.product_id
# ```

# Не нужно путать `user_id` и `product_id`.

# ---

# ## 4. Алиасы AS

# Алиасы позволяют дать таблицам короткие имена.

# ```sql
# FROM users AS u
# JOIN orders AS o
#     ON u.id = o.user_id
# JOIN products AS p
#     ON p.id = o.product_id
# ```

# Теперь:

# ```text
# u = users
# o = orders
# p = products
# ```

# Поэтому вместо:

# ```sql
# users.name
# products.price
# orders.user_id
# ```

# можно писать:

# ```sql
# u.name
# p.price
# o.user_id
# ```

# `AS` можно не писать:

# ```sql
# FROM users u
# JOIN orders o
# ```

# ---

# ## 5. SELECT после JOIN

# Можно выбрать столбцы из разных таблиц.

# ```sql
# SELECT u.name, p.name, p.price
# FROM users AS u
# JOIN orders AS o
#     ON u.id = o.user_id
# JOIN products AS p
#     ON p.id = o.product_id;
# ```

# Получим:

# ```text
# имя пользователя | товар | цена
# ```

# ---

# ## 6. WHERE вместе с JOIN

# `WHERE` фильтрует строки после соединения таблиц.

# Например, вывести товары дороже 4000:

# ```sql
# SELECT u.name, p.name, p.price
# FROM users AS u
# JOIN orders AS o
#     ON u.id = o.user_id
# JOIN products AS p
#     ON p.id = o.product_id
# WHERE p.price > 4000;
# ```

# Можно использовать несколько условий:

# ```sql
# WHERE p.price > 3000
# AND p.category = 'Audio';
# ```

# ---

# ## 7. IN

# `IN` позволяет проверить значение на принадлежность списку.

# Вместо:

# ```sql
# WHERE u.name = 'Alex'
# OR u.name = 'Mike'
# OR u.name = 'Anna'
# ```

# можно:

# ```sql
# WHERE u.name IN ('Alex', 'Mike', 'Anna');
# ```

# То же самое работает с категориями:

# ```sql
# WHERE p.category IN ('Devices', 'Audio');
# ```

# ---

# ## 8. BETWEEN

# Проверяет, находится ли значение в определённом диапазоне.

# ```sql
# WHERE p.price BETWEEN 2000 AND 7000;
# ```

# Это означает:

# ```text
# price >= 2000
# AND
# price <= 7000
# ```

# Границы включаются.

# ---

# ## 9. !=

# `!=` означает «не равно».

# ```sql
# WHERE u.name != 'Egor';
# ```

# То есть показать всех пользователей, кроме Egor.

# Также можно:

# ```sql
# WHERE p.category != 'Accessories';
# ```

# ---

# ## 10. ORDER BY

# `ORDER BY` сортирует результат.

# По возрастанию:

# ```sql
# ORDER BY p.price ASC;
# ```

# `ASC` можно не писать:

# ```sql
# ORDER BY p.price;
# ```

# По убыванию:

# ```sql
# ORDER BY p.price DESC;
# ```

# Например:

# ```sql
# SELECT *
# FROM products
# ORDER BY price DESC;
# ```

# Получим сначала самые дорогие товары.

# ---

# ## 11. Сортировка по нескольким столбцам

# Можно сортировать сразу по нескольким столбцам:

# ```sql
# ORDER BY u.name ASC, p.price DESC;
# ```

# Сначала сортируем пользователей по имени:

# ```text
# Alex
# Anna
# Bob
# Mike
# ```

# А если у одного пользователя несколько товаров, внутри его товаров сортируем по цене от большей к меньшей.

# ---

# # GROUP BY и ORDER BY — разница

# Это разные конструкции.

# ```text
# GROUP BY → группирует строки
# ORDER BY → сортирует строки
# ```

# ## GROUP BY

# `GROUP BY` объединяет строки с одинаковым значением в группы.

# Например:

# ```sql
# SELECT category, COUNT(*)
# FROM products
# GROUP BY category;
# ```

# Получим:

# ```text
# Devices     3
# Audio       2
# Accessories 1
# ```

# Здесь товары были объединены по категории, а `COUNT(*)` посчитал количество товаров в каждой группе.

# `GROUP BY` часто используется вместе с агрегатными функциями:

# ```sql
# COUNT()
# SUM()
# AVG()
# MIN()
# MAX()
# ```

# ---

# ## ORDER BY

# `ORDER BY` не создаёт группы.

# Он просто меняет порядок строк:

# ```sql
# SELECT *
# FROM products
# ORDER BY price DESC;
# ```

# Количество строк остаётся тем же.

# ---

# ## GROUP BY + ORDER BY вместе

# Их можно использовать вместе:

# ```sql
# SELECT category, COUNT(*) AS amount
# FROM products
# GROUP BY category
# ORDER BY amount DESC;
# ```

# Порядок действий:

# ```text
# 1. GROUP BY → группируем товары по категориям
# 2. COUNT(*) → считаем товары в каждой категории
# 3. ORDER BY → сортируем получившиеся группы
# ```

# ### Главное различие

# ```text
# GROUP BY → ЧТО ОБЪЕДИНИТЬ В ГРУППЫ

# ORDER BY → В КАКОМ ПОРЯДКЕ ПОКАЗАТЬ РЕЗУЛЬТАТ
# ```

# ---

# # Общая конструкция JOIN

# При работе с несколькими таблицами часто получается такая структура:

# ```sql
# SELECT ...
# FROM users AS u
# JOIN orders AS o
#     ON u.id = o.user_id
# JOIN products AS p
#     ON p.id = o.product_id
# WHERE ...
# GROUP BY ...
# HAVING ...
# ORDER BY ...;
# ```

# Пока тебе особенно важно запомнить:

# ```text
# SELECT  → что вывести
# FROM    → откуда начать
# JOIN    → какую таблицу присоединить
# ON      → по какому условию соединить
# WHERE   → какие строки оставить
# GROUP BY → какие строки объединить в группы
# HAVING  → какие группы оставить
# ORDER BY → как отсортировать результат
# ```

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# PostgreSQL — OUTER JOIN и CROSS JOIN

## 1. INNER JOIN

# Показывает **только строки, для которых найдено совпадение**.

# ```sql
# SELECT u.name, o.id
# FROM users AS u
# INNER JOIN orders AS o
#     ON u.id = o.user_id;
# ```

# Если у пользователя нет заказа — он не попадёт в результат.

# ```text
# INNER JOIN → только совпадения
# ```

# ---

# ## 2. LEFT JOIN

# Показывает **все строки из левой таблицы** + совпадения из правой.

# ```sql
# SELECT u.name, o.id
# FROM users AS u
# LEFT JOIN orders AS o
#     ON u.id = o.user_id;
# ```

# Если заказа нет:

# ```text
# Mike | NULL
# ```

# То есть:

# ```text
# LEFT JOIN → все строки слева + совпадения справа
# ```

# ### Пример

# ```sql
# SELECT u.name, p.name, p.price
# FROM users AS u
# LEFT JOIN orders AS o
#     ON u.id = o.user_id
# LEFT JOIN products AS p
#     ON o.product_id = p.id;
# ```

# Получим всех пользователей, даже тех, кто ничего не заказывал.

# ---

# ## 3. LEFT JOIN + IS NULL

# Очень полезная конструкция для поиска строк, **у которых нет соответствия**.

# Например, найти пользователей без заказов:

# ```sql
# SELECT u.name
# FROM users AS u
# LEFT JOIN orders AS o
#     ON u.id = o.user_id
# WHERE o.id IS NULL;
# ```

# Логика:

# ```text
# LEFT JOIN
# ↓
# пользователь без заказа
# ↓
# данные orders = NULL
# ↓
# WHERE o.id IS NULL
# ↓
# получаем пользователей без заказов
# ```

# ### Важно

# Начинай `FROM` с того, **кого хочешь найти**.

# Найти пользователей без заказов:

# ```sql
# FROM users
# LEFT JOIN orders
# ```

# Найти товары без заказов:

# ```sql
# FROM products
# LEFT JOIN orders
# ```

# ### Пример — товары без заказов

# ```sql
# SELECT p.name
# FROM products AS p
# LEFT JOIN orders AS o
#     ON p.id = o.product_id
# WHERE o.id IS NULL;
# ```

# ---

# ## 4. LEFT JOIN + IS NOT NULL

# Если использовать `IS NOT NULL`, то мы оставим строки, **для которых соответствие найдено**.

# ```sql
# SELECT u.name, o.id
# FROM users AS u
# LEFT JOIN orders AS o
#     ON u.id = o.user_id
# WHERE o.id IS NOT NULL;
# ```

# Получим только пользователей, у которых есть заказы.

# Можно запомнить:

# ```text
# LEFT JOIN + IS NULL
# → нет соответствия

# LEFT JOIN + IS NOT NULL
# → есть соответствие
# ```

# ---

# ## 5. RIGHT JOIN

# Работает наоборот относительно `LEFT JOIN`.

# Показывает **все строки из правой таблицы** + совпадения из левой.

# ```sql
# SELECT u.name, o.id
# FROM users AS u
# RIGHT JOIN orders AS o
#     ON u.id = o.user_id;
# ```

# Главной здесь является правая таблица:

# ```text
# users RIGHT JOIN orders
#               ↑
#         сохраняем все orders
# ```

# Можно запомнить:

# ```text
# LEFT JOIN  → сохраняет левую таблицу
# RIGHT JOIN → сохраняет правую таблицу
# ```

# ---

# ## 6. FULL JOIN

# Показывает **все строки обеих таблиц**.

# Совпадения объединяются, а там, где совпадения нет, появляется `NULL`.

# ```sql
# SELECT u.name, o.id
# FROM users AS u
# FULL JOIN orders AS o
#     ON u.id = o.user_id;
# ```

# То есть:

# ```text
# FULL JOIN
# → все слева
# + все справа
# + совпадения
# ```

# ---

# ## 7. CROSS JOIN

# Создаёт **все возможные комбинации** строк двух таблиц.

# ```sql
# SELECT u.name, p.name
# FROM users AS u
# CROSS JOIN products AS p;
# ```

# Если:

# ```text
# users = 4 строки
# products = 4 строки
# ```

# то:

# ```text
# 4 × 4 = 16 строк
# ```

# Например:

# ```text
# Alex | Phone
# Alex | Mouse
# Alex | Keyboard
# Alex | Monitor

# Bob  | Phone
# Bob  | Mouse
# Bob  | Keyboard
# Bob  | Monitor
# ...
# ```

# `CROSS JOIN` **не использует `ON`**.

# ---

# ## 8. CROSS JOIN с несколькими таблицами

# Можно написать:

# ```sql
# SELECT u.name, o.id, p.name
# FROM users AS u
# CROSS JOIN orders AS o
# CROSS JOIN products AS p;
# ```

# Тогда количество комбинаций:

# ```text
# users × orders × products
# ```

# Например:

# ```text
# 4 × 3 × 4 = 48 строк
# ```

# Но если задача просто:

# ```text
# пользователь × товар
# ```

# то `orders` здесь не нужна:

# ```sql
# SELECT u.name, p.name
# FROM users AS u
# CROSS JOIN products AS p;
# ```

# ---

# # 9. Главное отличие JOIN

# ```text
# INNER JOIN
# → только совпадения

# LEFT JOIN
# → все строки слева + совпадения справа

# RIGHT JOIN
# → все строки справа + совпадения слева

# FULL JOIN
# → все строки обеих таблиц

# CROSS JOIN
# → все возможные комбинации
# ```

# ---

# # 10. LEFT JOIN или CROSS JOIN?

# ### Нужно:

# > Показать всех пользователей и их заказы.

# Используем:

# ```sql
# LEFT JOIN
# ```

# Потому что нам нужно установить связь:

# ```text
# users.id = orders.user_id
# ```

# ---

# ### Нужно:

# > Получить каждого пользователя с каждым товаром.

# Используем:

# ```sql
# CROSS JOIN
# ```

# Потому что нужны **все комбинации**, а не реальные связи между таблицами.

# ---

# # 11. Полезная схема

# ```text
# INNER JOIN
#        ↓
# только совпадения


# LEFT JOIN
#        ↓
# все слева
# + совпадения справа


# RIGHT JOIN
#        ↓
# совпадения слева
# + все справа


# FULL JOIN
#        ↓
# всё слева
# + всё справа


# CROSS JOIN
#        ↓
# каждый × каждый
# ```

# ---

# # 12. Главное, что нужно запомнить

# ### Если нужно найти тех, у кого чего-то нет:

# ```sql
# SELECT ...
# FROM основная_таблица AS a
# LEFT JOIN другая_таблица AS b
#     ON ...
# WHERE b.id IS NULL;
# ```

# Например:

# ```sql
# SELECT p.name
# FROM products AS p
# LEFT JOIN orders AS o
#     ON p.id = o.product_id
# WHERE o.id IS NULL;
# ```

# → товары, которые никто не заказывал.

# ### Если нужно найти тех, у кого что-то есть:

# ```sql
# WHERE b.id IS NOT NULL;
# ```

# ### Если нужны все возможные комбинации:

# ```sql
# CROSS JOIN
# ```

# ### Главное правило:

# ```text
# LEFT JOIN + IS NULL
# → найти записи БЕЗ соответствия
# ```

# Это один из самых полезных приёмов при работе с JOIN.


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# UNION
# ↓
# объединяет результаты SELECT

# UNION
# → убирает дубликаты

# UNION ALL
# → оставляет дубликаты

# JOIN
# → соединяет столбцы/строки связанных таблиц

# UNION
# → складывает результаты запросов друг под другом




# Шаблон:

# SELECT column1, column2
# FROM table1

# UNION

# SELECT column1, column2
# FROM table2;



# Количество столбцов должно совпадать
# Типы соответствующих столбцов должны быть совместимы



# JOIN — "соедини эти таблицы".
# UNION — "возьми результаты этих запросов и собери в один результат".


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# UNION
# → объединяет результаты

# UNION ALL
# → объединяет результаты + сохраняет дубликаты

# EXCEPT
# → берёт первый результат и убирает строки,
#   которые есть во втором

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# INTERSECT в PostgreSQL

## 1. Что такое INTERSECT

# `INTERSECT` возвращает только те строки, которые присутствуют **в обоих результатах SELECT**.

# Проще:

# ```text
# A INTERSECT B
# ```

# → что есть и в A, и в B.

# ### Пример

# ```sql
# SELECT name
# FROM customers

# INTERSECT

# SELECT name
# FROM employees;
# ```

# Если:

# ```text
# customers:  Alex, Bob, Mike, Anna
# employees:  Bob, Anna, Sergey
# ```

# Результат:

# ```text
# Bob
# Anna
# ```

# ---

# ## 2. Синтаксис

# ```sql
# SELECT столбцы
# FROM таблица1

# INTERSECT

# SELECT столбцы
# FROM таблица2;
# ```

# ---

# ## 3. Главное правило

# Оба `SELECT` должны возвращать:

# * одинаковое количество столбцов;
# * совместимые типы данных.

# ✅ Правильно:

# ```sql
# SELECT name, city
# FROM customers

# INTERSECT

# SELECT name, city
# FROM employees;
# ```

# ❌ Неправильно:

# ```sql
# SELECT name, city
# FROM customers

# INTERSECT

# SELECT name
# FROM employees;
# ```

# Слева 2 столбца, справа 1.

# ---

# ## 4. INTERSECT убирает дубликаты

# Обычный `INTERSECT` возвращает уникальные строки.

# ```sql
# SELECT city
# FROM customers

# INTERSECT

# SELECT city
# FROM employees;
# ```

# Если `Moscow` встречается несколько раз, в результате она будет только один раз.

# ---

# ## 5. INTERSECT ALL

# `INTERSECT ALL` сохраняет повторения.

# ```sql
# SELECT name
# FROM customers

# INTERSECT ALL

# SELECT name
# FROM employees;
# ```

# В обычных задачах чаще используется обычный `INTERSECT`.

# ---

# # 6. Сравнение UNION, EXCEPT и INTERSECT

# ### UNION

# Объединяет результаты.

# ```sql
# SELECT name FROM customers
# UNION
# SELECT name FROM employees;
# ```

# ```text
# A + B
# ```

# → всё из обоих результатов, без дубликатов.

# ---

# ### EXCEPT

# Вычитает второй результат из первого.

# ```sql
# SELECT name FROM customers
# EXCEPT
# SELECT name FROM employees;
# ```

# ```text
# A - B
# ```

# → есть в A, но нет в B.

# **Порядок важен:**

# ```sql
# A EXCEPT B
# ```

# и

# ```sql
# B EXCEPT A
# ```

# — разные результаты.

# ---

# ### INTERSECT

# Находит пересечение.

# ```sql
# SELECT name FROM customers
# INTERSECT
# SELECT name FROM employees;
# ```

# ```text
# A ∩ B
# ```

# → есть и в A, и в B.

# ---

# # 7. INTERSECT с несколькими столбцами

# Сравнивается **вся строка**, то есть комбинация столбцов.

# ```sql
# SELECT name, city
# FROM customers

# INTERSECT

# SELECT name, city
# FROM employees;
# ```

# Например:

# ```text
# Bob | Kazan
# Anna | Perm
# ```

# Если имя совпадает, но город разный:

# ```text
# Bob | Moscow
# Bob | Kazan
# ```

# такие строки не считаются одинаковыми.

# ---

# # 8. INTERSECT с JOIN

# `INTERSECT` можно использовать внутри подзапроса, чтобы сначала получить нужных людей.

# Например, найти покупателей, которые одновременно являются сотрудниками:

# ```sql
# SELECT c.name, COUNT(o.product)
# FROM customers AS c
# JOIN orders AS o
#     ON o.customer_id = c.id
# WHERE c.name IN (
#     SELECT name
#     FROM customers

#     INTERSECT

#     SELECT name
#     FROM employees
# )
# GROUP BY c.name;
# ```

# Здесь:

# ```text
# INTERSECT
#     ↓
# получаем общих людей

# JOIN
#     ↓
# подключаем их заказы

# GROUP BY
#     ↓
# группируем по имени

# COUNT
#     ↓
# считаем заказы
# ```

# ---

# # 9. INTERSECT + GROUP BY + HAVING

# Можно фильтровать группы:

# ```sql
# SELECT c.name, COUNT(o.product), SUM(o.price)
# FROM customers AS c
# JOIN orders AS o
#     ON o.customer_id = c.id
# WHERE c.name IN (
#     SELECT name
#     FROM customers

#     INTERSECT

#     SELECT name
#     FROM employees
# )
# GROUP BY c.name
# HAVING COUNT(o.product) > 1
#    AND SUM(o.price) > 5000;
# ```

# Получаем покупателей, которые:

# * являются сотрудниками;
# * сделали больше 1 заказа;
# * потратили больше 5000.

# ---

# # 10. Главное правило для запоминания

# ```text
# UNION
# → объединить

# EXCEPT
# → вычесть

# INTERSECT
# → найти общее
# ```

# Можно представить как множества:

# ```text
# UNION       → A + B
# EXCEPT      → A - B
# INTERSECT   → A ∩ B
# ```

# ### Коротко:

# ```sql
# A UNION B
# ```

# → всё из A и B

# ```sql
# A EXCEPT B
# ```

# → только A, без B

# ```sql
# A INTERSECT B
# ```

# → только общее для A и B


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------



# -----------------------------------------------------------------------
# -----------------------------------------------------------------------