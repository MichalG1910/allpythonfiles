import tkinter as tk
from tkinter import ttk
import os, sys
import tkinter.filedialog as fd
from tkinter import PhotoImage
from tkinter import scrolledtext

class ReName():
    def __init__(self):

        self.win = tk.Tk()
        self.filePath = os.path.dirname(sys.argv[0])
        self.winStyle(self.win)
        self.win.title("ReName filer v1.0")
        self.directory = None
        self.widgets()
        self.preview()
        self.strLen = None
        self.dirButton.bind("<Button-1>", self.ask_dir)
        
        # self.win.iconbitmap('./ikona2.ico')

    def winStyle(self, window):
        window.tk.call('source', os.path.join(self.filePath, 'forest-dark.tcl'))
        ttk.Style().theme_use('forest-dark')
        #window.tk.call("LoadImages", "forest-dark")
    
    def ask_dir(self, event):
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
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 8, sticky="WE") # przysłania

    def widgets(self):

        self.mainFrame = ttk.LabelFrame(self.win, text='Masowa zmiana nazwy plików',labelanchor='n')
        self.mainFrame.grid(column=0, row=0,columnspan=1, sticky="WE", padx=10, pady=(10,10))
            
        ttk.Label(self.mainFrame, text = "lokalizacja katalogu:").grid(column = 0, row = 1,  padx=10, pady=(20,2))
        self.location1 = tk.StringVar()
        self.lok = ttk.Entry(self.mainFrame, text=self.directory, width= 34, textvariable= self.location1)   
        self.lok.grid(column= 0, row= 2, sticky="W", padx=10, pady=(0,5))
        
        self.icon = PhotoImage(file=f'{self.filePath}/folder24dp.png')
        TButton1 = ttk.Style()
        TButton1.configure("New.TButton", width = 5, border = 2, padding= {0,0,0,0})
        self.dirButton = ttk.Button(self.mainFrame, image= self.icon, command= self.ask_dir, style='New.TButton')
        self.dirButton.grid(column= 0, row= 2, sticky="NE", padx=10)

        ttk.Label(self.mainFrame, text = "Tekst do zmiany:").grid(column = 0, row = 3, padx=10, pady=(10,2))
        self.toConvert1 = tk.StringVar() 
        toConv = ttk.Entry(self.mainFrame, width= 40, textvariable= self.toConvert1) 
        toConv.grid(column= 0, row= 4, padx=10, pady=(0,5))

        ttk.Label(self.mainFrame, text = "Zmienić na:").grid(column = 0, row = 5, padx=10, pady=(10,2))
        self.afterConvert1 = tk.StringVar() 
        aConv = ttk.Entry(self.mainFrame, width= 40, textvariable= self.afterConvert1) 
        aConv.grid(column= 0, row= 6, padx=10, pady=(0,10))
        
        self.chVarUn = tk.IntVar() 
        check = ttk.Checkbutton(self.mainFrame, text= "Wprowadzić numerację?", variable=self.chVarUn, command= self.call) 
        #check.deselect() # .deselect - nie będzie zaznaczony
        check.grid(column= 0, row= 7, sticky= tk.W, padx=10, pady=10)

        exit = ttk.Button(self.mainFrame, text= "Quit", command= self._quit)
        exit.grid(column= 0, row= 9, sticky="E", padx=10, pady=10)

        action = ttk.Button(self.mainFrame, text= "Start", command= self.start)
        action.grid(column= 0, row= 9, sticky="W", padx=10, pady=10)

        self.numLabel = ttk.Label(self.mainFrame).grid(column = 0, row = 8, sticky="W", padx=10, pady=10) # pełni rolę pustego rzędu

    def preview(self):
        self.previewFrame = ttk.LabelFrame(self.win, text='Podgląd',labelanchor='n')
        self.previewFrame.grid(column=1, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.scrolledText = tk.Text(self.previewFrame, width=48, height=22, wrap= tk.NONE, background='grey', foreground='black')
        self.scrolledText.grid(column= 1, row= 0, rowspan=8, sticky="NSEW", padx=(10,10), pady=(10,10))

        vsb = ttk.Scrollbar(self.previewFrame, command=self.scrolledText.yview, orient="vertical")
        hsb = ttk.Scrollbar(self.previewFrame, command=self.scrolledText.xview, orient="horizontal")
        self.scrolledText.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.grid(column=2, row=0, rowspan=8, sticky="ns", padx=2)
        hsb.grid(column=1, row=9, sticky="ew", padx=2)   
                

    def optionalWidget(self):   
        self.numLabel = ttk.Label(self.mainFrame, text = "Format numeracji:").grid(column = 0, row = 8, sticky="W", padx=10, pady=10)
        self.numeration1 = tk.StringVar()
        self.num = ttk.Entry(self.mainFrame, width= 6, textvariable=self.numeration1)
        self.num.grid(column= 0, row= 8)
        
reOop = ReName()
reOop.win.mainloop()