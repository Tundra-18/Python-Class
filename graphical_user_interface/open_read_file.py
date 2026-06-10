import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Open & Read File")
root.geometry("400x400")

def openfile():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if file:
        with open(file,"r",encoding="utf-8") as f:
            content =f.read()
            text_area.delete('1.0',tk.END)
            text_area.insert(tk.END,content)

text_area = tk.Text(root,wrap='word',height=15)
text_area.pack(padx=10,pady=10)

open_btn = tk.Button(root,text='Open',command=openfile)
open_btn.pack(pady=5)

root.mainloop()