import tkinter as tk
from tkinter import ttk
import os, sys
import tkinter.filedialog as fd
from tkinter import PhotoImage
from os import listdir

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
        self._tree(self.win, path='\\')
        #self.tree.bind('<Double-Button-1>', self.selectItem)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.treeLoc = ''
        #self.traceFolder()
        # self.win.iconbitmap('./ikona2.ico')
       
    def OnDoubleClick(self, event):
        item = self.tree.selection()[0]
        parent_iid = self.tree.parent(item)
        node = []
        # go backward until reaching root
        while parent_iid != '':
            node.insert(0, self.tree.item(parent_iid)['text'])
            parent_iid = self.tree.parent(parent_iid)
        i = self.tree.item(item, "text")
        path = os.path.join(*node, i)
        print(path) # zamien \ na /
        self.location1.set(path)
        self.beforePreview()
    '''
    def selectItem(self, event):
        curItem = self.tree.focus()
        self.treeLoc = self.treeLoc + self.tree.item(curItem)['text']
        self.location1.set(self.treeLoc)
        print (self.tree.item(curItem))
    '''
    '''
    def selectItem(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        print ('curItem = ', curItem)
        print ('col = ', col)

        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        print ('cell_value = ', cell_value)
'''
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
    
    
    '''
    def folderSelection1(self, *ignoredArgs):
        print('aaa')
        self.location = self.tree.selection_get()
        print(self.location)
        self.location1.set(self.location)
        
    def traceFolder(self):         
        self.location1.trace('w', lambda unused0, unused1, unused2 : self.folderSelection1())
     '''   
    
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
        separator = ""
        self.location = self.location1.get()
        afterConvert = self.afterConvert1.get()
        self.oldNameLenList, self.newNameList, self.addNumList = [],[],[]
        
        try:
            toConvert = self.previewText.selection_get() 
            self.toConvert1.set(toConvert)
        except:    
            toConvert = self.toConvert1.get()

        #print(f'chvarun: {self.chVarUn.get()}')
        #print(f'standard: {self.standardVar.get()}   series: {self.seriesVar.get()}')
        if self.chVarUn.get() == 1 and self.standardVar.get() == 1:
            numeration = int(self.standardNumeration.get())
            separator = self.sepVar.get()
        elif self.chVarUn.get() == 1 and self.seriesVar.get() == 1:
            numeration = int(self.seriesNumeration1.get())
            numeration2 = int(self.seriesNumeration2.get())
            separator = self.sepVar.get()
        else: numeration = None
        #self.objs = os.listdir(location)
        '''
        if numeration == "":
            a = None
        else:
            a = int(numeration)
             
            b = int(numeration2)
        '''
        
        for oldName in self.objsPreview:
            full_oldName = os.path.join(self.location, oldName)
            if os.path.isfile(full_oldName):
                
                if numeration != None:                               # samo dodanie numeracji
                    if self.chVarUn.get() == 1 and self.standardVar.get() == 1:             # zwykła
                        addNum = "0" + str(numeration) + separator  if numeration < 10 else str(numeration) + separator 
                        self.newName = addNum + oldName.replace(toConvert, afterConvert, 1)
                        numeration += 1
                    else:
                        addNum = "S0" + str(numeration) + "E0" + str(numeration2) + separator if numeration2 < 10 else "S0" + str(numeration) + "E" + str(numeration2) + separator
                        self.newName = addNum + oldName.replace(toConvert, afterConvert, 1)
                        numeration2 += 1
                    self.addNumList.append(addNum)

                else:                                               # standardowa zamiana/usuniecie części nazwy bez zamiany na inną bez numeracji
                    self.newName = oldName.replace(toConvert, afterConvert, 1)    
                    
            if oldName != self.newName:
                full_newName = os.path.join(self.location, self.newName)
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
            self.oldNameList = self.objsPreview
            self.beforePreview()

            self.backButton.configure(state='normal')
    
    def activateOptionalWidget(self):
        self.chCall = self.chVarUn.get()      
        if self.chCall == 1:
            self.optionalWidget()
        if self.chCall == 0:
            self.num.destroy()
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 8, sticky="NSWE") # przysłania
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 9, sticky="NSWE") # przysłania
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 10, sticky="NSWE") # przysłania
    
    def optionalWidget(self): 
        self.standardNumeration = tk.StringVar()
        self.seriesNumeration1 = tk.StringVar()
        self.seriesNumeration2 = tk.StringVar()
        self.standardVar = tk.IntVar()
        self.seriesVar = tk.IntVar()
        self.sepVar = tk.StringVar()
        self.trace()
        
        def activateStandardEntry():
            try:
                self.numLabel.destroy()
                self.num.destroy()
                del self.numLabel, self.num 
                self.numLabel1.destroy()
                self.num1.destroy()
                del self.numLabel1, self.num
            except: pass
            
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 10, sticky="NSWE") # przysłania
            self.numLabel = ttk.Label(self.mainFrame, text = "Zacznij od:").grid(column = 0, row = 10, sticky="W", padx=10, pady=2)
            self.num = ttk.Entry(self.mainFrame, width= 6, textvariable=self.standardNumeration)
            self.num.grid(column= 0, row= 10, sticky = "W", padx=(80,0))
            self.sepLabel = ttk.Label(self.mainFrame, text = "separator:").grid(column = 0, row = 10, sticky="W", padx=(180,0), pady=2)
            self.sepEntry = ttk.Entry(self.mainFrame, width= 4, textvariable=self.sepVar)
            self.sepEntry.grid(column= 0, row= 10, sticky = "W", padx=(245,0))
        
        def activateSeriesEntry():
            try:
                self.numLabel.destroy()
                self.num.destroy()
                del self.numLabel, self.num
            except: pass
            
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 10, sticky="NSWE") # przysłania
            self.numLabel = ttk.Label(self.mainFrame, text = "Zacznij od: S").grid(column = 0, row = 10, sticky="W", padx=10, pady=2)
            self.num = ttk.Entry(self.mainFrame, width= 2, textvariable=self.seriesNumeration1)
            self.num.grid(column= 0, row= 10, sticky = "W", padx=(89,0))
            self.numLabel1 = ttk.Label(self.mainFrame, text = "E").grid(column = 0, row = 10, sticky="W", padx=(122,0), pady=2)
            self.num1 = ttk.Entry(self.mainFrame, width= 2, textvariable=self.seriesNumeration2)
            self.num1.grid(column= 0, row= 10, sticky = "W", padx=(136,0))
            self.sepLabel = ttk.Label(self.mainFrame, text = "separator:").grid(column = 0, row = 10, sticky="W", padx=(180,0), pady=2)
            self.sepEntry = ttk.Entry(self.mainFrame, width= 4, textvariable=self.sepVar)
            self.sepEntry.grid(column= 0, row= 10, sticky = "W", padx=(245,0))

        checkStandard = ttk.Checkbutton(self.mainFrame, text= "zwykła", variable=self.standardVar, command= activateStandardEntry) 
        checkStandard.grid(column= 0, row= 8, sticky= tk.W, padx=10, pady=2)
        
        checkSeries = ttk.Checkbutton(self.mainFrame, text= "serialowa (np. S01E01)", variable=self.seriesVar, command= activateSeriesEntry) 
        checkSeries.grid(column= 0, row= 9, sticky= tk.W, padx=10, pady=2)
    
    def numerationSelection1(self, *ignoredArgs):
        if self.standardVar.get() == 0:
            self.seriesVar.set(1)
        elif self.standardVar.get() == 1:         
            self.seriesVar.set(0)
         
        
    def numerationSelection2(self, *ignoredArgs):
        if self.seriesVar.get() == 0:
            self.standardVar.set(1)
        elif self.seriesVar.get() == 1:         
            self.standardVar.set(0) 
        
    def trace(self):         
        self.standardVar.trace('w', lambda unused0, unused1, unused2 : self.numerationSelection1())
        self.seriesVar.trace('w', lambda unused0, unused1, unused2 : self.numerationSelection2())
    
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
        
        checkOptionalWidget = ttk.Checkbutton(self.mainFrame, text= "Wprowadzić numerację?", variable=self.chVarUn, command= self.activateOptionalWidget) 
        checkOptionalWidget.grid(column= 0, row= 7, sticky= tk.W, padx=10, pady=10)
        
        startButton = ttk.Button(self.mainFrame, text= "Start", command= self.start)
        startButton.grid(column= 0, row= 11, sticky="W", padx=10, pady=10)
        
        previewButton = ttk.Button(self.mainFrame, text= "Podgląd", command= self._preview)
        previewButton.grid(column= 0, row= 11, sticky="N", padx=10, pady=10)
        
        exitButton = ttk.Button(self.mainFrame, text= "Zamknij", command= self._quit)
        exitButton.grid(column= 0, row= 11, sticky="E", padx=10, pady=10)
        
        disabledButton = ttk.Style()
        disabledButton.configure("DS.TButton")
        self.backButton = ttk.Button(self.mainFrame, text= "Cofnij", command= self._back, style='DS.TButton', state='disabled')
        disabledButton.map('DS.TButton', foreground=[('disabled', 'gray'), ('active', 'white')])
        self.backButton.grid(column= 0, row= 12, sticky="W", padx=10, pady=(0,10))
        
        clearButton = ttk.Button(self.mainFrame, text= "Wyczyść", command= self._clear)
        clearButton.grid(column= 0, row= 12, sticky="N", padx=10, pady=(0,10))
        
        self.numLabel = ttk.Label(self.mainFrame).grid(column = 0, row = 10, sticky="W", padx=10, pady=10) # pełni rolę pustego rzędu

    def previewWidgets(self):
        def multiple_yview(*args):
            self.previewText.yview(*args)
            self.previewTextAfter.yview(*args)
        def on_textscroll(*args):
            scrollbar.set(*args)
            multiple_yview('moveto', args[0])
        
        self.previewFrame = ttk.LabelFrame(self.win, text='Podgląd',labelanchor='n')
        self.previewFrame.grid(column=2, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.previewText = tk.Text(self.previewFrame, width=48, height=23, wrap= tk.NONE, background='white', foreground='black')
        self.previewText.grid(column= 1, row= 0, rowspan=8, sticky="NSEW", padx=(10,0), pady=(10,10))
        self.previewTextAfter = tk.Text(self.previewFrame, width=48, height=23, wrap= tk.NONE, background='white', foreground='black',)
        self.previewTextAfter.grid(column= 2, row= 0, rowspan=8, sticky="NSEW", padx=(0,10), pady=(10,10))

        scrollbar = ttk.Scrollbar(self.previewFrame, command=multiple_yview, orient="vertical")
        #hsb = ttk.Scrollbar(self.previewFrame, command=(self.previewText.xview==self.previewTextAfter.xview), orient="horizontal",)
        self.previewText.configure(yscrollcommand=on_textscroll)
        self.previewTextAfter.configure(yscrollcommand=on_textscroll)
        #self.previewTextAfter.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(column=3, row=0, rowspan=8, sticky="ns", padx=2)
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
            startIndexBefore = self.objsPreview[f].find(self.toConvert1.get())
            startIndexAfter = self.newNameList[f].find(self.afterConvert1.get())
            endIndexBefore = startIndexBefore + len(self.toConvert1.get())
            endIndexAfter = startIndexAfter + len(self.afterConvert1.get())
            if startIndexBefore != -1:
                self.previewText.tag_add("before", f"{a}.{startIndexBefore}", f"{a}.{endIndexBefore}")
                self.previewText.tag_configure("before", background="white", foreground="red") 
                self.previewTextAfter.tag_add("after", f"{a}.{startIndexAfter}", f"{a}.{endIndexAfter}")
                self.previewTextAfter.tag_configure("after", background="white", foreground="green")
                if self.chVarUn.get() == 1:
                    self.previewTextAfter.tag_add("after", f"{a}.{0}", f"{a}.{len(self.addNumList[f])}")
                    self.previewTextAfter.tag_configure("after", background="white", foreground="green")

            a += 1
            multiplierList.append(self.multiplier)
            newNameLenList.append(len(self.newNameList[f]))
            winWidthDict[len(self.newNameList[f])] = self.multiplier
        self.previewTextAfter.configure(width=max(newNameLenList)+round(max(newNameLenList)*(winWidthDict[max(newNameLenList)] / 3.2)))
        self.previewTextAfter.configure(state='disabled')
    
    def _back(self):
        self.backButton.configure(state='disabled')
        a = 0
        for f in self.newNameList:
            full_newName = os.path.join(self.location, f)
            full_oldName = os.path.join(self.location, self.oldNameList[a])
            os.rename(full_newName, full_oldName)
            a += 1
        self.beforePreview()

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
        try: 
            self.standardNumeration.set('')
            self.chVarUn.set(0)
            self.activateOptionalWidget()
        except: pass


    def _tree(self, master, path):
        self.fileIcon = PhotoImage(file=f'{self.filePath}/file18t.png')
        self.folderIcon = PhotoImage(file=f'{self.filePath}/folder18t.png')
        self.openfolderIcon = PhotoImage(file=f'{self.filePath}/openfolder18t.png')
        self.nodes = dict()
        #self.treeFrame = ttk.LabelFrame(self.win, text='TREE',labelanchor='n')
        #self.treeFrame.grid(column=1, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.treeFrame = ttk.Frame(master, width=80, height=80)
        self.treeFrame.grid(column=1, row=0, sticky="NSEW", padx=10, pady=20,)
        self.tree = ttk.Treeview(self.treeFrame, height=16,)
        ysb = ttk.Scrollbar(self.treeFrame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self.treeFrame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Project tree', anchor='w')

        self.tree.grid()
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        

        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)

    def insert_node(self, parent, text, abspath):
        self.parent = parent
        self.text = text
       # node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            node = self.tree.insert(parent, 'end', text=text, image=self.folderIcon, open=False)
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')
        else:
            node = self.tree.insert(parent, 'end', text=text, image=self.fileIcon, open=False)


    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))

         
reOop = ReName()
reOop.win.mainloop()

