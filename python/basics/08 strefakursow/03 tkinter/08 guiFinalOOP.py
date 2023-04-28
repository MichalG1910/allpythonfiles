#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
import klasa06ToolTip as tt
from tkinter import messagebox as mBox

from threading import Thread # klasa umożliwiająca wywoływanie wątków

GLOBAL_CONST = 42

#===================================================================
class OOP():
    def __init__(self):
        # Create instance (okno)
        self.win = tk.Tk()
        
        # tooltip do okna
        tt.createToolTip(self.win, 'Hello GUI.')

        # Add a title
        self.win.title("Python GUI")
        
        # tworzymy nasze Widgety
        self.createWidgets()
    
    # definiujemy wszystkie akcje(będą powiązane z command w widget)
    # Button callback
    def clickMe(self):
        self.action.configure(text='Hello ' + self.name.get()+ " " + self.numberChosen.get())

    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT, value + ' ')

    # Checkbox callback (nie było tego)
    def checkCallback(self, *ignoredArgs):
        # only enable one checkbutton (tylko jeden checkbox może być zaznaczony)
        if self.chVarUn.get(): self.check3.configure(state='disabled') # jeżeli self.chVarUn(check2) = True (zostanie zaznaczony) to check3 - state=disabled (będzie nieaktywny)
        else:             self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled') # check3 zaznaczony --> check2 nieaktywny
        else:             self.check2.configure(state='normal')

    # Radiobutton callback function
    def radCall(self):
        radSel=self.radVar.get()
        if   radSel == 0: self.win.configure(background=self.colors[0])
        elif radSel == 1: self.win.configure(background=self.colors[1])
        elif radSel == 2: self.win.configure(background=self.colors[2])
        elif radSel == 3: self.win.configure(background=self.colors[3])
        elif radSel == 4: self.win.configure(background=self.colors[4])
        elif radSel == 5: self.win.configure(background=self.colors[5])

    def radCall2(self):
        radSel2 = self.radVar2.get()  
        for c in range(3):
            if radSel2 == c: self.mainFrame2.configure(text=self.colors2[c])

    # helpMenu callback functions
    def _msgBoxAbout(self):
        mBox.showinfo("Wiadomość", "Strefa kusrów - kurs Python")  
    def _msgBoxWarning(self): 
        mBox.showwarning("Ostrzeżenie", "Uwaga - Nowe kursy w strefie kursów. Zapraszam") 
    def _msgBoxError(self): 
        mBox.showerror("Uwaga", "Aplikacja może nie działać prawidowo") 
    def _msgBoxAskYesNo(self):
        answer = mBox.askyesno("Komunikat", "Czy jesteś zadowolony z kursu?") 
        print(answer)

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
    
    def methodInAThread(self):
        print('Hi, how are you')

    def usingGlobal(self):
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)

    #####################################################################################
    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control

        tab1 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab1, text='Tab 1')      # Add the tab

        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Tab 2')      # Make second tab visible

        tabControl.pack(expand=1, fill="both", padx=10, pady=10)  # Pack to make visible
        # ~ Tab Control introduced here -----------------------------------------

        # We are creating a container frame to hold all other widgets
        self.mainFrame = ttk.LabelFrame(tab1, text='Main label Frame')
        self.mainFrame.grid(column=0, row=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Changing our Label
        ttk.Label(self.mainFrame, text="Enter a name:").grid(column=0, row=0)

        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.mainFrame, width=12, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        self.action = ttk.Button(self.mainFrame, text="kliknij mnie...", command=self.clickMe)
        self.action.grid(column=2, row=1)
        
        # adding a Combobox
        ttk.Label(self.mainFrame, text="Wybierz numer:").grid(column=1, row=0)
        number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.mainFrame, width=12, textvariable=number)
        self.numberChosen['values'] = (1, 2, 4, 42, 100)
        self.numberChosen.grid(column=1, row=1)
        self.numberChosen.current(0)

        # Creating three checkbox
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mainFrame, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=4, sticky=tk.W)

        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.mainFrame, text="UnChecked", variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=4, sticky=tk.W )

        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.mainFrame, text="Toggle", variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=4, sticky=tk.W)

        # trace the state of the two checkbuttons
        self.chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())
        self.chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())
        
        # Radiobutton list
        self.colors = ["Blue", "Gold", "Red", "Green", "Black", "White"]

        self.radVar = tk.IntVar()

        # Selecting a non-existing index value for radVar
        self.radVar.set(99)

        # Creating all three Radiobutton widgets within one loop
        for col in range(6):
            curRad = 'rad' + str(col)
            curRad = tk.Radiobutton(self.mainFrame, text=self.colors[col], variable=self.radVar, value=col, command=self.radCall)
            if col < 3: curRad.grid(column=col, row=5, sticky=tk.W)
            else: curRad.grid(column=col-3, row=6, sticky=tk.W)
            # And now adding tooltips
            tt.createToolTip(curRad, 'This is a Radiobutton control.')
        # Adding a Spinbox widget using a set of values
        self.spin = Spinbox(self.mainFrame, values=(1, 2, 4, 42, 100), width=4, bd=4, command=self._spin, relief="ridge")
        self.spin.grid(column=0, row=7, sticky="W")

        # Using a scrolled Text control
        scrolW  = 30; scrolH  =  3
        self.scr = scrolledtext.ScrolledText(self.mainFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, sticky='WE', columnspan=3)

        # Create a container to hold labels
        labelsFrame = ttk.LabelFrame(self.mainFrame, text='--- Labels in Frame ---')
        labelsFrame.grid(column=0, row=9, sticky="WE")

        # Place labels into the container element - vertically
        ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
        ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
        ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

        # Add some space around each label
        for child in labelsFrame.winfo_children():
            child.grid_configure(padx=10, pady=10)


        # Creating a Menu Bar
        menuBar = Menu(self.win)
        self.win.config(menu=menuBar)

        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_command(label="Save")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Add another Menu to the Menu Bar and an item
        self.helpMenu = Menu(menuBar, tearoff=0) 
        self.helpMenu.add_command(label="About", command=self._msgBoxAbout) # podpinamy akcję  _msgBox do labela "About"
        self.helpMenu.add_command(label="Warning", command=self._msgBoxWarning) 
        self.helpMenu.add_command(label="Error", command=self._msgBoxError) 
        self.helpMenu.add_command(label="Question", command=self._msgBoxAskYesNo) 
        menuBar.add_cascade(label="Help", menu=self.helpMenu)

        # Tab Control 2 refactoring  -----------------------------------------
        # We are creating a container frame to hold all other widgets -- Tab2
        self.mainFrame2 = ttk.LabelFrame(tab2, text='Main Label Frame Tab2')
        self.mainFrame2.grid(column=0, row=0, padx=8, pady=4)
        
        # Creating three checkbox
        chVarDis = tk.IntVar() 
        check1 = tk.Checkbutton(self.mainFrame2, text= "disabled", variable=chVarDis, state= "disabled")
        check1.select() 
        check1.grid(column= 0, row= 4, sticky= tk.W) 

        chVarUn = tk.IntVar() 
        check2 = tk.Checkbutton(self.mainFrame2, text= "UnChecked", variable=chVarUn) 
        check2.deselect() 
        check2.grid(column= 1, row= 4, sticky= tk.W)

        chVarEn = tk.IntVar() 
        check3 = tk.Checkbutton(self.mainFrame2, text= "Enabled", variable=chVarEn) 
        check3.select() 
        check3.grid(column= 2, row= 4, sticky= tk.W)
        
        # creating radioButton Tab2
        self.colors2 = ["Green", "Black", "Gold"]
        self.radVar2 = tk.IntVar()
        self.radVar2.set(99) 

        for col in range(3):
            curRad = "rad" + str(col) 
            curRad = tk.Radiobutton(self.mainFrame2, text=self.colors2[col], variable= self.radVar2, value=col, command=self.radCall2)
            curRad.grid(column=col, row=6, sticky=tk.W)
        
        # ~ Tab Control 2 refactoring  -----------------------------------------
        
        # adding iconbitmap to mainWindow
        # self.win.iconbitmap('./ikona2.ico')

        # Using tkinter Variable Classes
        strData = tk.StringVar()
        strData.set('Hello StringVar')
        print(strData.get())

        # Default tkinter Variable Classes
        intData = tk.IntVar()
        print(intData.get())
        print(tk.DoubleVar())
        print(tk.BooleanVar())

        # It is not necessary to create a tk.StringVar()
        strData = tk.StringVar()
        strData = self.spin.get()
        print("Hello " + strData)

        # Printing the Global works
        print(GLOBAL_CONST)

        # call method
        self.usingGlobal()

        # Place cursor into name Entry
        nameEntered.focus()

        # Add a Tooltip to the Spinbox
        tt.createToolTip(self.spin, 'This is a Spin control.')

        # Add Tooltips to more widgets
        tt.createToolTip(nameEntered, 'This is an Entry control.')
        tt.createToolTip(self.action, 'This is a Button control.')
        tt.createToolTip(self.scr,    'This is a ScrolledText control.')

#======================
# Start GUI
#======================
oop = OOP()

runT = Thread(target=oop.methodInAThread)

oop.win.mainloop()
