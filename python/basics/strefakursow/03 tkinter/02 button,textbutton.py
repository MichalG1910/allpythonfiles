import tkinter as tk
from tkinter import ttk # ttk - klasa do tworzenia label

win = tk.Tk() # tworzymy obiekt
win.title("Pierwsze okno w tkinter") # odwołujemy się do naszego obiektu i nadajemy mu nazwę 
# win.resizable(0,0) # nię będziemy mogli rozszerzyć okna (0,0)

# label
aLabel = ttk.Label(win, text = "Pierwszy Label") # tworzymy obiekt który będzie  label
aLabel.grid(column = 0, row = 0) # umieszczamy go w oknie

# Button Click Event Function
def clickMe(): # funkcja z różnymi zachowaniami naszych obiektów
    action.configure(text = "** Zostałem kliknięty! **") # konfigurujemy nasz obiekt(button) - będzie zawierał taki tekst
    aLabel.configure(text = "Drugi Label") # po naszej akcji(kliknięciu button) zmieni teks w naszym aLabel
    aLabel.configure(foreground = "red") # nowy tekst będzie miał kolor czerwony
    

# Adding a Button
action = ttk.Button(win, text = "Kliknij mnie", command = clickMe) # tworzymy nasz przycisk, command- odnosi się do naszej funkcji ze zdefiniowanymi 
action.grid(column = 1, row = 0) # umieszczamy go w oknie          # zachowaniami po kliknięciu naszego button


win.mainloop() # okno cały czas będzie wyświetlane