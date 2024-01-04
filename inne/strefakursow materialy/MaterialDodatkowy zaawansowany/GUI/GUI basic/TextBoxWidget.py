import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Witaj w Kursie python dla Zaawansowanych - Strefa Kursów")

#Label
aLabel = ttk.Label(win, text="Tekst bez zmiany")
aLabel.grid(column=0, row=0)

# Modyfikacja funkcj klik button
def clickMe():
    action.configure(text='Hello ' + name.get())

# Zmien naszą label
aLabel.configure(text="Enter a name:")

# Dodanie Textbox
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Dodanie przycisku
action = ttk.Button(win, text="Kliknij mnie", command=clickMe)
action.grid(column=1, row=1)
#action.configure(state='disabled')
nameEntered.focus()

win.mainloop()