import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()
strData.set("Hello StringVar") # przekazanie daneych tekstowych do zmiennej

varData = strData.get() # zmienna varData bierze (get) dane z strData

print(varData) # Hello StringVar

# mamy inne typy klas do przechowywania zmiennych w tkinter
print(tk.IntVar) # <class 'tkinter.IntVar'>
print(tk.DoubleVar) # <class 'tkinter.DoubleVar'>
print(tk.BooleanVar) # <class 'tkinter.BooleanVar'>

intData = tk.IntVar()
print(intData) # PY_VAR1 (byłoby PY_VAR0, gdyby wcześniej nie było zmiennej strData)
print(intData.get()) # 0 (puste get() pobiera 0)
#win.mainloop()