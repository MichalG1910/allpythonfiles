import tkinter as tk
from tkinter import ttk
import os, sys
import tkinter.filedialog as fd
from tkinter import PhotoImage

class ReName():
    def __init__(self):

        self.win = tk.Tk()
        self.filePath = os.path.dirname(sys.argv[0])
        self.winStyle(self.win)
        self.win.title("ReName filer v1.0")
        self.directory = None
        self.widgets()
        self.previewWidgets()
        self.strLen = None
        self.dirButton.bind("<Button-1>", self.ask_dir)
        # self.win.iconbitmap('./ikona2.ico')
    
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
        
    def winStyle(self, window):
        window.tk.call('source', os.path.join(self.filePath, 'forest-dark.tcl'))
        ttk.Style().theme_use('forest-dark')
    
    def ask_dir(self, event):
        self.directory = fd.askdirectory()
        self.beforePreview()
    
    def beforePreview(self):
        objsPreviewLenList, multiplierList, winWidthDict = [],[],{}
        if self.directory:
            self.lok.delete(first=0, last=self.strLen)
            self.lok.insert(0, self.directory)
            self.strLen = len(self.directory)
            self.objsPreview = os.listdir(self.location1.get())
            self.objsPreview.sort()
            self.previewText.configure(state="normal")
            self.previewText.delete('1.0', tk.END)
            a = 0
            for f in self.objsPreview:
                self.previewText.insert(tk.INSERT, f"{f}\n")
                self.stringLetterLowerUpper(f)
                objsPreviewLenList.append(len(self.objsPreview[a]))
                multiplierList.append(self.multiplier)
                winWidthDict[len(self.objsPreview[a])] = self.multiplier
                a += 1
            self.previewText.configure(width=max(objsPreviewLenList)+round(max(objsPreviewLenList)*(winWidthDict[max(objsPreviewLenList)] / 3.2)))
            self.previewText.configure(state="disabled")

    def start(self, preview = 'no'):
        numeration = ""
        location = self.location1.get()
        try:
            toConvert = self.previewText.selection_get() 
            self.toConvert1.set(toConvert)
        except:    
            toConvert = self.toConvert1.get() 
        
        afterConvert = self.afterConvert1.get()
        if self.chVarUn.get() == 1:
            numeration = self.numeration1.get()
        #self.objs = os.listdir(location)
        if numeration == "":
            a = None
        else:
            a = int(numeration)
        self.oldNameLenList, self.newNameList = [],[]
        for oldName in self.objsPreview:
            full_oldName = os.path.join(location, oldName)
            if os.path.isfile(full_oldName):
                
                if afterConvert == "" and a != None:
                    afterCon = "0" + str(a) + ". " if a < 10 else str(a) + ". "
                    self.newName = oldName.replace(toConvert, afterCon, 1)
                    a += 1
                elif afterConvert == "" and a == None:
                    self.newName = oldName.replace(toConvert, afterConvert, 1)
                elif a == None:
                    self.newName = oldName.replace(toConvert, afterConvert, 1)    
                else:
                    # newName = oldName.replace(toConvert, ( str(a)+ ". " + afterConvert))
                    afterCon = "0" + str(a) + ". " + afterConvert if a < 10 else str(a) + ". " + afterConvert
                    self.newName = oldName.replace(toConvert, afterCon, 1)
                    a += 1

            if oldName != self.newName:
                full_newName = os.path.join(location, self.newName)
                if preview == 'no':
                    os.rename(full_oldName, full_newName)
            self.oldNameLenList.append(len(oldName))
            self.newNameList.append(self.newName)
                
        if preview == 'no':
            self.toConvert1.set('')
            self.afterConvert1.set('')
            self.previewTextAfter.configure(state='normal')
            self.previewTextAfter.delete('1.0', tk.END)
            self.previewTextAfter.configure(state='disabled')
            self.beforePreview()

            self.backButton.configure(state='normal')
    
    def activateOptionalWidget(self):
        self.chCall = self.chVarUn.get()      
        if self.chCall == 1:
            self.optionalWidget()
        if self.chCall == 0:
            self.num.destroy()
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 8, sticky="WE") # przysłania

    def widgets(self):
        self.location1 = tk.StringVar()
        self.toConvert1 = tk.StringVar()
        self.afterConvert1 = tk.StringVar()
        self.chVarUn = tk.IntVar()

        self.mainFrame = ttk.LabelFrame(self.win, text='Masowa zmiana nazwy plików',labelanchor='n')
        self.mainFrame.grid(column=0, row=0,columnspan=1, sticky="NSWE", padx=10, pady=(10,10))
            
        ttk.Label(self.mainFrame, text = "lokalizacja katalogu:").grid(column = 0, row = 1,  padx=10, pady=(20,2))
        self.lok = ttk.Entry(self.mainFrame, text=self.directory, width= 34, textvariable= self.location1)   
        self.lok.grid(column= 0, row= 2, sticky="W", padx=10, pady=(0,5))
        
        self.icon = PhotoImage(file=f'{self.filePath}/folder24dp.png')
        TButton1 = ttk.Style()
        TButton1.configure("New.TButton", width = 5, border = 2, padding= {0,0,0,0})
        self.dirButton = ttk.Button(self.mainFrame, image= self.icon, command= self.ask_dir, style='New.TButton')
        self.dirButton.grid(column= 0, row= 2, sticky="NE", padx=10)

        ttk.Label(self.mainFrame, text = "Tekst do zmiany:").grid(column = 0, row = 3, padx=10, pady=(10,2))
        toConv = ttk.Entry(self.mainFrame, width= 40, textvariable= self.toConvert1) 
        toConv.grid(column= 0, row= 4, padx=10, pady=(0,5))

        ttk.Label(self.mainFrame, text = "Zmienić na:").grid(column = 0, row = 5, padx=10, pady=(10,2))
        self.afterConvert1 = tk.StringVar() 
        aConv = ttk.Entry(self.mainFrame, width= 40, textvariable= self.afterConvert1) 
        aConv.grid(column= 0, row= 6, padx=10, pady=(0,10))
        
         
        check = ttk.Checkbutton(self.mainFrame, text= "Wprowadzić numerację?", variable=self.chVarUn, command= self.activateOptionalWidget) 
        check.grid(column= 0, row= 7, sticky= tk.W, padx=10, pady=10)
        
        startButton = ttk.Button(self.mainFrame, text= "Start", command= self.start)
        startButton.grid(column= 0, row= 9, sticky="W", padx=10, pady=10)
        
        previewButton = ttk.Button(self.mainFrame, text= "Podgląd", command= self._preview)
        previewButton.grid(column= 0, row= 9, sticky="N", padx=10, pady=10)
        
        exitButton = ttk.Button(self.mainFrame, text= "Zamknij", command= self._quit)
        exitButton.grid(column= 0, row= 9, sticky="E", padx=10, pady=10)
        
        disabledButton = ttk.Style()
        disabledButton.configure("DS.TButton", foregroundg='#blue', bg='black')
        self.backButton = ttk.Button(self.mainFrame, text= "Cofnij", command= self._back, style='DS.TButton')
        self.backButton.grid(column= 0, row= 10, sticky="W", padx=10, pady=(0,10))
        
        
        clearButton = ttk.Button(self.mainFrame, text= "Wyczyść", command= self._clear)
        clearButton.grid(column= 0, row= 10, sticky="N", padx=10, pady=(0,10))
        
        self.numLabel = ttk.Label(self.mainFrame).grid(column = 0, row = 8, sticky="W", padx=10, pady=10) # pełni rolę pustego rzędu

    def optionalWidget(self): 
        self.numeration1 = tk.StringVar()

        self.numLabel = ttk.Label(self.mainFrame, text = "Format numeracji:").grid(column = 0, row = 8, sticky="W", padx=10, pady=10)
        self.num = ttk.Entry(self.mainFrame, width= 6, textvariable=self.numeration1)
        self.num.grid(column= 0, row= 8)

    def previewWidgets(self):
        def multiple_yview(*args):
            self.previewText.yview(*args)
            self.previewTextAfter.yview(*args)
        def on_textscroll(*args):
            vsb.set(*args)
            multiple_yview('moveto', args[0])
        
        self.previewFrame = ttk.LabelFrame(self.win, text='Podgląd',labelanchor='n')
        self.previewFrame.grid(column=1, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.previewText = tk.Text(self.previewFrame, width=48, height=23, wrap= tk.NONE, background='white', foreground='black')
        self.previewText.grid(column= 1, row= 0, rowspan=8, sticky="NSEW", padx=(10,0), pady=(10,10))
        self.previewTextAfter = tk.Text(self.previewFrame, width=48, height=23, wrap= tk.NONE, background='white', foreground='black',)
        self.previewTextAfter.grid(column= 2, row= 0, rowspan=8, sticky="NSEW", padx=(0,10), pady=(10,10))

        vsb = ttk.Scrollbar(self.previewFrame, command=multiple_yview, orient="vertical")
        #hsb = ttk.Scrollbar(self.previewFrame, command=(self.previewText.xview==self.previewTextAfter.xview), orient="horizontal",)
        self.previewText.configure(yscrollcommand=on_textscroll)
        self.previewTextAfter.configure(yscrollcommand=on_textscroll)
        #self.previewTextAfter.configure(yscrollcommand=vsb.set)
        vsb.grid(column=3, row=0, rowspan=8, sticky="ns", padx=2)
        #hsb.grid(column=1, row=9, sticky="ew", padx=2)
    
    def stringLetterLowerUpper(self, string):
        upperLetter = len([i for i in string if i.isupper()==True])
        self.multiplier = upperLetter / len(string)
    
    def _preview(self):
        multiplierList, newNameLenList, winWidthDict = [],[],{}
        a = 1
        self.generatePreview = 'yes'
        
        self.start(self.generatePreview)
        self.beforePreview()
        
        self.previewTextAfter.configure(state='normal')
        self.previewTextAfter.delete('1.0', tk.END)
        self.objsPreview.sort()
        for f in range(len(self.newNameList)):
            self.previewTextAfter.insert(tk.INSERT, f"{self.newNameList[f]}\n") 
            self.stringLetterLowerUpper(self.newNameList[f])
            startIndex = self.objsPreview[f].find(self.toConvert1.get())
            endIndexBefore = startIndex + len(self.toConvert1.get())
            endIndexAfter = startIndex + len(self.afterConvert1.get())
            if startIndex != -1:
                self.previewText.tag_add("before", f"{a}.{startIndex}", f"{a}.{endIndexBefore}")
                self.previewText.tag_configure("before", background="white", foreground="red") 
                self.previewTextAfter.tag_add("after", f"{a}.{startIndex}", f"{a}.{endIndexAfter}")
                self.previewTextAfter.tag_configure("after", background="white", foreground="green")
            a += 1
            multiplierList.append(self.multiplier)
            newNameLenList.append(len(self.newNameList[f]))
            winWidthDict[len(self.newNameList[f])] = self.multiplier
        self.previewTextAfter.configure(width=max(newNameLenList)+round(max(newNameLenList)*(winWidthDict[max(newNameLenList)] / 3.2)))
        self.previewTextAfter.configure(state='disabled')
    
    def _back(self):
        pass
    def _clear(self):
        self.previewText.configure(state='normal', width=48)
        self.previewText.delete('1.0', tk.END)
        self.previewText.configure(state='disabled')
        
        self.previewTextAfter.configure(state='normal', width=48)
        self.previewTextAfter.delete('1.0', tk.END)
        self.previewTextAfter.configure(state='disabled')

        self.location1.set('')
        self.toConvert1.set('')
        self.afterConvert1.set('')
        self.numeration1.set('')
        self.chVarUn.set(0)
        self.activateOptionalWidget()
        
reOop = ReName()
reOop.win.mainloop()