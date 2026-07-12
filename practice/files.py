import shelve

FILENAME = 'contacts.db'

menu_user = input('1. Добавить контакт\t2. Найти контакт\t3. Показать все контакты\t4. Выход\n')

with shelve.open(FILENAME) as file:
    if menu_user == '1':
        name = input('\tВведите Имя\n')
        phone_number = input('\tВведите Номер Телефона\n')
        
        file[name] = [phone_number]

        print('\tИмя: ', name, '\tТелефон: ', phone_number)

    if menu_user == '2':
            name = input('\tВведите имя:\n')

            if name in file:
                print(f"\t{name}: {file[name]}")
            else:
                print("\tТакого контакта нету!")

    if menu_user == '3':
            keys = sorted(file.keys())
            
            for key in keys:
                print(f'\tИмя: {key} \tТелефон: {file[key]}')

    if menu_user == '4':
        quit()




    
    