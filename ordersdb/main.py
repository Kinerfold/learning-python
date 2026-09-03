import sqlite3

con = sqlite3.connect('orders.db')

cursor = con.cursor()

con.execute('PRAGMA foreign_keys = ON')

cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NO NULL)
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               product TEXT,
               price INTEGER,
               user_id INTEGER,
               
               FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)
               ''')

con.commit()

user = int(input('1, 2, 3, 4, 5, 6\n'))

if user == 1:
    user_name = input('Имя: ')
    
    cursor.execute("INSERT INTO users (name) VALUES (?)",
                   (user_name,))
    
    con.commit()
    
    print(f'Пользователь {user_name} добавлен!')

elif user == 2:
    user_id = int(input('ID пользователя: '))
    user_product = input('Товар: ')
    user_price = int(input('Цена: '))

    cursor.execute(
        "INSERT INTO orders (product, price, user_id) VALUES (?, ?, ?)",
        (user_product, user_price, user_id))

    con.commit()

    print(f'Заказ {user_product} добавлен!')

elif user == 3:
    cursor.execute("SELECT * FROM users")
    
    print(cursor.fetchall())

elif user == 4:
    cursor.execute("SELECT * FROM orders")
    
    print(cursor.fetchall())

elif user == 5:
    user_id = int(input('ID Пользователя: '))
    
    cursor.execute("SELECT * FROM orders WHERE user_id = ?",
                   (user_id,))
    
    print(cursor.fetchall())

elif user == 6:
    user_id = int(input('ID Пользователя: '))
    
    cursor.execute("DELETE FROM users WHERE id = ?",
                   (user_id,))
    
    con.commit()
    
    print(f'ID {user_id} удалён!')

else:
    print(f'Команды {user} нету!')