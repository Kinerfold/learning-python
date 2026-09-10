import sqlite3

con = sqlite3.connect('testdb.db')

cursor = con.cursor()

con.execute("PRAGMA foreign_keys = ON")

# cursor.execute("DROP TABLE IF EXISTS users")
# cursor.execute("DROP TABLE IF EXISTS orders")

cursor.execute("""CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               email TEXT UNIQUE,
               age INTEGER CHECK(age >=18 ))
               """)

cursor.execute("""CREATE TABLE IF NOT EXISTS orders
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               product TEXT NOT NULL,
               price INTEGER CHECK(price > 0),
               quantity INTEGER DEFAULT 1 CHECK(quantity > 0),
               user_id INTEGER,
               
               FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE)""")

con.commit()


def work():
    menu = int(input("1. Добавить пользователя\n2. Показать пользователей\n3. Найти пользователя\n4. Добавить заказ\n5. Показать все заказы\n6. Показать заказы конкретного пользователя\n7. Найти заказы по товару\n8. Показать самые дорогие заказы\n9. Удалить пользователя\n0. Выход\n"))
    
    if menu == 1:
        name_user = input('Имя: ')
        email_user = input('Email: ')
        age_user = int(input('Возраст: '))
        
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                       (name_user, email_user, age_user))
        
        con.commit()
        
        print('Пользователь добавлен!')
    
    elif menu == 2:
        cursor.execute("SELECT * FROM users")
        
        print(cursor.fetchall())
    
    elif menu == 3:
        name_user = input('Введите имя: ')

        cursor.execute("SELECT * FROM users WHERE name LIKE ?",
                       (name_user,))

        print(cursor.fetchall())
    
    elif menu == 4:
        user_id = int(input('ID: '))
        user_product = input('Товар: ')
        user_price = int(input('Цена: '))
        user_quantity = int(input('Количество: '))
        
        cursor.execute("INSERT INTO orders (user_id, product, price, quantity) VALUES (?, ?, ?, ?)",
                       (user_id, user_product, user_price, user_quantity))
        
        con.commit()
        
        print('Заказ добавлен')
    
    elif menu == 5:
        cursor.execute("SELECT users.name, orders.product FROM users JOIN orders ON users.id = orders.user_id")
    
        print(cursor.fetchall())
        
    elif menu == 6:
        user_id = int(input('ID: '))
        
        cursor.execute("SELECT * FROM orders WHERE user_id=?",
                       (user_id,))
        
        print(cursor.fetchall())
    
    elif menu == 7:
        user_product = input('Введите товар: ')
        
        cursor.execute('SELECT product FROM orders WHERE product LIKE ?',
                       (f"%{name_user}%",))
        
        print(cursor.fetchall())
    
    elif menu == 8:
        cursor.execute("SELECT price, quantity FROM orders ORDER BY price * quantity DESC LIMIT 3")
        
        print(cursor.fetchall())
    
    elif menu == 9:
        user_id = int(input('ID: '))
        
        cursor.execute("DELETE FROM users WHERE id=?",
                       (user_id,))
        
        con.commit()
        
        print('Пользователь удалён!')
    
    elif menu == 0:
        print('Пока!')     
        
        quit()  

work()