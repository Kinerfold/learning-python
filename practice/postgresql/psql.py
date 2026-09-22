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

