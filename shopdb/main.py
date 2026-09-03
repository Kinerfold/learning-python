import sqlite3

con = sqlite3.connect('list.db')

cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               sku INTEGER UNIQUE,
               price INTEGER CHECK(price > 0),
               quantity INTEGER CHECK(quantity >= 0),
               category TEXT CHECK(category IN ('electronics', 'clothes', 'food'))
               )''')

con.commit()

user = int(input('1, 2, 3, 4, 5, 6\n'))

if user == 1:
    user_name = input('Название: ')
    user_sku = int(input('Единица Складского Учёта: '))
    user_price = int(input('Цена: '))
    user_quantity = int(input('Колво: '))
    user_category = input('Категория: ') # 'electronics', 'clothes', 'food'
    
    cursor.execute("INSERT INTO products (name, sku, price, quantity, category) VALUES (?, ?, ?, ?, ?)",
                   (user_name, user_sku, user_price, user_quantity, user_category))
    
    con.commit()
    
    print(f'Товар {user_name} добавлен(ы)!')
    
elif user == 2:
    cursor.execute("SELECT * FROM products")
    
    print(cursor.fetchall())

elif user == 3:
    user_name = input('Название: ')
    
    cursor.execute("SELECT * FROM products WHERE name = ?",
                   (user_name,))
    
    print(cursor.fetchall())

elif user == 4:
    user_name = input('Название товара: ')
    user_quantity = int(input('Колво для изменения: '))
    
    cursor.execute("UPDATE products SET quantity = ? WHERE name = ?",
                   (user_quantity, user_name))
    
    con.commit()
    
    print(f'Товар {user_name} поменял своё колво на {user_quantity}')

elif user == 5:
   user_name = input('Название товара: ')
   
   cursor.execute("DELETE FROM products WHERE name = ?",
                  (user_name,))
   
   con.commit()
   
   print(f'Товар {user_name} удалён!')

elif user == 6:
    user_price = int(input('Дороже (число): '))
    
    cursor.execute("SELECT * FROM products WHERE price > ?",
                   (user_price,))
    
    print(cursor.fetchall()) 