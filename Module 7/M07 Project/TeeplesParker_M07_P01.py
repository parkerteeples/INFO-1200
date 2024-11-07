#Name: Parker Teeples
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section number
#Professor: Tyler Bartholomew
#Date: 11/4/24
#Project #: M07_P1
#By submitting this assignment, I declare that the source code contained in this assignment was written s
#olely by me, unless specifically provided in the assignment. I attest that no part of this assignment, i
#n whole or in part, was generated by Generative Artificial Intelligence (e.g., ChatGPT, Gemini, Copilot, 
#Claude, etc.) nor obtained from a paid solution service (e.g., Chegg, Course Hero, Bartleby, etc.). I un
#derstand that copying any source code, in whole or in part, constitutes cheating, and that I will receiv
#e a zero on this project if I am found in violation of this policy.

import tkinter as tk # import tkinter as tk
from tkinter import ttk, messagebox # from tkinter import ttk and messagebox

def solve():
    numset = '1234567890.' # numbers allowed to continue
    num = (avar.get()) + (bvar.get())
    num = str(num) # make num the a side and b side
    for char in num: # loop for the amount of charicters in mum
        if char not in numset: # if charicter is not in numset
            messagebox.showerror("Error","This Is Not a Valid Entry") # display error message
            return # return
        else: # if is in numset
            pass # pass
    a2 = float(avar.get()) ** 2 # square side a
    b2 = float(bvar.get()) ** 2 # square side b
    c = round(((a2 + b2) ** 0.5), 3) # calculate for side c
    cvar.set(c) # set cvar as c

root = tk.Tk() # set window as root
root.geometry('500x500+2500+100') # set window geometry
frame = ttk.Frame(root, padding = "30 30 30 30").pack() # set frame
root.title('Pythagorean Theorem Calculator') # make window title as 'Pythagorean Theorem Calculator'

avar = tk.StringVar()# set avar as a string variable
bvar = tk.StringVar()# set bvar as a string variable
cvar = tk.IntVar()# set cvar as a string variable


labela = tk.Label(frame, text = 'Enter Side A: ').pack() # label for entry a
entrya = tk.Entry(frame, width = 25, textvariable = avar).pack() # entry for a
labelb = tk.Label(frame, text = 'Enter Side B: ').pack() # label for entry b
entryb = tk.Entry(frame, width = 25, textvariable = bvar).pack() # entry for b
labelc = tk.Label(frame, text = 'Side C: ').pack() # label for entry c
entryc = tk.Entry(frame, width = 25, textvariable = cvar, state = "readonly").pack() # read only text entry for displaying c
buttonsolve = tk.Button(frame, text = 'Calculate', command = solve).pack() # button to solve

root.mainloop() # root mainloop