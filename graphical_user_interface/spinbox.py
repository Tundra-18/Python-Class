import tkinter as tk

root = tk.Tk()
root.title("Spinbox")
root.geometry("400x400")

def show_value():
    label.config(text=f"Value is : {spin.get()}")

spin = tk.Spinbox(root,from_=0,to=10)
spin.pack(pady=5)

btn = tk.Button(root,text="Spin",command=show_value)
btn.pack(pady=5)

label = tk.Label(root,text="")
label.pack(pady=5)
root.mainloop()