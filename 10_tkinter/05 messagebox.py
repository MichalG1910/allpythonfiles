from tkinter import messagebox as mBox
from tkinter import Tk

root = Tk() # tworzymy okno
root.withdraw()  # spowoduje wyświetlenie naszego mBox i nie wyświetlenie okna
mBox.showinfo("Tytuł komunikatu", "Treść komunikatu")
root.mainloop()

# może być przydatne w przypadku błedu programu