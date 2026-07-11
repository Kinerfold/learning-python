import pickle

FILENAME = 'students.pkl'

students = {
    "Иван": 5,
    "Анна": 4,
    "Максим": 3
}

while True:

    with open (FILENAME, 'wb') as file:
        pickle.dump(students, file)

    with open(FILENAME, 'rb') as file:
        students = pickle.load(file)
        
        user = input('Введи имя студента: ')
        if user in students:
            print(students[user])
            break
        else:
            print('\tСтудент не найден')
            
            a = input('\tХотите повторить? д/н ')
            
        if a == 'д':
            continue
        elif a == 'н':
            break