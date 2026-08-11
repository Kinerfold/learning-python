from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def open_file():
    filepath = filedialog.askopenfilename()
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()
        
        if data:
            label = ttk.Label(root, text=filepath, font=("Arial", 12))
            label.pack(pady=70)
            label.after(3000, lambda: label.pack_forget())
        else:
            return False

def start():
    os.startfile(open_file,'runas')# I know the script is very simple, but I spent quite a lot of time figuring out how to make it.

root = Tk()
root.title("Save Files")
root.geometry("450x400")

open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.pack(expand=True, fill=X, padx=[70, 70], pady=30)

root.mainloop()