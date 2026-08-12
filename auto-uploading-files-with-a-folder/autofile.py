from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def open_file():
    filepath = filedialog.askopenfilename()
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()
        
        if data:
            os.startfile(filepath, 'runas')
            label = ttk.Label(root, text=filepath, font=("Arial", 12))
            label.pack(pady=70)
            label.after(5000, lambda: label.pack_forget())
        else:
            return False

root = Tk()
root.title("Save Files")
root.geometry("450x500")

open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.pack(expand=True, fill=BOTH, padx=[70, 70], pady=130)

root.mainloop()

# does not work