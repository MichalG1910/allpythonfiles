import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI - Strefa Kursów")

# Tab Control
tabControl = ttk.Notebook(win) # tworzymy obiekt na klasie(metoddzie NoteBook)

tab1 = ttk.Frame(tabControl) # tworzymy 1 zakładkę i podpinamy dotabControl
tabControl.add(tab1, text="Tab 1") # dodajemy do naszego tabControl naszą zakładkę tab1 i definiujemy jej nazwę text="Tab 1"

tab2 = ttk.Frame(tabControl) # tworzymy 2 zakładkę
tabControl.add(tab2, text="Tab 2")

tabControl.pack(expand=1, fill="both") # zapis spowoduje rozciągnięcie naszego tabControl do szerokości i wysokości naszego okna win (fill="both", może być jeszcze fill="x" - rozciągnie tylko w poziomie, fill="y" - rozciągnie tylko w pionie)

# Widgets (do naszych Tab, aby nie były puste)
lFrame = ttk.LabelFrame(tab1, text="jestem elementem z tab1")
lFrame.grid(column=0, row=0, padx=10, pady=10)
ttk.Label(lFrame, text="Label1:").grid(column=0, row=0, sticky="W")

win.mainloop()