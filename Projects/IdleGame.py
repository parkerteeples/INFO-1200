import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import time

currency = 0

def currencyupdate(currency):
    currency += 1
    game_window.after(1000, currencyupdate)
    return currency


def UpgradeMulti():
    print('Works')




game_window = tk.Tk()
game_window.title("Idle Game")

currencyVar = tk.IntVar()

currencylabel = ttk.Label(game_window, text='Currency: ').grid(column=0, row=0, padx=10, pady=10)
currentamount = ttk.Entry(game_window, width=25, textvariable=currency, state='readonly').grid(column=1, row=0, padx=10, pady=10)
multiplierbutton = ttk.Button(game_window, text='Upgrade Multiplier', command=UpgradeMulti).grid(column=0, row=1, padx=10, pady=10)



currencyupdate(currency)
game_window.mainloop()