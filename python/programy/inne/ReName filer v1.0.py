import tkinter as tk
from tkinter import ttk
import os
import tkinter.filedialog as fd

class ReName():
    def __init__(self):

        self.win = tk.Tk()
        self.win.title("ReName filer v1.0")
        self.directory = None
        self.widgets()
        self.strLen = None
        self.dirButton.bind("<Button-1>", self.on_lbc)
        # self.win.iconbitmap('./ikona2.ico')
    
    def on_lbc(self, event):
        directory = fd.askdirectory()
        if directory:
            self.lok.delete(first=0, last=self.strLen)
            self.lok.insert(0, directory)
            self.strLen = len(directory)
        

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
        
    def start(self):
        numeration = ""
        location = self.location1.get()
        toConvert = self.toConvert1.get()
        afterConvert = self.afterConvert1.get()
        if self.chVarUn.get() == 1:
            numeration = self.numeration1.get()
        objs = os.listdir(location)
        if numeration == "":
            a = None
        else:
            a = int(numeration)
        for src in objs:
            full_src = os.path.join(location, src)
            if os.path.isfile(full_src):
                
                if afterConvert == "" and a != None:
                    afterCon = "0" + str(a) + ". " if a < 10 else str(a) + ". "
                    dst = src.replace(toConvert, afterCon)
                    a += 1
                elif afterConvert == "" and a == None:
                    dst = src.replace(toConvert, afterConvert)
                elif a == None:
                    dst = src.replace(toConvert, afterConvert)    
                else:
                    # dst = src.replace(toConvert, ( str(a)+ ". " + afterConvert))
                    afterCon = "0" + str(a) + ". " + afterConvert if a < 10 else str(a) + ". " + afterConvert
                    dst = src.replace(toConvert, afterCon)
                    a += 1

            if src != dst:
                full_dst = os.path.join(location, dst)
                os.rename(full_src, full_dst)
    def call(self):
        
        self.chCall = self.chVarUn.get()      
        if self.chCall == 1:
            self.optionalWidget()
        if self.chCall == 0:
            self.num.destroy()
            self.numLabel = ttk.Label(self.mainFrame, text = "                                   ").grid(column = 1, row = 8, sticky="WE") # przysłania

    def widgets(self):

        self.mainFrame = ttk.LabelFrame(self.win, text='Masowa zmiana nazwy plikow')
        self.mainFrame.grid(column=0, row=0,columnspan=3, sticky="W", padx=10, pady=10)
            
        ttk.Label(self.mainFrame, text = "lokalizacja katalogu:").grid(column = 1, row = 1)
        self.location1 = tk.StringVar()
        self.lok = ttk.Entry(self.mainFrame, text=self.directory, width= 35, textvariable= self.location1)   
        self.lok.grid(column= 1, row= 2, sticky="W")
        self.dirButton = ttk.Button(self.mainFrame, text= "DIR", width=3, command= self.on_lbc)
        self.dirButton.grid(column= 1, row= 2, sticky="E")

        ttk.Label(self.mainFrame, text = "Tekst do zmiany:").grid(column = 1, row = 3)
        self.toConvert1 = tk.StringVar() 
        toConv = ttk.Entry(self.mainFrame, width= 40, textvariable= self.toConvert1) 
        toConv.grid(column= 1, row= 4)

        ttk.Label(self.mainFrame, text = "Zmienić na:").grid(column = 1, row = 5)
        self.afterConvert1 = tk.StringVar() 
        aConv = ttk.Entry(self.mainFrame, width= 40, textvariable= self.afterConvert1) 
        aConv.grid(column= 1, row= 6)
        
        self.chVarUn = tk.IntVar() 
        check = tk.Checkbutton(self.mainFrame, text= "Wprowadzić numerację?", variable=self.chVarUn, command= self.call) 
        check.deselect() # .deselect - nie będzie zaznaczony
        check.grid(column= 1, row= 7, sticky= tk.W)

        exit = ttk.Button(self.mainFrame, text= "Quit", command= self._quit)
        exit.grid(column= 1, row= 9, sticky="E")

        action = ttk.Button(self.mainFrame, text= "Start", command= self.start)
        action.grid(column= 1, row= 9, sticky="W")

        self.numLabel = ttk.Label(self.mainFrame).grid(column = 1, row = 8, sticky="W",pady=5) # pełni rolę pustego rzędu

    def optionalWidget(self):   
        self.numLabel = ttk.Label(self.mainFrame, text = "Format numeracji:").grid(column = 1, row = 8, sticky="W")
        self.numeration1 = tk.StringVar()
        self.num = ttk.Entry(self.mainFrame, width= 6, textvariable=self.numeration1)
        self.num.grid(column= 1, row= 8, padx=85)
        
reOop = ReName()
reOop.win.mainloop()