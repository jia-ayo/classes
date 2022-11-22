import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('240x100')
root.title('login')
root.resizable(0,0)

#configure grid
root.columnconfigure(0, weight=1)
root.columnconfigure(0, weight=3)

#username
username_label = ttk.Label(root, text="Username: ")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

#password 
password_label = ttk.Label(root, text="Login: ")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root)
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
