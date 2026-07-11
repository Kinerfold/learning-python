with open('notes.txt', 'r', encoding='utf-8') as file:
        line = file.readlines()
        lines = len(line)
        print('В файле строк: ', lines )