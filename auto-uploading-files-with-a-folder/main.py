from tkinter import *
from tkinter import ttk
import time

FILENAME = 'data.txt'

def delete():
    entry.delete(0, END)

def save():
    entry.get()
    
    if not entry.get():
            label2['text'] = 'Поле пустое!'
            root.after(1800, label2.grid_remove())
    elif entry.get():
        with open(FILENAME, 'a', encoding="utf-8") as file:
            file.write(entry.get())
            file.write('\n')
            
            label1['text'] = 'Сохранено!'
            label1.grid()
            root.after(1800, label1.grid_remove())

root = Tk()
root.geometry('370x200')
root.title('Тестовое окно')

label1 = ttk.Label()
label1.place(x=125, y=45)

label2 = ttk.Label()
label2.place(x=135, y=45)

entry = ttk.Entry()
entry.place(x=100, y=70)

btn1 = ttk.Button(text="Сборс", command=delete)
btn1.place(x=70, y=95)

btn2 = ttk.Button(text='Сохранить', command=save)
btn2.place(x=180, y=95)

root.mainloop()