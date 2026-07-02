import sys

while True:
    print("""
        КАЛЬКУЛЯТОР

    1. Сложение
    2. Вычитание
    3. Умножение
    4. Деление
    5. Степень
    6. Целочисленное деление
    0. Выход
    """)
    operation = input('')

    if operation == '0':
        print("""
            
            До свидания!
            
            """)
        sys.exit()

    user = int(input('Первое число: '))
    user2 = int(input('Второе число: '))

    def plus(user, user2):
        return(user + user2)

    def minus(user, user2):
        return(user - user2)

    def multiplication(user, user2):
        return(user * user2)

    def division(user, user2):
        return(user / user2)
        
    def degree(user, user2):
        return(user ** user2)

    def int_division(user, user2):
        return(user // user2)

    if operation == "1":
        print(plus(user, user2))
        answer = input("""
               
               Хотите продолжить? д/н 
               
               """)
        if answer == 'д':
            continue
        elif answer == 'н':
            sys.exit()
    elif operation == "2":
        print(minus(user, user2))
        answer = input("""
               
               Хотите продолжить? д/н 
               
               """)
        if answer == 'д':
            continue
        elif answer == 'н':
            sys.exit()
    elif operation == "3":
        print(multiplication(user, user2))
        answer = input("""
               
               Хотите продолжить? д/н 
               
               """)
        if answer == 'д':
            continue
        elif answer == 'н':
            sys.exit()
    elif operation == "4":
        print(division(user, user2))
        try:
            print(user / user2)
        except ZeroDivisionError:
            print('Ошибка!')
        except ValueError:
            print('Это не число!')
            
        answer = input("""
               
               Хотите продолжить? д/н 
               
               """)
        if answer == 'д':
            continue
        elif answer == 'н':
            sys.exit()

    elif operation == "5":
        print(degree(user, user2))
        answer = input("""
               
               Хотите продолжить? д/н 
               
               """)
        if answer == 'д':
            continue
        elif answer == 'н':
            sys.exit()
    elif operation == "6":
        print(int_division(user, user2))
        answer = input("""
               
               Хотите продолжить? д/н 
               
               """)
        if answer == 'д':
            continue
        elif answer == 'н':
            sys.exit()
