from tkinter import *
from tkinter import ttk
from tkinter import filedialog
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

 
# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
 
open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)


root.mainloop()