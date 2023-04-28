import tkinter as tk
from tkinter import ttk # ttk - klasa do tworzenia label
from tkinter import scrolledtext # klasa do tworzenia scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox # moduł do tworzenia  komunikatów dla użytkownika
from klasa06ToolTip import createToolTip

win = tk.Tk()
win.title("Python GUI - Strefa Kursów")

# Tab Control
tabControl = ttk.Notebook(win) # tworzymy obiekt na klasie(metoddzie NoteBook)

tab1 = ttk.Frame(tabControl) # tworzymy 1 zakładkę i podpinamy dotabControl
tabControl.add(tab1, text="Tab 1") # dodajemy do naszego tabControl naszą zakładkę tab1 i definiujemy jej nazwę text="Tab 1"

tab2 = ttk.Frame(tabControl) # tworzymy 2 zakładkę
tabControl.add(tab2, text="Tab 2")

tabControl.pack(expand=1, fill="both", padx=10, pady=10) # fill="both" powoduje rozciągnięcie naszego tabControl do szerokości i wysokości naszego okna win (może być jeszcze fill="x" - rozciągnie tylko w poziomie, fill="y" - rozciągnie tylko w pionie)
# ja zastosowałem padx, pady aby część okna win była widoczna ( i działały nasze RadioButton z kolorami okna win) 
#____________________________________________________________________________
# dopinamy nasz GUI z 03 labelFrameWLabelFrame.py pod tab1 (zakładkę 1)
#____________________________________________________________________________

mainFrame = ttk.LabelFrame(tab1, text="Main Label Frame") # główna ramka (nie ma opcji background color- nie zmienimy koloru tła)
mainFrame.grid(column=0, row=0, columnspan=3, sticky= "W", padx= 10, pady= 10)

# label
aLabel = ttk.Label(mainFrame, text= "Pierwszy Label Michała") 
aLabel.grid(column= 0, row= 0)

# Modyfikacja funkcji klik button
def clickMe():
    action.configure(text= "Hello " + name.get() + " " + numberChosen.get())

# Zmieniamy nasz Label
aLabel.configure(text = "Enter a name: ") # nadpisujemy nasz aLabel
# ttk.Label(win, text = "Enter a name: ").grid(column = 0, row = 0) # gdybyśmy zostawili nowy przycisk w tym samym miejscu, przesłoniłby on stary aLabel

# Dodanie Textbox
name = tk.StringVar() # zmienna będzie przechowywała nasz wpisany w Textbox tekst
nameEntered = ttk.Entry(mainFrame, width= 12, textvariable= name) # tworzymy nowy obiekt o długości = 12(width = 12, pole do wpisania tekstu), będzie się on odnosił do naszej zmiennej name(textvariable = name)
nameEntered.grid(column= 0, row= 1, sticky= tk.W) # umieszczamy go w oknie

# Dodanie przycisku
action = ttk.Button(mainFrame, text= "kliknij mnie...", command= clickMe)
action.grid(column= 2, row= 1)
# action.configure(state = "disabled") # nasz obiekt(Button) będzie nieaktywny
nameEntered.focus() # spowoduje podświetlenie Textbox do wpisania tekst

# Dodanie Combobox(lista wartości rozwijana )
ttk.Label(mainFrame, text = "Wybierz numer: ").grid(column= 1, row= 0)
number = tk.StringVar # tworzymy zmienną, która przechowa nasz wprowadzony numer
numberChosen = ttk.Combobox(mainFrame, width= 12, textvariable= number) # tworzymy zmienną z naszym Combobox
# numberChosen = ttk.Combobox(win, width= 12, textvariable= number, state= "readonly")- dodanie zmiennej state= "readonly" zablokuje nam wpisywanie w naszym Combobox danych z klawiatury (będziemy mogli tylko wybrać z listy)
numberChosen["values"] = (1, 2, 4, 42, 100) # definiujemy naszą rozwijaną listę (w postaci krotki)
numberChosen.grid(column= 1, row= 1)
numberChosen.current(0) # określamy, który element krotki będzie wyświetlany jako pierwszy

# Dodanie przycisków Checkbox (nieaktywny zaznaczony)
chVarDis = tk.IntVar() # obiekt do przechowywania wartości z Checkbox
check1 = tk.Checkbutton(mainFrame, text= "disabled", variable=chVarDis, state= "disabled") # tworzymy Checkbox 1, state= disabled - nieaktywny
check1.select() # .select - będzie zaznaczony
check1.grid(column= 0, row= 4, sticky= tk.W) # sticky= tk.W - wyrównywanie do granicy West (E- East)

# Dodanie przycisków Checkbox (aktywny niezaznaczony)
chVarUn = tk.IntVar() 
check2 = tk.Checkbutton(mainFrame, text= "UnChecked", variable=chVarUn) 
check2.deselect() # .deselect - nie będzie zaznaczony
check2.grid(column= 1, row= 4, sticky= tk.W)

# Dodanie przycisków Checkbox (aktywny zaznaczony)
chVarEn = tk.IntVar() 
check3 = tk.Checkbutton(mainFrame, text= "Enabled", variable=chVarEn) 
check3.select() 
check3.grid(column= 2, row= 4, sticky= tk.W)

# RadioButton
Color1 = "Blue" #definiujemy kolory
Color2 = "Gold"
Color3 = "Red"

def radCall(): # tworzymy funkcję przypisującą kolor tła w zależności od naszego wyboru
    radSel = radVar.get() # tworzymy zmienną, która weźmie dane z naszej zmiennej przechowującej dane 
    if radSel == 1: win.configure(background=Color1)
    elif radSel == 2: win.configure(background=Color2)
    elif radSel == 3: win.configure(background=Color3)

radVar = tk.IntVar() # zmienna przechowująca dane z naszego RadioButton
rad1 = tk.Radiobutton(mainFrame, text=Color1, variable=radVar, value=1, command=radCall) # value=1 - radiobutton zwróci taką wartość, kiedy zostanie wciśnięty
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(mainFrame, text=Color2, variable=radVar, value=2, command=radCall) 
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(mainFrame, text=Color3, variable=radVar, value=3, command=radCall) 
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3) 

# RadioButton w pętli

colors = ["Green", "Black", "White"]

def radCall1():
    radSel1 = radVar1.get()  
    if radSel1 == 0: win.configure(background=colors[0])
    elif radSel1 == 1: win.configure(background=colors[1])
    elif radSel1 == 2: win.configure(background=colors[2])
    # for c in range(3):
    #     if radSel1 == c: win.configure(background=colors[c])          # można też użyć zapisu z pętlą for (przy dużej liczbie opcji)

radVar1 = tk.IntVar()
radVar1.set(99) # definiujemy radVar1 tak, aby nie była ona równa 0 lub 1 lub 2 (nie wyświetliła radsel1 w chwili uruchomienia skryptu)

for col in range(3):
    curRad = "rad" + str(col) # pętla przypisze nazwę curRad w zależności, jaki będzie col
    curRad = tk.Radiobutton(mainFrame, text=colors[col], variable= radVar1, value=col, command=radCall1)
    curRad.grid(column=col, row=6, sticky=tk.W)

# spinbox (widget-pole zawierające warości integer ze strzałkami góra/dół do ich ustawienia)
def _spin(): # Definiujemy akcję dla naszego spina
    value = spin.get() # pobieramy wartośc z naszego spin
    print(value) # wydruk do terminala naszej wartości spin
    scr.insert(tk.INSERT, value + " ") # umieszczamy nasz value w naszym scr(scrolled Text) z odpowiednim formatowaniem(arg 2) 

spin = Spinbox(mainFrame, from_=1, to=10, width=4, bd=4, command=_spin, relief='ridge') # from_=1, to=10 - zakres wyświetlanych int, width=4 szerokość w pikselach, bd=4 ramka w pikselach(bd od border)
spin.grid(column=0, row=7, sticky=tk.W)                                                 # relief="ridge" - formatowanie ramki (flat, groove, raised, ridge, solid, or sunken). Dopuszcza się zapis relief=tk.RIDGE"

# spinbox tooltips( podpowiedzi po najechaniu na element)
createToolTip(spin, "to nasz object spin ") # dodajemy podpowiedzi do obiektu spin (patrz opis klasy klasa06ToolTip)



# Scrolled Text Control - pole (podobne do Textbox) o ustalonej wysokości i szerokości
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(mainFrame, width=scrolW, height=scrolH, wrap= tk.WORD)# width- szerokość pola, high- wysokość pola, wrap=tk.WORD - dzielenie i zawijanie co całe słowa
scr.grid(column=0, columnspan=3, sticky= "WE") # columnspan = 3 - umieści nasze okno w naszych 3 już wykorzystywanych kolumnach

# scrolled text tooltips
createToolTip(scr, "To nasz object ScrolledText") # dodajemy podpowiedzi do obiektu scr

# Label Frame (Label otoczony ramką, w której mogą występować inne elementy)
labelsFrame = ttk.LabelFrame(mainFrame, text= "--- Labels in Frame ---") # tworzymy label Frame
# labelsFrame.grid(column=0, row=8, padx= 10, pady= 10)# padx- ustawienie do lewej i prawej, pady- ustawienie do góry i do dołu (odnosi się w tym przypadku do naszego okna win. W pikselach) 
labelsFrame.grid(column=0, row=9, sticky= "WE")# sticky= "WE" - wyrównanie do lewej i prawej (West, East) 
ttk.Label(labelsFrame, text= "Label1").grid(column=0, row=0) # tworzymy w nim labele (numeracja kolumn i rzędów od 0)
ttk.Label(labelsFrame, text= "Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text= "Label3").grid(column=0, row=2)

for child in labelsFrame.winfo_children(): # pętla pozwoli ustawić padding na poszczególne labels w LabelsFrame
    child.grid_configure(padx=10, pady=10) # ustawi padding dla każdego pojedyńczego label
# metoda child - pozwala odnieść się do naszych zdefiniowanych elementów labels w naszym LabelsFrame
# winfo_children() - pozyskuje informacje o położeniu naszych labels względem LabelFrame
# grid_configure() - pozwala skonfigurować nowe położenie dla poszczególnego elementu
# usunięcie text z LabelFrame pozwoli zobaczyć jak działa padding

# Menu
def _quit(): # akcja odpowiedzialna za zamknięcie naszego programu
    win.quit()
    win.destroy()
    exit()


menuBar = Menu(win) # tworzymy obiekt przypięty do okna win
win.config(menu=menuBar) # configurujemy, aby nasze okno odnosiło się do baszego MemuBar

# dodajemy elementy do naszego menu (add menu items)
fileMenu = Menu(menuBar, tearoff=0) # tworzymy obiekt menu w naszym menuBar. tearoff- wyłącza możliwośc przesuwania menu względem okna
fileMenu.add_command(label="New") # dodajemy w naszym fileMenu
fileMenu.add_command(label="Save")
fileMenu.add_separator() # tworzy separator pomiędzy etykietami
fileMenu.add_command(label="Exit", command=_quit) # korzystamy z def _quit - po kliknięciu zamkniemy okno win
menuBar.add_cascade(label="File", menu=fileMenu) # głownę pole w naszym menuBar(z niego rozwinie się możliwość kliknięcia "New"). File-->New

def _msgBoxAbout(): # tworzymy funkcję do wyświetlenia komunikatu dla użytkownika
    mBox.showinfo("Wiadomość", "Strefa kusrów - kurs Python") # showinfo("nazwa komunikatu", "treść komunikatu")- metoda wyświetli użytkownikowi komunikat (po wykonaniu akcji) 
def _msgBoxWarning(): # tworzymy funkcję do wyświetlenia komunikatu dla użytkownika
    mBox.showwarning("Ostrzeżenie", "Uwaga - Nowe kursy w strefie kursów. Zapraszam") # showwarning("nazwa komunikatu", "treść komunikatu")- metoda wyświetli użytkownikowi ostrzeżenie (po wykonaniu akcji)
def _msgBoxError(): # tworzymy funkcję do wyświetlenia komunikatu dla użytkownika
    mBox.showerror("Uwaga", "Aplikacja może nie działać prawidowo") # showerror("nazwa komunikatu", "treść komunikatu")- metoda wyświetli użytkownikowi error (po wykonaniu akcji)
def _msgBoxAskYesNo():
    answer = mBox.askyesno("Komunikat", "Czy jesteś zadowolony z kursu?") # przypisujemy zmienną do naszego pytania tak/nie
    print(answer) # jeśli tak, zwróci do konsoli True, nie - False
    
helpMenu = Menu(menuBar, tearoff=0) 
helpMenu.add_command(label="About", command=_msgBoxAbout) # podpinamy akcję  _msgBox do labela "About"
helpMenu.add_command(label="Warning", command=_msgBoxWarning) 
helpMenu.add_command(label="Error", command=_msgBoxError) 
helpMenu.add_command(label="Question", command=_msgBoxAskYesNo) 
menuBar.add_cascade(label="Help", menu=helpMenu)

#_____________________________________________________________________________________________________
# zagospodarowujemy Tab2
#_______________________________________________________________________________________________________

mainFrame2 = ttk.LabelFrame(tab2, text="Main Label Frame Tab2") 
mainFrame2.grid(column=0, row=0, columnspan=3, sticky= "W", padx= 10, pady= 10)

# Dodanie przycisków Checkbox (nieaktywny zaznaczony)
chVarDis = tk.IntVar() # obiekt do przechowywania wartości z Checkbox
check1 = tk.Checkbutton(mainFrame2, text= "disabled", variable=chVarDis, state= "disabled") # tworzymy Checkbox 1, state= disabled - nieaktywny
check1.select() # .select - będzie zaznaczony
check1.grid(column= 0, row= 4, sticky= tk.W) # sticky= tk.W - wyrównywanie do granicy West (E- East)

# Dodanie przycisków Checkbox (aktywny niezaznaczony)
chVarUn = tk.IntVar() 
check2 = tk.Checkbutton(mainFrame2, text= "UnChecked", variable=chVarUn) 
check2.deselect() # .deselect - nie będzie zaznaczony
check2.grid(column= 1, row= 4, sticky= tk.W)

# Dodanie przycisków Checkbox (aktywny zaznaczony)
chVarEn = tk.IntVar() 
check3 = tk.Checkbutton(mainFrame2, text= "Enabled", variable=chVarEn) 
check3.select() 
check3.grid(column= 2, row= 4, sticky= tk.W)

# RadioButton w pętli

colors2 = ["Green", "Black", "Gold"]

def radCall2():
    radSel2 = radVar2.get()  
    for c in range(3):
        if radSel2 == c: mainFrame2.configure(text=colors2[c])          # można też użyć zapisu z pętlą for (przy dużej liczbie opcji)

radVar2 = tk.IntVar()
radVar2.set(99) # definiujemy radVar1 tak, aby nie była ona równa 0 lub 1 lub 2 (nie wyświetliła radsel1 w chwili uruchomienia skryptu)

for col in range(3):
    curRad = "rad" + str(col) # pętla przypisze nazwę curRad w zależności, jaki będzie col
    curRad = tk.Radiobutton(mainFrame2, text=colors2[col], variable= radVar2, value=col, command=radCall2)
    curRad.grid(column=col, row=6, sticky=tk.W)

win.iconbitmap('./ikona2.ico') # pokaże naszą ikonę w oknie win
# img = tk.PhotoImage(file='@/media/micha/84CA-F753/python/basics/strefakursow/tkinter/ico.xbm')
# win.tk.call('wm', 'iconphoto', win._w, img)
# win.tk.call('wm', 'iconphoto', win._w, img)
#win.wm_iconbitmap('./media/micha/84CA-F753/python/basics/strefakursow/tkinter/ico.gif')
#win.iconphoto(False, tk.PhotoImage(file='./ico.gif'))
win.mainloop()