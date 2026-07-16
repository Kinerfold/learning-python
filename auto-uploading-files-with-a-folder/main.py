from tkinter import *
from tkinter import ttk

def delete():
    btn2[''] = entry.delete(0, END)
    
root = Tk()
root.geometry('300x200')
root.title('Тестовое окно')

entry = ttk.Entry()
entry.place(x=50, y=70)

btn2 = ttk.Button(text="Сборс", command=delete)
btn2.place(x=70, y=95)

root.mainloop()