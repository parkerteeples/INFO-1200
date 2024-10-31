import tkinter as tk
from tkinter import ttk, messagebox

binresult = 0

def fromdecimal():
    print("Decimal")

def frombinary():
    binnum = int(entrytextbin.get())
    binresult = binnum / 2
    return binresult

window = tk.Tk()
window.geometry('500x500')

frame = ttk.Frame(window, padding = "30 30 30 30")
frame.pack(fill = tk.BOTH, expand = True)

entrytextbin = tk.IntVar()
entrybin = ttk.Entry(frame, width = 25, textvariable = entrytextbin).pack()

binarybutton = ttk.Button(frame, text = "Binary", command = frombinary).pack()

solutionbin = ttk.Entry(frame, textvariable = binresult, state="readonly").pack()



window.mainloop()