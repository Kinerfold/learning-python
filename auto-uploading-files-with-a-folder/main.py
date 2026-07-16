from tkinter import *
from tkinter import ttk

FILENAME = 'data.txt'

def delete():
    entry.delete(0, END)

def save():
    entry.get()
    
    with open(FILENAME, 'a', encoding="utf-8") as file:
        file.write(str(entry.get()))
        file.write('\n')

root = Tk()
root.geometry('370x200')
root.title('Тестовое окно')

entry = ttk.Entry()
entry.place(x=100, y=70)

btn1 = ttk.Button(text="Сборс", command=delete)
btn1.place(x=70, y=95)

btn2 = ttk.Button(text='Сохранить', command=save)
btn2.place(x=180, y=95)

root.mainloop()