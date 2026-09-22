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

