import tkinter as tk

root = tk.Tk()
root.title("Escape")
root.geometry("300x400")

def on_press(event):
    if event.keysym == "Escape":
        root.destroy()

root.bind("<Escape>",on_press)
root.mainloop()

