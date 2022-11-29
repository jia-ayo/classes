import tkinter as tk
from tkinter import ttk

root= tk.Tk()

# def button_clicked():
#     print("Button clicked")
# button = ttk.Button(root, text="Click Me", command=button_clicked)
# button.pack()

root.geometry("200x200")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
def button_clicked():
    print("this text wasprinted as a command binding example")
button = ttk.Button(root, text="ok", command=button_clicked)
button.pack()



root.mainloop()



