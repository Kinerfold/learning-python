import sqlite3

con = sqlite3.connect('shop.db')

cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER,
                quantity INTEGER)
                ''')

con.commit()

def choose():
    user = int(input('''1. Добавить товар\n
    2. Показать товары\n
    3. Найти товар\n
    4. Изменить цену\n
    5. Изменить количество\n
    6. Удалить товар\n
    0. Выход\n'''))

    if user == 1:
        user_name = input('Напиши имя: ')
        user_price = input('Напиши цену: ')
        user_quantity = input('Напиши колво: ')
        
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", 
                       (user_name, user_price, user_quantity))
        con.commit()
        
        print(cursor.fetchall())


    if user == 2:
        cursor.execute("SELECT * FROM products")
        con.commit()
        
        print(cursor.fetchall())
    
    if user == 3:
        user_name = input('Введи имя: ')
        
        cursor.execute("SELECT * FROM products WHERE name=?", (user_name,))
        con.commit()
        
        print(cursor.fetchall())
    
    if user == 4:
        user_id = input('Введи ID: ')
        user_price = input('Введи цену: ')
        
        cursor.execute("UPDATE products SET price=? WHERE id=?", (user_price, user_id))
        con.commit()
        
        cursor.execute("SELECT * FROM products")
        con.commit()
        
        print(cursor.fetchall())
    
    if user == 5:
        user_id = input('Введи ID: ')
        user_quantity = input('Введи колво: ')
        
        cursor.execute("UPDATE products SET quantity=? WHERE id=?", (user_quantity, user_id))
        con.commit()
        
        cursor.execute("SELECT * FROM products")
        con.commit()
        
        print(cursor.fetchall())
    
    if user == 6:
        user_id = input('ID: ')
        
        cursor.execute("DELETE FROM products WHERE id=?", (user_id))
        con.commit()
        
        cursor.execute("SELECT * FROM products")
        con.commit()
        
        print(cursor.fetchall())
    
    if user == 0:
        print('Пока!')
        quit()
    
    return choose
        
    
    

choose()