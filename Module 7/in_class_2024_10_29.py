import tkinter as tk
from tkinter import ttk

def change_title():
    
    root.title(entry_text.get())
    
# def change_color():
#     color_text = color_text.replace(i[0], "", 1)
#     root.configure(color_text.get())

root = tk.Tk()

root.configure(bg='lightblue')

root.geometry('500x500')

frame = tk.Frame(root, bg='lightgreen')
frame.pack(fill=tk.BOTH, expand=True)

# color_text = tk.StringVar()
entry_text = tk.StringVar()

entry = ttk.Entry(root, width = 25, textvariable = entry_text).pack()
button1 = ttk.Button(entry, text = "Change Title", command = change_title).pack()

# color = ttk.Entry(root, width = 25, textvariable = color_text).pack()
# button2 = ttk.Button(color, text = "Change Back Ground Color", command = change_color).pack()

root.mainloop()