import tkinter as tk
from tkinter import ttk # ttk - klasa do tworzenia label

win = tk.Tk() # tworzymy obiekt
win.title("Pierwsze okno w tkinter") # odwołujemy się do naszego obiektu i nadajemy mu nazwę 
# win.resizable(0,0) # nię będziemy mogli rozszerzyć okna (0,0)
ttk.Label(win, text = "Strefa kursów, pierwszy label").grid(column = 0, row = 0) # tworzymy nasz label. grid(column,row) - położenie naszego label
win.mainloop() # okno cały czas będzie wyświetlane

# https://trinket.io/pygame/f5af3f7500  paleta kolorów