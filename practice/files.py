import shelve

FILENAME = 'contacts.db'

menu_user = input('1. Добавить контакт\t2. Найти контакт\t3. Показать все контакты\t4. Выход\n')

if menu_user == '1':
    name = input('\tВведите Имя\n')
    phone_number = input('\tВведите Номер Телефона\n')
    
    with shelve.open(FILENAME) as file:
        file[name] = [phone_number]

    print('\tИмя: ', name, '\tТелефон: ', phone_number)

if menu_user == '2':
        number = input('\tВведите номер телефона:\n')
        
        with shelve.open(FILENAME) as file:
            if number in file:
                print(f"\t{number} {file[name]}")
            else:
                print('\tТакого номера нету!')

if menu_user == '3':
    with shelve.open(FILENAME) as file:
        keys = sorted(file.keys())
        
        for key in keys:
            print(f'\tИмя: {key} \tТелефон: {file[key]}')

if menu_user == '4':
    quit()




    
    