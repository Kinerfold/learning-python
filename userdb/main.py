import sqlite3

con = sqlite3.connect('users.db')

cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS db
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER CHECK(age > 0),
                city TEXT DEFAULT 'Unknown')
                ''')

con.commit()

user = int(input('1, 2, 3, 4 ?\n'))

if user == 1:
    user_name = input('Имя: ')
    user_age = int(input('Возраст: '))
    user_city = input('Город: ')
    
    cursor.execute("INSERT INTO db (name, age, city) VALUES (?, ?, ?)",
                (user_name, user_age, user_city))
    
    con.commit()
    
    print('Пользователь добавлен!')
    
    cursor.execute("SELECT * FROM db")
    
    print(cursor.fetchall())

elif user == 2:
    cursor.execute("SELECT * FROM db")
    
    print(cursor.fetchall())

elif user == 3:
    user_age = int(input('Возраст: '))
    
    cursor.execute("SELECT * FROM db WHERE age > ?",
                (user_age,))
    
    
    print(cursor.fetchall())

elif user == 4:
    user_city = input('Город: ')
    
    cursor.execute("SELECT * FROM db WHERE city = ?",
                (user_city,))
    
    print(cursor.fetchall())

else:
    print('Такого действия нет!')