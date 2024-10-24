import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def click_button1():
    btn_count.set(btn_count.get() + 1)
    test_window.title("You Clicked the Button " + str(btn_count.get()) + " Times!")

def click_button2():
    test_window.destroy()

def click_button3():
    test_window.title(entry_text1.get())

def click_error():
    messagebox.showerror("Error","This is an Error message test")

test_window = tk.Tk()
test_window.title("Test App")
test_window.geometry("500x300+500+300")

frame = ttk.Frame(test_window, padding = "30 30 30 30")
frame.pack(fill = tk.BOTH, expand = True)

btn_count = tk.IntVar()
btn_count.set(0)

button1 = ttk.Button(frame, text = "Click Me!", command = click_button1)
button1.pack()
button2 = ttk.Button(frame, text = "No Click Me!", command = click_button2)
button2.pack()

label1 = ttk.Label(frame, text = "Test Label").pack()
entry_text1 = tk.StringVar()
entry1 = ttk.Entry(frame, width = 25, textvariable = entry_text1).pack()

button3 = ttk.Button(frame, text = "Change Title!", command = click_button3).pack()

error_button = ttk.Button(frame, text = "Show Error Message", command = click_error).pack()

test_window.mainloop()