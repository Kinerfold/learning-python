# Пример с оператором CONSTRAINT 

import sqlite3

con = sqlite3.connect('shop.db')

cursor = con.cursor()

con.execute('''CREATE TABLE IF NOT EXISTS products
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sku INTEGER,
            price INTEGER,
            quantity INTEGER,
            category TEXT,
            status TEXT DEFAULT 'available',

            CONSTRAINT user_sku UNIQUE(sku),
            CONSTRAINT user_price CHECK(price > 0),
            CONSTRAINT user_quantity CHECK(quantity >= 0),
            CONSTRAINT user_category CHECK(category IN ('electronics', 'clothes', 'food')),
            CONSTRAINT user_status CHECK(status IN ('available', 'sold')))
           ''')

con.commit()


def work():
    name_work = input('Имя: ')
    sku_work = int(input('Число: '))
    price_work = int(input('Цена: '))
    quantity_work = int(input('Колво: '))
    category_work = input('Категория: ')
    status_work = input('Статус: ')
    
    try:
        cursor.execute("INSERT INTO products (name, sku, price, quantity, category, status) VALUES(?, ?, ?, ?, ?, ?)"
                    ,(name_work, sku_work, price_work, quantity_work, category_work, status_work))
        
        con.commit()
        
        print('Всё добавлено!')
        
    except sqlite3.IntegrityError as error:
        print(error)


work()


