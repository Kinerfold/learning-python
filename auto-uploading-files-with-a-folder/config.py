from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

FILENAME = 'main.py'



root = Tk()
root.title("Save Files")
root.geometry("450x400")

open_button = ttk.Button(text="Открыть файл")
open_button.pack(expand=True, fill=X, padx=[70, 70], pady=30)

root.mainloop()