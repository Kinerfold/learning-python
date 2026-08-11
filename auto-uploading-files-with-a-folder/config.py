from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import main

def open_file():
    filepath = filedialog.askopenfilename()
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()
        
        if data:
            os.system('python main.py')
            label = ttk.Label(root, text=filepath, font=("Arial", 12))
            label.pack(pady=70)
            label.after(3000, lambda: label.pack_forget())
        else:
            return False

root = Tk()
root.title("Save Files")
root.geometry("450x400")

open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.pack(expand=True, fill=X, padx=[70, 70], pady=30)

root.mainloop()
