from tkinter import *
from tkinter import ttk

def display():
    label['text'] = entry.get()
    
    if label:
        entry.delete(0, END)
    
    if len(label['text']) > 15:
        label['text'] = 'Слишком длинное имя!'

root = Tk()
root.title('ОКНО 1')
root.geometry("250x200")

btn = ttk.Button(text='Поздороваться!', command=display)
btn.pack()

label = ttk.Label()
label.pack()

entry = ttk.Entry()
entry.pack()

entry.insert(0, "Введите имя!")

root.mainloop()