from tkinter import *
from tkinter import ttk
import time

FILENAME = 'data.txt'

def delete(): entry.delete(0, END)

def save():
    if not entry.get():
            label2['text'] = 'Поле пустое!'
            label2.grid()
            root.after(2000, label2.grid_remove)
    elif entry.get():
        with open(FILENAME, 'a', encoding="utf-8") as file:
            file.write(entry.get())
            file.write('\n')
            
            label1['text'] = 'Сохранено!'
            label1.grid()
            root.after(2000, label1.grid_remove)

def data():
        # очистка data.txt
            pass

root = Tk()
root.geometry('370x200')
root.title('Тест Tkinter')

label1 = ttk.Label()
label1.place(x=125, y=45)

label2 = ttk.Label()
label2.place(x=135, y=45)

label3 = ttk.Label()
label3.place(x=165, y=45)

entry = ttk.Entry()
entry.place(x=100, y=70)

delete_btn = ttk.Button(text="Сборс", command=delete)
delete_btn.place(x=70, y=95)

save_btn = ttk.Button(text='Сохранить', command=save)
save_btn.place(x=180, y=95)

savedata_btn = ttk.Button(text='Список сохранений', command=data)
savedata_btn.place(x=105, y=125)

root.mainloop()