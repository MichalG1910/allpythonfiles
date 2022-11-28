import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Witaj w Kursie python dla Zaawansowanych - Strefa Kursów")


mainFrame = ttk.LabelFrame(win, text="Main Label Frame")
mainFrame.grid(column=0, row=0, columnspan=3, sticky='W', padx=10, pady=10)

#Label
aLabel = ttk.Label(mainFrame, text="Tekst bez zmiany")
aLabel.grid(column=0, row=0)

# Modyfikacja funkcj klik button
def clickMe():
    action.configure(text='Hello ' + name.get() + " " + numberChosen.get())

# Zmien naszą label
aLabel.configure(text="Enter a name:")

# Dodanie Textbox
name = tk.StringVar()
nameEntered = ttk.Entry(mainFrame, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)

# Dodanie przycisku
action = ttk.Button(mainFrame, text="Kliknij mnie", command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')
nameEntered.focus()

ttk.Label(mainFrame, text="Wybierz numer:").grid(column=1,row=0)
number = tk.StringVar
numberChosen = ttk.Combobox(mainFrame, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# CheckBox

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mainFrame, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mainFrame, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mainFrame, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#Using scrolled Text Control

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(mainFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, sticky='WE')

# RadioButton

colors = ["Blue", "Gold", "Red"]

def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(mainFrame, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Label Frame
labelsFrame = ttk.LabelFrame(mainFrame, text=' --- Labels in Frame ---')
labelsFrame.grid(column=0, row=7, sticky='WE') # in pixel

ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=10, pady=10)



win.mainloop()