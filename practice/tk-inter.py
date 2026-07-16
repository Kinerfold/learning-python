from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
def checkbutton_changed():
    if enabled.get() == 1:
        showinfo(title="Info", message="Включено")
    else:
        showinfo(title="Info", message="Отключено")
 
enabled = IntVar()
  
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, command=checkbutton_changed)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
 
root.mainloop()