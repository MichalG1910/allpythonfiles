import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Witaj w Kursie python dla Zaawansowanych - Strefa Kursów")

#Label
aLabel = ttk.Label(win, text="Tekst bez zmiany")
aLabel.grid(column=0, row=0)

# Modyfikacja funkcj klik button
def clickMe():
    action.configure(text='Hello ' + name.get() + " " + numberChosen.get())

# Zmien naszą label
aLabel.configure(text="Enter a name:")

# Dodanie Textbox
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Dodanie przycisku
action = ttk.Button(win, text="Kliknij mnie", command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')
nameEntered.focus()

ttk.Label(win, text="Wybierz numer:").grid(column=1,row=0)
number = tk.StringVar
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

win.mainloop()