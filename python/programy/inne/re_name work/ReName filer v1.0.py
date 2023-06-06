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

    def winStyle(self, window):
        window.tk.call('source', os.path.join(self.filePath, 'forest-dark.tcl'))
        ttk.Style().theme_use('forest-dark')
        ttk.Style().configure("treeview", background='red')
        #window.tk.call("LoadImages", "forest-dark")
    
    def ask_dir(self, event):
        self.directory = fd.askdirectory()
        self.beforePreview()
    
    def beforePreview(self):
        objsPreviewLenList = []
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
                objsPreviewLenList.append(len(self.objsPreview[a]))
                a += 1
            self.previewText.configure(width=max(objsPreviewLenList)+round(max(objsPreviewLenList)*0.18))
            self.previewText.configure(state="disabled")

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
        
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
        self.objs = os.listdir(location)
        if numeration == "":
            a = None
        else:
            a = int(numeration)
        self.srcLenList, self.dstList = [],[]
        for src in self.objs:
            full_src = os.path.join(location, src)
            if os.path.isfile(full_src):
                
                if afterConvert == "" and a != None:
                    afterCon = "0" + str(a) + ". " if a < 10 else str(a) + ". "
                    self.dst = src.replace(toConvert, afterCon, 1)
                    a += 1
                elif afterConvert == "" and a == None:
                    self.dst = src.replace(toConvert, afterConvert, 1)
                elif a == None:
                    self.dst = src.replace(toConvert, afterConvert, 1)    
                else:
                    # dst = src.replace(toConvert, ( str(a)+ ". " + afterConvert))
                    afterCon = "0" + str(a) + ". " + afterConvert if a < 10 else str(a) + ". " + afterConvert
                    self.dst = src.replace(toConvert, afterCon, 1)
                    a += 1

            if src != self.dst:
                full_dst = os.path.join(location, self.dst)
                if preview == 'no':
                    os.rename(full_src, full_dst)
            self.srcLenList.append(len(src))
            self.dstList.append(self.dst)
            
        if preview == 'no':
            self.toConvert1.set('')
            self.afterConvert1.set('')
            self.previewTextAfter.configure(state='normal')
            self.previewTextAfter.delete('1.0', tk.END)
            self.previewTextAfter.configure(state='disabled')
            self.beforePreview()
    def call(self):
        
        self.chCall = self.chVarUn.get()      
        if self.chCall == 1:
            self.optionalWidget()
        if self.chCall == 0:
            self.num.destroy()
            self.numLabel = ttk.Label(self.mainFrame, text = "").grid(column = 0, row = 8, sticky="WE") # przysłania

    def widgets(self):

        self.mainFrame = ttk.LabelFrame(self.win, text='Masowa zmiana nazwy plików',labelanchor='n')
        self.mainFrame.grid(column=0, row=0,columnspan=1, sticky="NSWE", padx=10, pady=(10,10))
            
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
        
        previewButton = ttk.Button(self.mainFrame, text= "Podgląd", command= self._preview)
        previewButton.grid(column= 0, row= 9, sticky="N", padx=10, pady=10)

        action = ttk.Button(self.mainFrame, text= "Start", command= self.start)
        action.grid(column= 0, row= 9, sticky="W", padx=10, pady=10)

        self.numLabel = ttk.Label(self.mainFrame).grid(column = 0, row = 8, sticky="W", padx=10, pady=10) # pełni rolę pustego rzędu

    def previewWidgets(self):
        def multiple_yview(*args):
            self.previewText.yview(*args)
            self.previewTextAfter.yview(*args)
        def on_textscroll(*args):
            vsb.set(*args)
            multiple_yview('moveto', args[0])
        
        self.previewFrame = ttk.LabelFrame(self.win, text='Podgląd',labelanchor='n')
        self.previewFrame.grid(column=1, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.previewText = tk.Text(self.previewFrame, width=48, height=22, wrap= tk.NONE, background='white', foreground='black')
        self.previewText.grid(column= 1, row= 0, rowspan=8, sticky="NSEW", padx=(10,0), pady=(10,10))
        self.previewTextAfter = tk.Text(self.previewFrame, width=48, height=22, wrap= tk.NONE, background='white', foreground='black',)
        self.previewTextAfter.grid(column= 2, row= 0, rowspan=8, sticky="NSEW", padx=(0,10), pady=(10,10))

        vsb = ttk.Scrollbar(self.previewFrame, command=multiple_yview, orient="vertical")
        #hsb = ttk.Scrollbar(self.previewFrame, command=(self.previewText.xview==self.previewTextAfter.xview), orient="horizontal",)
        self.previewText.configure(yscrollcommand=on_textscroll)
        self.previewTextAfter.configure(yscrollcommand=on_textscroll)
        #self.previewTextAfter.configure(yscrollcommand=vsb.set)
        vsb.grid(column=3, row=0, rowspan=8, sticky="ns", padx=2)
        #hsb.grid(column=1, row=9, sticky="ew", padx=2) 
    def _preview(self):
        objsPreviewLenList, dstLenList = [],[]
        a = 1
        self.generatePreview = 'yes'
        
        self.start(self.generatePreview)
        self.beforePreview()
        #self.previewText.configure(state='normal')
        self.previewTextAfter.configure(state='normal')
        self.previewTextAfter.delete('1.0', tk.END)
        
        self.objsPreview.sort()
        self.dstList.sort()
        for f in range(len(self.dstList)):
            self.previewTextAfter.insert(tk.INSERT, f"{self.dstList[f]}\n") 

            startIndex = self.objsPreview[f].find(self.toConvert1.get())
            endIndexBefore = startIndex + len(self.toConvert1.get())
            endIndexAfter = startIndex + len(self.afterConvert1.get())
            self.previewText.tag_add("before", f"{a}.{startIndex}", f"{a}.{endIndexBefore}")
            self.previewText.tag_configure("before", background="white", foreground="red") 
            self.previewTextAfter.tag_add("after", f"{a}.{startIndex}", f"{a}.{endIndexAfter}")
            self.previewTextAfter.tag_configure("after", background="white", foreground="green")
            a += 1
            #objsPreviewLenList.append(len(self.objsPreview[f]))
            dstLenList.append(len(self.dstList[f]))
            
        #self.previewText.configure(width=max(objsPreviewLenList)+5)
        self.previewTextAfter.configure(width=max(dstLenList)+round(max(dstLenList)*0.18))
        #self.previewText.configure(state='disabled')
        self.previewTextAfter.configure(state='disabled')
        
                

    def optionalWidget(self):   
        self.numLabel = ttk.Label(self.mainFrame, text = "Format numeracji:").grid(column = 0, row = 8, sticky="W", padx=10, pady=10)
        self.numeration1 = tk.StringVar()
        self.num = ttk.Entry(self.mainFrame, width= 6, textvariable=self.numeration1)
        self.num.grid(column= 0, row= 8)
        
reOop = ReName()
reOop.win.mainloop()