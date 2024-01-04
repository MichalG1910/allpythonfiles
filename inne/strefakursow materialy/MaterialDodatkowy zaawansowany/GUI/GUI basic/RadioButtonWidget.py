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

# CheckBox

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

# RadioButton

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

win.mainloop()