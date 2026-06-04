import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Message Box")
root.geometry("300x400")

def show_info():
    messagebox.showinfo("Information","This is information!")

def ask_question():
    response = messagebox.askyesno("Question","Answer Yes or No!")
    if response:
        label.config(text="You chose Yes!")
    else:
        label.config(text="You chose No!")

info_btn = tk.Button(root,text="Show Info",command=show_info)
info_btn.pack(pady=10)

ques_btn = tk.Button(root,text="Ask",command=ask_question)
ques_btn.pack(pady=10)

label = tk.Label(root,text="")
label.pack()

root.mainloop()