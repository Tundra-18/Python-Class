import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox")
root.geometry("400x400")

def show_choice():
    label.config(text=f"You choose : {combo.get()}")


combo = ttk.Combobox(root,values=["Python","Java","C++","PHP"])
combo.current(0)
combo.pack()

btn = tk.Button(root,text="Show Selected",command=show_choice,bg="lightgreen")
btn.pack(pady=10)

label = tk.Label(root,text="Choose",bg='lightblue')
label.pack(pady=5)
root.mainloop()

