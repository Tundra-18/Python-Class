import tkinter as tk

root = tk.Tk()
root.title("Slider")

def show_value(value):
    label.config(text=f"Value is : {value}")

scale = tk.Scale(root,from_=0,to=100,orient='horizontal',command=show_value)
scale.pack()

label = tk.Label(root,text="")
label.pack()

root.mainloop()

