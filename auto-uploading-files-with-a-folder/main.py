from tkinter import *
from tkinter import ttk
import time

FILENAME = 'data.txt'

def delete(): entry.delete(0, END)

def save():
    if not entry.get():
            empty['text'] = 'Поле пустое!'
            empty.grid()
            root.after(2000, empty.grid_remove)
    elif entry.get():
        with open(FILENAME, 'a', encoding="utf-8") as file:
            file.write(entry.get())
            file.write('\n')
            
            savebtn['text'] = 'Сохранено!'
            savebtn.grid()
            root.after(2000, savebtn.grid_remove)

def data():
    with open(FILENAME, 'w') as file:
        pass

root = Tk()
root.geometry('370x200')
root.title('Тест Tkinter')

savebtn = ttk.Label()
savebtn.place(x=125, y=45)

empty = ttk.Label()
empty.place(x=135, y=45)

clear = ttk.Label()
clear.place(x=165, y=45)

entry = ttk.Entry()
entry.place(x=100, y=70)

deletebtn = ttk.Button(text="Сборс", command=delete)
deletebtn.place(x=70, y=95)

savebtn_savebtnn = ttk.Button(text='Сохранить', command=save)
savebtn_savebtnn.place(x=180, y=95)

clearbtn = ttk.Button(text='Очистить файл', command=data)
clearbtn.place(x=115, y=125)

root.mainloop()