import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

def currencyupdate():
    currencyVar.set(currencyVar.get() + 1)
    game_window.after(1000, currencyupdate)

def UpgradeMulti():
    print('Works')

def main():
    currencyVar.set(0)
    currencyupdate()


game_window = tk.Tk()
game_window.title("Idle Game")

currencyVar = tk.IntVar()
multiplierVar = tk.IntVar()

currencylabel = ttk.Label(game_window, text='Money: ').grid(column=0, row=0, padx=5, pady=10)
currentamount = ttk.Entry(game_window, width=25, textvariable=currencyVar, state='readonly').grid(column=1, row=0, padx=5, pady=10)

mulitplierlabel = ttk.Label(game_window, text="Multiplier: ").grid(column=1, row=1, padx=5, pady=10)
multiplierbutton = ttk.Button(game_window, text='Upgrade Multiplier', command=UpgradeMulti).grid(column=0, row=1, padx=5, pady=10)
multiplieramount = ttk.Entry(game_window, width=25, textvariable=multiplierVar, state="readonly").grid(column=2, row=1, padx=5, pady=10)

if __name__ == "__main__":
    main()
    game_window.mainloop()