import tkinter as tk
from tkinter import ttk
import os, sys, string
import tkinter.filedialog as fd
from tkinter import PhotoImage
import psutil
from tkinter import messagebox as mBox
# wiersz 916 wurzucilo błąd, trzeba znalezć


# class to visualize the directory tree
class Tree():
    def __init__(self):
        self.filePath = os.path.dirname(sys.argv[0])
        self.home_directory = os.path.expanduser( '~' )
        self.getDrivesName()
    
    # function detect all active disk partitions  
    def getDrivesName(self):
        data1 = {} 
        linuxMountpoint = []   
        win_drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:\\' % d)]
        # linux_drives = ['/dev/sda%s' % d for d in range(100) if os.path.exists('/dev/sda%s' % d)]                 sprawdz pendrive pod linuksem
        psutil_drives = psutil.disk_partitions(all=False)
    
        for v in psutil_drives:
            if v.fstype != 'squashfs' and v.device not in data1.values():
                try:
                    os.listdir(v.mountpoint)
                    data1[v.mountpoint] = v.device
                    linuxMountpoint.insert(1, v.mountpoint)
                except PermissionError:
                    pass
      
        self.os_drives = set(win_drives + linuxMountpoint)
        self.os_drives = list(self.os_drives)

        del data1, linuxMountpoint, win_drives
    
    # the function responsible for the tree view and tree view widgets
    def _tree(self, master, path):
        
        # directory tree reset
        def _treeReset(): 
            self._tree(reNameObj.win, path=self.os_drives)
            self.tree.bind("<Double-1>",self.OnDoubleClick)      

        self.driveTextList = [] 
        self.fileIcon = PhotoImage(file=f'{self.filePath}/file18t.png')
        self.folderIcon = PhotoImage(file=f'{self.filePath}/folder18t.png')
        self.openfolderIcon = PhotoImage(file=f'{self.filePath}/openfolder18t.png')
        self.errorfolderIcon = PhotoImage(file=f'{self.filePath}/error folder.png')
        self.diskIcon = PhotoImage(file=f'{self.filePath}/disk18.png')
        self.nodes = dict()
        self.nodesAll = dict()
        self.treeFrame = ttk.Frame(master, height=20)
        self.treeFrame.grid(column=1, row=0, sticky="NSEW", padx=10, pady=(55,10))
        self.tree = ttk.Treeview(self.treeFrame, height=23, show='tree headings')
        ysb = ttk.Scrollbar(self.treeFrame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self.treeFrame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(xscrollcommand=xsb.set, yscrollcommand=ysb.set )
        self.tree.heading('#0', text='Reset tree', anchor='w',command=_treeReset)
        self.tree.column('#0', minwidth=620, stretch=False, anchor='e',width=350 )
        
        self.tree.grid(column=0, row=1)
        ysb.grid(row=1, column=1, sticky='ns')
        xsb.grid(row=2, column=0, sticky='ew')
        self.insert_node('', self.home_directory, self.home_directory, self.folderIcon)
        for i in range(len(path)):
            abspath = os.path.abspath(path[i-1])
            driveText = abspath[abspath.rfind('/')+1:] 
            self.driveTextList.append(driveText)
            if len(driveText) > 15:
                a=i
                if a == 0: a=''
                driveText = f"Wolumin{a}"
            elif len(driveText) == 0: 
                driveText = "Ubuntu" 
            self.insert_node('', driveText, abspath, self.diskIcon)
            i += 1
        #print(self.tree.item(self.nodesAll))
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind('<<TreeviewClose>>', self.close_node)
   
    # inserts a new directory node
    def insert_node(self, parent, text, abspath, img):
        self.parent = parent
        self.text = text
       
        if os.path.isdir(abspath) :
            node = self.tree.insert(parent, 'end', text=text, image=img, open=False)
            self.nodes[node] = abspath
            self.nodesAll[node] = abspath
            self.tree.insert(node, 'end')
            
        else:
            node = self.tree.insert(parent, 'end', text=text, image=img, open=False)
    
    # closes the directory node
    def close_node(self,event):
        node = self.tree.focus()
        path = os.path.abspath(self.nodesAll[node])
        try:
            os.listdir(path)
            if self.tree.item(node)['text'] in  self.driveTextList or self.tree.item(node)['text'] == 'Ubuntu':
                img=self.diskIcon
            else:
                img=self.openfolderIcon
        except PermissionError:
            img=self.errorfolderIcon
        self.tree.item(node, image=img, open=False)
   
    # opens the directory node
    def open_node(self, event):
        node = self.tree.focus()
        if self.tree.item(node)['text'] in  self.driveTextList or self.tree.item(node)['text'] == 'Ubuntu':
            img=self.diskIcon
        else:
            img=self.openfolderIcon
        self.tree.item(node, image=img, open=True)
        abspath = self.nodes.pop(node, None) 
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            try:
                for p in os.listdir(abspath):
                    if os.path.isdir(os.path.join(abspath, p)):
                        try:
                            os.scandir(os.path.join(abspath, p))
                            img = self.folderIcon
                            self.insert_node(node, p, os.path.join(abspath, p),img)
                        except PermissionError:
                            img=self.errorfolderIcon
                            self.insert_node(node, p, os.path.join(abspath, p),img)
                    else:
                        img = self.fileIcon
                        self.insert_node(node, p, os.path.join(abspath, p), img)
            except PermissionError:
                self.close_node('<<TreeviewClose>>')
                mBox.showerror(reNameObj.translateDict["Acces denided"][reNameObj.lang], reNameObj.translateDict["You do not have permission to access this directory."][reNameObj.lang])
                img=self.errorfolderIcon
        
    # event one double click of the right mouse button
    def OnDoubleClick(self, event):
        reNameObj._clear()
        self.directory = False
        item = self.tree.selection()[0]
        if item in self.nodesAll:
            parent_iid = self.tree.parent(item)
            node = []
            # go backward until reaching root
            while parent_iid != '':
                
                node.insert(0, self.nodesAll[parent_iid])
                parent_iid = self.tree.parent(parent_iid)
            i = self.nodesAll[item]
            path = os.path.join(*node, i)
            
            try:
                os.listdir(path)
                reNameObj.location1.set(path)
                reNameObj.beforePreview()    
            except PermissionError or ValueError:
                pass
        else:
            mBox.showinfo(reNameObj.translateDict["This is not a directory"][reNameObj.lang], reNameObj.translateDict["The specified location cannot be accessed because it is not a directory. Choose another location."][reNameObj.lang])
            pass

# class responsible for execute the action
class StartAction():
    # action function
    def action(self,  preview = 'no'):
        self.actionVariable()
        self.checkAddnumeration()
        if self.stopActionFunc == "Yes":
            pass
        else: 
            self.actionLoop(preview)
    
    # checks whether the passed parameter consists only of digits
    def regexNum(self, getNum):
        return getNum.isdigit()
    
    # checks whether the passed parameter consists only of letters
    def regexNotNum(self, getNum):
        return getNum.isalpha()
    
    # the function initializes the variables necessary to perform the action
    def actionVariable(self):
        self.numeration = ''
        self.numeration2 = ''
        self.startIVar = 1
        self.lengthIVar = 0
        self.newName = ''
        self.separator = ''
        self.stopActionFunc = 'No'
        self.location = reNameObj.location1.get()
        self.afterConvert = reNameObj.afterConvert1.get()
        self.toConvert = reNameObj.toConvert1.get()
        self.oldNameList, self.oldNameLenList, self.newNameList, self.addNumList, self.newAllFilesList, self.oldAllFilesList, self.fulloldAllFilesList = [],[],[],[],[],[],[]
        if reNameObj.deleteAddVar.get() == 1:
            if self.regexNum(reNameObj.startIndexVar.get()) == True and self.regexNum(reNameObj.lengthIndexVar.get()) == True:
                self.startIVar = int(reNameObj.startIndexVar.get())
                self.lengthIVar = int(reNameObj.lengthIndexVar.get())
                if self.startIVar == 0:
                     mBox.showerror(reNameObj.translateDict["Attention"][reNameObj.lang], reNameObj.translateDict["'Character index' cannot be 0."][reNameObj.lang])
                     self.stopActionFunc = 'Yes'
            elif reNameObj.startIndexVar.get() != '' and self.regexNum(reNameObj.startIndexVar.get()) == False or reNameObj.lengthIndexVar.get() != '' and self.regexNum(reNameObj.lengthIndexVar.get()) == False:
                mBox.showerror(reNameObj.translateDict["Enter a number"][reNameObj.lang], reNameObj.translateDict["The 'character index' and 'number of characters' fields must be numbers."][reNameObj.lang])
                self.stopActionFunc = 'Yes'

        self.newTxtVar = reNameObj.newTextVar.get()
    
    # the function checks the conditions for adding numbering   
    def checkAddnumeration(self):
        if self.stopActionFunc == 'Yes':
            pass
        else:
            if reNameObj.checkNumVar.get() == 1 and reNameObj.standardVar.get() == 1:
                if self.regexNum(reNameObj.standardNumeration.get()) == True:
                    self.numeration = int(reNameObj.standardNumeration.get())
                    self.separator = reNameObj.sepVar.get()
                    self.numeration2 = None
                else: 
                    mBox.showerror(reNameObj.translateDict["Enter a number"][reNameObj.lang], reNameObj.translateDict["The 'start at' field must be an integer greater than 0."][reNameObj.lang])
                    self.stopActionFunc = 'Yes'
            elif reNameObj.checkNumVar.get() == 1 and reNameObj.seriesVar.get() == 1:
                if self.regexNum(reNameObj.seriesNumeration1.get()) == True and self.regexNum(reNameObj.seriesNumeration2.get()) == True:
                    self.numeration = int(reNameObj.seriesNumeration1.get())
                    self.numeration2 = int(reNameObj.seriesNumeration2.get())
                    self.separator = reNameObj.sepVar.get()
                else:
                    mBox.showerror(reNameObj.translateDict["Enter a number"][reNameObj.lang], reNameObj.translateDict["The 'start at: S/E' fields must be integers greater than 0."][reNameObj.lang])
                    self.stopActionFunc = 'Yes'
            else: 
                self.numeration = None
                self.numeration2 = None
        return self.stopActionFunc
    
    # a function responsible for running a loop and making changes
    def actionLoop(self,preview): 
        
        # the function will add numbering
        def addNumeration(oldName, afterConvert = None, toConvert = None ):
            if reNameObj.checkNumVar.get() == 1 and reNameObj.standardVar.get() == 1:               # zwykła numeracja
                addNum = "0" + str(self.numeration) + self.separator  if self.numeration < 10 else str(self.numeration) + self.separator 
                if reNameObj.changePartNameVar.get() == 1:
                    self.newName = addNum + oldName.replace(toConvert, afterConvert, 1)
                else: 
                    self.newName = addNum + oldName.replace(oldName[(self.startIVar-1):(self.startIVar-1+self.lengthIVar)], afterConvert, 1)
                self.numeration += 1
            else:                                                                               # serialowa numeracja
                addNum = "S0" + str(self.numeration) + "E0" + str(self.numeration2) + self.separator if self.numeration2 < 10 else "S0" + str(self.numeration) + "E" + str(self.numeration2) + self.separator
                if reNameObj.changePartNameVar.get() == 1:
                    self.newName = addNum + oldName.replace(toConvert, afterConvert, 1)
                else: 
                    self.newName = addNum + oldName.replace(oldName[(self.startIVar-1):(self.startIVar-1+self.lengthIVar)], afterConvert, 1)
                self.numeration2 += 1
            self.addNumList.append(addNum)
        
        # function responsible for checking whether the names after the change will be unique
        def checkChangeConditions():
            newNameSet = set(self.newAllFilesList)
            if len(self.newAllFilesList) != len(newNameSet):
                mBox.showerror(reNameObj.translateDict["Rename error"][reNameObj.lang], reNameObj.translateDict["Selected files cannot be renamed. Some of the changed files would have the same name. Change the renaming conditions or enter numbering."][reNameObj.lang])
                self.stopActionFunc = "Yes"
            else:
                a=0
                for v in self.oldAllFilesList:
                    renameFunc(v,self.newAllFilesList[a], self.fulloldAllFilesList[a])
                    if self.stopActionFunc == 'Yes':
                        break
                    a += 1
            del newNameSet, self.newAllFilesList, self.oldAllFilesList, self.fulloldAllFilesList
       
        # function responsible for renaming the file
        def renameFunc(oldName, newName, full_oldName):
            if oldName != newName:
                full_newName = os.path.join(self.location, newName)
                if preview == 'no':
                    try:
                        os.rename(full_oldName, full_newName)
                    except OSError:
                        mBox.showerror(reNameObj.translateDict["Wrong separator"][reNameObj.lang], reNameObj.translateDict["An illegal character was used in the separator. Change separator."][reNameObj.lang])
                        self.stopActionFunc = 'Yes'
            self.oldNameLenList.append(len(oldName))
            self.newNameList.append(newName)
            self.oldNameList.append(oldName)
        
        # function responsible for making changes
        def loop():
            for oldName in reNameObj.objsPreview:
                full_oldName = os.path.join(self.location, oldName)
                if os.path.isfile(full_oldName):                               
                    if reNameObj.changePartNameVar.get() == 1:
                        if self.numeration != None:                               
                            if reNameObj.toConvert1.get() == '' and reNameObj.afterConvert1.get() == '':
                                addNumeration(oldName, self.afterConvert, self.toConvert)  
                            elif oldName.find(self.toConvert) != -1:             
                                addNumeration(oldName, self.afterConvert, self.toConvert)
                            else:
                                self.newName = oldName.replace(self.toConvert, self.afterConvert, 1) 
                                self.addNumList.append(0)
                        else:                                               
                            self.newName = oldName.replace(self.toConvert, self.afterConvert, 1)
                    else:                                                                                       
                        if self.regexNum(reNameObj.startIndexVar.get()) == False or self.regexNum(reNameObj.lengthIndexVar.get()) == False:
                            mBox.showinfo(reNameObj.translateDict["Fill in the fields"][reNameObj.lang], reNameObj.translateDict["Please complete all fields necessary for the name change."][reNameObj.lang])
                            self.stopActionFunc = "Yes"
                            break                                                        
                        elif self.numeration != None:                               
                            if self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 0:
                                self.afterConvert = ''
                                addNumeration(oldName, self.afterConvert)  
                            elif self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 1:             
                                self.afterConvert = self.newTxtVar
                                addNumeration(oldName, self.afterConvert)
                            else:
                                pass
                        else:                                               
                            if self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 0:
                                self.afterConvert = ''
                            elif self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 1:            
                                self.afterConvert = self.newTxtVar 
                           
                            self.newName = oldName[0:self.startIVar-1] + self.afterConvert + oldName[self.startIVar-1+self.lengthIVar:]
                    if len(oldName)-len(oldName[oldName.rfind('.'):])+1 <= self.startIVar + self.lengthIVar-1:
                        mBox.showerror(reNameObj.translateDict["Unable to rename the file"][reNameObj.lang], reNameObj.translateDict["Exceeded maximum number of changeable letters, please enter a smaller number."][reNameObj.lang])
                        self.stopActionFunc = 'Yes'
                        break       
                    self.newAllFilesList.append(self.newName)
                    self.oldAllFilesList.append(oldName)
                    self.fulloldAllFilesList.append(full_oldName)
                    if self.stopActionFunc == 'Yes':
                        break
            checkChangeConditions()
            #renameFunc(oldName, self.newName, full_oldName)

        # function responsible for changing field settings when file names are changed
        def ifNoPreview():
            if preview == 'no':
                reNameObj.toConvert1.set('')
                reNameObj.afterConvert1.set('')
                reNameObj.previewTextAfter.configure(state='normal')
                reNameObj.previewTextAfter.delete('1.0', tk.END)
                reNameObj.previewTextAfter.configure(state='disabled')
                reNameObj.beforePreview()
                reNameObj.backButton.configure(state='normal')
        
        if os.path.isdir(self.location): 
            loop()
            if self.stopActionFunc == 'No':        
                ifNoPreview()
            else:
                pass
                #reNameObj._clear()
        else: 
            self.workingDirError = mBox.showinfo(reNameObj.translateDict["No working directory selected"][reNameObj.lang], reNameObj.translateDict["Select a working directory to continue."][reNameObj.lang])
            self.stopActionFunc ='Yes'

# the main class responsible for the work of the application             
class ReName(Tree, StartAction):
    def __init__(self):
        self.win = tk.Tk()
        self.osVar()
        super().__init__()
        self.dictionary()
        self.winStyle(self.win)
        self.win.title("ReName v1.0")
        self.directory = None
        self.widgets()
        self.previewWidgets()
        self.tracechangeLang()
        self.strLen = None
        self.dirButton.bind("<Button-1>", self.ask_dir)
        self.tree.bind("<Double-1>", super().OnDoubleClick)
        
    # function responsible for creating a special variable used to adjust the graphical interface for the linux system
    def osVar(self):
        if sys.platform == 'linux':
            self.sysVar = 10
        else:
            self.sysVar = 0

    # a function containing a dictionary with translations of words/sentences
    def dictionary(self):
        self.lang = 0
        self.translateDict = {
            'Acces denided':['Acces denided','Brak dostępu'], 
            'You do not have permission to access this directory.':['You do not have permission to access this directory.','Nie masz uprawnień do dostępu do tego katalogu.'],
            'This is not a directory':['This is not a directory','To nie jest katalog'],
            'The specified location cannot be accessed because it is not a directory. Choose another location.':['The specified location cannot be accessed because it is not a directory. Choose another location.','Nie da się wejść do wskazanej lokalizacji ponieważ nie jest to katalog.\nWskaż inną lokalizację.'],
            'Attention':['Attention','Uwaga'],
            "'Character index' cannot be 0.":["'Character index' cannot be 0.","'Indeks znaku' nie może być 0."],
            'Enter a number':['Enter a number','Wprowadź liczbę'],
            "The 'character index' and 'number of characters' fields must be numbers.":["The 'character index' and 'number of characters' fields must be numbers.","Pola 'indeks znaku' i 'ilość znaków' muszą być liczbami."],
            "The 'start at' field must be an integer greater than 0.":["The 'start at' field must be an integer greater than 0.","Pole 'zacznij od' musi być liczbą całkowitą większą od 0."],
            "The 'start at: S/E' fields must be integers greater than 0.":["The 'start at: S/E' fields must be integers greater than 0.","Pola 'zacznij od: S/E' muszą być liczbami całkowitymi większymi od 0."],
            'Rename error':['Rename error','Błąd zmiany nazwy'],
            'Selected files cannot be renamed. Some of the changed files would have the same name. Change the renaming conditions or enter numbering.':['Selected files cannot be renamed. Some of the changed files would have the same name. Change the renaming conditions or enter numbering.','Nie można zmienić nazwy wybranych plików.\nCzęść ze zmienianych plików miałaby tą samą nazwę.\nZmień warunki zmiany nazw lub wprowadź numerację.'],
            'Wrong separator':['Wrong separator','Błędny separator'],
            'An illegal character was used in the separator. Change separator.':['An illegal character was used in the separator. Change separator.','W separatorze użyto niedozwolonego znaku.\nZmień separator.'],
            'Fill in the fields':['Fill in the fields','Uzupełnij pola'],
            'Please complete all fields necessary for the name change.':['Please complete all fields necessary for the name change.','Uzupełnij wszystkie pola niezbędne do przeprowadzenia zmiany nazwy.'],
            'Unable to rename the file':['Unable to rename the file','Nie można zmienić nazwy pliku'],
            'Exceeded maximum number of changeable letters, please enter a smaller number.':['Exceeded maximum number of changeable letters, please enter a smaller number.','Przekroczono maksymalną liczbę zmienianych liter, wprowadź mniejszą liczbę.'],
            'No working directory selected':['No working directory selected','Nie wybrano katalogu roboczego'],
            'Select a working directory to continue.':['Select a working directory to continue.','Wybierz katalog roboczy, aby kontynuować.'],
            'start at:':['start at:','zacznij od:'],
            'start at: S':['start at: S','zacznij od: S'],
            'actions available':['actions available','dostępne akcje'],
            'change part of name':['change part of name','zmień fragment nazwy'],
            'text to change:':['text to change:','tekst do zmiany:'],
            'change to:':['change to:','zmienić na:'],
            'delete/replace in name':['delete/replace in name','usuń/zastąp w nazwie'],
            'character index:':['character index:','indeks znaku:'],
            'quantity:':['quantity:','ilość znaków:'],
            'replace with text':['replace with text','zastąpić tekstem'],
            'enter numbering?':['enter numbering?','wprowadzić numerację?'],
            'typical':['typical','zwykła'],
            'TV series (e.g. S01E01)':['TV series (e.g. S01E01)','serialowa (np. S01E01)'],
            'Preview':['Preview','Podgląd'],
            'Exit':['Exit','Zamknij'],
            'Back':['Back','Cofnij'],
            'Clear':['Clear','Wyczyść'],
            'Reset tree':['Reset tree', 'Reset drzewa']
            }
    
    # function containing widgets to be translated
    def widgetsToTranslate(self):
        self.mainFrame.configure(text=self.translateDict['actions available'][self.lang])
        self.changePartNameChb.configure(text=self.translateDict['change part of name'][self.lang])
        self.textToChangeLab.configure(text=self.translateDict['text to change:'][self.lang])
        self.changeToLab.configure(text=self.translateDict['change to:'][self.lang])
        self.deleteAddChb.configure(text=self.translateDict['delete/replace in name'][self.lang])
        self.startIndex.configure(text=self.translateDict['character index:'][self.lang])
        self.lenght.configure(text=self.translateDict['quantity:'][self.lang])
        self.addTextCheck.configure(text=self.translateDict['replace with text'][self.lang])
        self.checkNumerationWidget.configure(text=self.translateDict['enter numbering?'][self.lang])
        self.checkStandard.configure(text=self.translateDict['typical'][self.lang])
        self.checkSeries.configure(text=self.translateDict['TV series (e.g. S01E01)'][self.lang])
        self.previewButton.configure(text=self.translateDict['Preview'][self.lang])
        self.previewFrame.configure(text=self.translateDict['Preview'][self.lang])
        self.exitButton.configure(text=self.translateDict['Exit'][self.lang])
        self.backButton.configure(text=self.translateDict['Back'][self.lang])
        self.clearButton.configure(text=self.translateDict['Clear'][self.lang])
        self.startIndexEntry.grid_configure(padx=(100+self.sysVar*self.langPadxVar/10+self.langPadxVar,10))
        self.lenghtEntry.grid_configure(padx=(87-self.sysVar*0.3-self.langPadxVar*6,10))
        self.tree.heading('#0', text=self.translateDict['Reset tree'][self.lang])
        
        if self.standardVar.get() == 1:
            self.numLabel.configure(text=self.translateDict['start at:'][self.lang])
            self.num.grid_configure(padx=(80+self.sysVar*0.9-self.langPadxVar*2,0))
        else:
            self.numLabel.configure(text=self.translateDict['start at: S'][self.lang])
            self.num.grid_configure(padx=(89+self.sysVar*0.6-self.langPadxVar*1.8,0))
            self.numLabel1.grid_configure(padx=(122+self.sysVar-self.langPadxVar*1.8,0))
            self.num1.grid_configure(padx=(136+self.sysVar*0.7-self.langPadxVar*1.8,0))
    
    # a function that changes the values of variables when changing the application language    
    def changeLang(self,*ignoredArgs):
        if self.langVar.get() == 'en':
            self.lang = 0
            self.langPadxVar = 10
            self.widgetsToTranslate()
        elif self.langVar.get() == 'pl':
            self.lang = 1
            self.langPadxVar = 0
            self.widgetsToTranslate()
    
    # function responsible for tracking application language changes        
    def tracechangeLang(self):         
        self.langVar.trace('w', lambda unused0, unused1, unused2 : self.changeLang())        
    
    # function responsible for exiting the application   
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
    
    # function responsible for launching the application's graphic theme 
    def winStyle(self, window):
        window.tk.call('source', os.path.join(self.filePath, 'forest.tcl'))
        window.tk.call("set_theme", "forest-dark")
        self.icon = PhotoImage(file=f'{self.filePath}/light4.png')
        #window.attributes("-fullscreen", True) # okno otwiera się na pełnym ekranie

    # function responsible for changing the application's graphic theme 
    def change_theme(self):
        
        if self.win.tk.call("ttk::style", "theme", "use") == "forest-dark":
            self.win.tk.call("set_theme", "forest-light")
            self.icon1 = PhotoImage(file=f'{self.filePath}/dark4.png')
            self.themeButton.configure(image=self.icon1)
            TButton1 = ttk.Style()
            TButton1.configure("New.TButton", width = 5, border = 2, padding= {0,0,0,0})
            self.previewText.configure(background='white', foreground='black')
            self.previewTextAfter.configure(background='white', foreground='black')
            
        else:
            self.win.tk.call("set_theme", "forest-dark")
            self.icon1 = PhotoImage(file=f'{self.filePath}/light4.png')
            self.themeButton.configure(image=self.icon1)
            self.previewText.configure(background='white', foreground='black')
            self.previewTextAfter.configure(background='white', foreground='black')
        
    # function responsible for handling the event when opening the directory selection window
    def ask_dir(self, event):
        self._clear()
        self.directory = fd.askdirectory()
        if self.directory == '':
            pass
        else:
            self.beforePreview()
    
    # function responsible for creating a list of preview files and configuration parameters
    def beforePreview(self):
        self.nameWidthList = []
        if self.directory:
            self.lok.delete(first=0, last=self.strLen)
            self.lok.insert(0, self.directory)
            self.strLen = len(self.directory)
        
        self.objsPreview = os.listdir(self.location1.get())
        self.objsPreview.sort()
        self.previewText.configure(state="normal")
        self.previewText.delete('1.0', tk.END)
        a = 0
        for name in self.objsPreview:
            if os.path.isfile(os.path.join(self.location1.get(), name)):
                self.previewText.insert(tk.INSERT, f"{name}\n")
                self.textFieldAutoFit(name)
                self.nameWidthList.append(self.stringWidth)
                a += 1
    
        if self.nameWidthList == []: pass
        elif round(max(self.nameWidthList)) < 90:
            self.previewText.configure(width=round(max(self.nameWidthList)))
        else: self.previewText.configure( width = 90 )
        
        self.previewText.configure(state="disabled")
        
    # function responsible for building entry fields for regular numbering
    def activateStandardEntry(self):
        try:
            self.numLabel.destroy()
            self.num.destroy()
            del self.numLabel, self.num 
            self.numLabel1.destroy()
            self.num1.destroy()
            del self.numLabel1, self.num
        except: pass
        
        self.numLabel = ttk.Label(self.numerationFrame, text = "")
        self.numLabel.grid(column = 0, row = 1, sticky="NSWE") # przysłania
        self.numLabel = ttk.Label(self.numerationFrame, text=self.translateDict['start at:'][self.lang])
        self.numLabel.grid(column = 0, row = 1, sticky="W", padx=10, pady=2)
        self.num = ttk.Entry(self.numerationFrame, width= 6, textvariable=self.standardNumeration)
        self.num.grid(column= 0, row= 1, sticky = "W", padx=(80+self.sysVar-self.langPadxVar*2,0))
        self.sepLabel = ttk.Label(self.numerationFrame, text = "separator:")
        self.sepLabel.grid(column = 0, row = 1, sticky="W", padx=(180,0), pady=2)
        self.sepEntry = ttk.Entry(self.numerationFrame, width= 4, textvariable=self.sepVar)
        self.sepEntry.grid(column= 0, row= 1, sticky = "W", padx=(245+self.sysVar,0), pady=(10,10))
    
    # function responsible for building entry fields for serial numbering
    def activateSeriesEntry(self):
        try:
            self.numLabel.destroy()
            self.num.destroy()
            del self.numLabel, self.num
        except: pass
        
        self.numLabel = ttk.Label(self.numerationFrame, text = "")
        self.numLabel.grid(column = 0, row = 1, sticky="NSWE") # przysłania
        self.numLabel = ttk.Label(self.numerationFrame, text = self.translateDict['start at: S'][self.lang])
        self.numLabel.grid(column = 0, row = 1, sticky="W", padx=10, pady=2)
        self.num = ttk.Entry(self.numerationFrame, width= 2, textvariable=self.seriesNumeration1)
        self.num.grid(column= 0, row=1, sticky = "W", padx=(89+self.sysVar*0.6-self.langPadxVar*1.8,0))
        self.numLabel1 = ttk.Label(self.numerationFrame, text = "E")
        self.numLabel1.grid(column = 0, row = 1, sticky="W", padx=(122+self.sysVar-self.langPadxVar*1.8,0), pady=2)
        self.num1 = ttk.Entry(self.numerationFrame, width= 2, textvariable=self.seriesNumeration2)
        self.num1.grid(column= 0, row= 1, sticky = "W", padx=(136+self.sysVar*0.7-self.langPadxVar*1.8,0))
        self.sepLabel = ttk.Label(self.numerationFrame, text = "separator:")
        self.sepLabel.grid(column = 0, row = 1, sticky="W", padx=(180+self.sysVar*2,0), pady=2)
        self.sepEntry = ttk.Entry(self.numerationFrame, width= 4, textvariable=self.sepVar)
        self.sepEntry.grid(column= 0, row= 1, sticky = "W", padx=(245+self.sysVar*2.7,0), pady=(10,10))
    
    # function responsible for selecting appropriate numbering fields
    def chooseActivateEntry1(self):
        if self.standardVar.get() == 1 and self.seriesVar.get() == 0:
            self.activateStandardEntry()
        elif self.standardVar.get() == 0 and self.seriesVar.get() == 1:
            self.activateSeriesEntry()
    
    # function responsible for selecting appropriate numbering fields
    def chooseActivateEntry2(self):
        if self.standardVar.get() == 0 and self.seriesVar.get() == 1:
            self.activateSeriesEntry()
        elif self.standardVar.get() == 1 and self.seriesVar.get() == 0:
            self.activateStandardEntry()
   
    # function responsible for changing the selection of checkbuttons for numeration
    def numerationSelection1(self, *ignoredArgs):
        if self.standardVar.get() == 0:
            self.seriesVar.set(1)
        elif self.standardVar.get() == 1:         
            self.seriesVar.set(0)
    
    # function responsible for changing the selection of checkbuttons for numeration        
    def numerationSelection2(self, *ignoredArgs):
        if self.seriesVar.get() == 0:
            self.standardVar.set(1)
        elif self.seriesVar.get() == 1:         
            self.standardVar.set(0) 
   
    # function responsible for tracking changes in the numbering method   
    def traceNumerationSelection(self):         
        self.standardVar.trace('w', lambda unused0, unused1, unused2 : self.numerationSelection1())
        self.seriesVar.trace('w', lambda unused0, unused1, unused2 : self.numerationSelection2())
    
    # function responsible for changing the selection of main checkbuttons in main frame 
    def ruleFrame1(self, *ignoredArgs):
        if self.changePartNameVar.get() == 0:
            self.deleteAddVar.set(1)
            self.changeStatePartName()
            self.changeStateDelAdd()
        elif self.changePartNameVar.get() == 1:         
            self.deleteAddVar.set(0)
            self.changeStatePartName()
            self.changeStateDelAdd()
    
    # function responsible for changing the selection of main checkbuttons in main frame         
    def ruleFrame2(self, *ignoredArgs):
        if self.deleteAddVar.get() == 0:
            self.changePartNameVar.set(1)
            self.changeStatePartName()
            self.changeStateDelAdd()
        elif self.deleteAddVar.get() == 1:         
            self.changePartNameVar.set(0)
            self.changeStatePartName()
            self.changeStateDelAdd() 
        
    # function responsible for tracking changes in the main frame  
    def traceSelectRuleFrame(self):         
        self.changePartNameVar.trace('w', lambda unused0, unused1, unused2 : self.ruleFrame1())
        self.deleteAddVar.trace('w', lambda unused0, unused1, unused2 : self.ruleFrame2())
    
    # function responsible for changing the state of fields in the changePartNameframe
    def changeStatePartName(self):
        if self.changePartNameVar.get() == 0:
            self.textToChangeLab.configure(state='disabled')
            self.toConv.configure(state='disabled')
            self.changeToLab.configure(state='disabled')
            self.aConv.configure(state='disabled')
            
        if self.changePartNameVar.get() == 1:
            self.textToChangeLab.configure(state='normal')
            self.toConv.configure(state='normal')
            self.changeToLab.configure(state='normal')
            self.aConv.configure(state='normal')

    # function responsible for changing the state of fields in the deleteAddFrame        
    def changeStateDelAdd(self):
        if self.deleteAddVar.get() == 0:
            self.startIndex.configure(state='disabled')
            self.startIndexEntry.configure(state='disabled')
            self.lenght.configure(state='disabled')
            self.lenghtEntry.configure(state='disabled')
            self.addTextCheck.configure(state='disabled')
            self.newTextEntry.configure(state='disabled')
        else:
            self.startIndex.configure(state='normal')
            self.startIndexEntry.configure(state='normal')
            self.lenght.configure(state='normal')
            self.lenghtEntry.configure(state='normal')
            self.addTextCheck.configure(state='normal')
            self.newTextEntry.configure(state='disabled')
    
    # function responsible for changing the state of fields in the numerationFrame  
    def changeStateNumeration(self):
        if self.checkNumVar.get() == 0:
            self.checkStandard.configure(state='disabled')
            self.checkSeries.configure(state='disabled')
            self.numLabel.configure(state='disabled')
            self.num.configure(state='disabled')
            self.sepLabel.configure(state='disabled') 
            self.sepEntry.configure(state='disabled')
            try:
                self.numLabel1.configure(state='disabled') 
                self.num1.configure(state='disabled')
            except: pass
        else:
            self.checkStandard.configure(state='normal')
            self.checkSeries.configure(state='normal')
            self.numLabel.configure(state='normal')
            self.num.configure(state='normal')
            self.sepLabel.configure(state='normal') 
            self.sepEntry.configure(state='normal')
            try:
                self.numLabel1.configure(state='normal') 
                self.num1.configure(state='normal')
            except: pass
    
    # function responsible for changing the state of newTextEntry field in the deleteAddFrame
    def changeStateAddText(self):
        if self.addTextCheckVar.get() == 0:
            self.newTextEntry.configure(state='disabled')
        else: self.newTextEntry.configure(state='normal')          
    
    # function responsible for creating widgets for the graphical interface
    def widgets(self):
        self.langPadxVar = 10
        self.location1 = tk.StringVar()
        self.toConvert1 = tk.StringVar()
        self.afterConvert1 = tk.StringVar()
        self.changePartNameVar = tk.IntVar()
        self.deleteAddVar = tk.IntVar()
        self.startIndexVar = tk.StringVar()
        self.lengthIndexVar = tk.StringVar()
        self.addTextCheckVar = tk.IntVar()
        self.newTextVar = tk.StringVar()
        self.checkNumVar = tk.IntVar()
        self.standardNumeration = tk.StringVar()
        self.seriesNumeration1 = tk.StringVar()
        self.seriesNumeration2 = tk.StringVar()
        self.standardVar = tk.IntVar()
        self.seriesVar = tk.IntVar()
        self.sepVar = tk.StringVar()
        self.langVar = tk.StringVar()
        
       
        #################################### column 1 #######################################################
        self.mainFrame = ttk.LabelFrame(self.win, labelanchor='n', text=self.translateDict['actions available'][self.lang])
        self.mainFrame.grid(column=0, row=0,columnspan=1, sticky="NSWE", padx=10, pady=(10,10))
        
        # change part of the name widgets   
        self.changePartNameChb = ttk.Checkbutton(variable=self.changePartNameVar,  text=self.translateDict['change part of name'][self.lang], command= self.changeStatePartName,)
        self.changePartNameVar.set(1)
        self.changePartNameFrame = ttk.LabelFrame(self.mainFrame, labelanchor='n', labelwidget=self.changePartNameChb)
        self.changePartNameFrame.grid(column=0, row=0,columnspan=1, sticky="NSWE", padx=10, pady=(10,10))

        self.textToChangeLab = ttk.Label(self.changePartNameFrame, text = self.translateDict['text to change:'][self.lang])
        self.textToChangeLab.grid(column = 0, row = 1, padx=10, pady=(10,2))
        self.toConv = ttk.Entry(self.changePartNameFrame, width= 40, textvariable= self.toConvert1) 
        self.toConv.grid(column= 0, row= 2, padx=10, pady=(0,5))

        self.changeToLab = ttk.Label(self.changePartNameFrame, text = self.translateDict['change to:'][self.lang])
        self.changeToLab.grid(column = 0, row = 3, padx=10, pady=(10,2)) 
        self.aConv = ttk.Entry(self.changePartNameFrame, width= 40, textvariable= self.afterConvert1) 
        self.aConv.grid(column= 0, row= 4, padx=10, pady=(0,10))
        
        # delete/replace in name widgets   
        self.deleteAddChb = ttk.Checkbutton(variable=self.deleteAddVar,  text=self.translateDict['delete/replace in name'][self.lang], command= self.changeStateDelAdd)
        self.deleteAddVar.set(0)
        self.deleteAddFrame = ttk.LabelFrame(self.mainFrame, labelanchor='n', labelwidget=self.deleteAddChb, width=320, height=180)
        self.deleteAddFrame.grid(column=0, row=1,columnspan=2, sticky="NSWE", padx=10, pady=(10,10))

        self.startIndex = ttk.Label(self.deleteAddFrame, text = self.translateDict['character index:'][self.lang], state='disabled')
        self.startIndex.grid(column = 0, row = 0, padx=10, pady=(8,2), sticky = "W")
        self.startIndexEntry = ttk.Entry(self.deleteAddFrame, width= 3, textvariable= self.startIndexVar, state='disabled') 
        self.startIndexEntry.grid(column= 0, row= 0, padx=(100+self.sysVar*self.langPadxVar/10+self.langPadxVar,10), pady=(10,10))
        
        self.lenght = ttk.Label(self.deleteAddFrame, text = self.translateDict['quantity:'][self.lang], state='disabled')
        self.lenght.grid(column = 1, row = 0, padx=15, pady=(8,2), sticky="W")
        self.lenghtEntry = ttk.Entry(self.deleteAddFrame, width= 3, textvariable= self.lengthIndexVar, state='disabled') 
        self.lenghtEntry.grid(column= 1, row= 0, padx=(87-self.sysVar*0.3-self.langPadxVar*6,10), pady=(10,10))

        self.addTextCheck = ttk.Checkbutton(self.deleteAddFrame, variable=self.addTextCheckVar,  text=self.translateDict['replace with text'][self.lang], command=self.changeStateAddText, state='disabled')
        self.addTextCheck.grid(column= 0, row= 1, padx=(10,10), pady=(0,10))
        self.newTextEntry = ttk.Entry(self.deleteAddFrame, textvariable= self.newTextVar, state='disabled') 
        self.newTextEntry.grid(column= 1, row= 1, padx=(0,10), pady=(0,10), sticky="NSWE")

        # add numeration widgets   
        self.checkNumerationWidget = ttk.Checkbutton(variable=self.checkNumVar, text= self.translateDict['enter numbering?'][self.lang], command=self.changeStateNumeration) 
        self.checkNumVar.set(0)
        self.numerationFrame = ttk.LabelFrame(self.mainFrame, labelanchor='n', labelwidget=self.checkNumerationWidget, width=320, height=180)
        self.numerationFrame.grid(column=0, row=2,columnspan=2, sticky="NSWE", padx=10, pady=(10,10))
        
        self.checkStandard = ttk.Checkbutton(self.numerationFrame, text= self.translateDict['typical'][self.lang], variable=self.standardVar, command= self.chooseActivateEntry1, state='disabled') 
        self.checkStandard.grid(column= 0, row= 0, sticky= tk.W, padx=10, pady=2)
        self.standardVar.set(1)
        self.checkSeries = ttk.Checkbutton(self.numerationFrame, text= self.translateDict['TV series (e.g. S01E01)'][self.lang], variable=self.seriesVar, command= self.chooseActivateEntry2, state='disabled') 
        self.checkSeries.grid(column= 0, row= 0, sticky= tk.W, padx=(150,0), pady=2)
        self.traceNumerationSelection()
        self.activateStandardEntry()
        self.changeStateNumeration()
        self.traceSelectRuleFrame()
        
        # action button widgets    
        startButton = ttk.Button(self.mainFrame, text= "Start", command= super().action)
        startButton.grid(column= 0, row= 11, sticky="W", padx=10, pady=10)
        self.previewButton = ttk.Button(self.mainFrame, text= self.translateDict['Preview'][self.lang], command= self._preview)
        self.previewButton.grid(column= 0, row= 11, sticky="N", padx=10, pady=10)
        self.exitButton = ttk.Button(self.mainFrame, text= self.translateDict['Exit'][self.lang], command= self._quit)
        self.exitButton.grid(column= 0, row= 11, sticky="E", padx=10, pady=10)
        disabledButton = ttk.Style()
        disabledButton.configure("DS.TButton")
        disabledButton.map('DS.TButton', foreground=[('disabled', 'gray'), ('active', 'white')])
        self.backButton = ttk.Button(self.mainFrame, text= self.translateDict['Back'][self.lang], command= self._back, style='DS.TButton', state='disabled')
        self.backButton.grid(column= 0, row= 12, sticky="W", padx=10, pady=(0,10))
        self.clearButton = ttk.Button(self.mainFrame, text= self.translateDict['Clear'][self.lang], command= self._clear)
        self.clearButton.grid(column= 0, row= 12, sticky="N", padx=10, pady=(0,10))
        langCombobox = ttk.Combobox(self.mainFrame,textvariable= self.langVar, width=2, state= "readonly", values=['en', 'pl'])
        langCombobox.grid(column= 0, row= 12, sticky="E", padx=10, pady=(0,10)) 
        langCombobox.current(0)
        self.icon1 = PhotoImage(file=f'{self.filePath}/light4.png')
        self.themeButton = ttk.Button(self.mainFrame, image=self.icon1, width=1,command=self.change_theme)
        self.themeButton.grid(column=0, row=12, sticky="E",padx=(0,65), pady=(0,10))
        
        ###################################### column 2 ######################################################
        # directory selection widgets
        self.folderLocLab = ttk.Label(self.win, text = "folder:")
        self.folderLocLab.grid(column = 1, row = 0,  padx=10, pady=(20,5), sticky="NW")
        self.lok = ttk.Entry(self.win, text=self.directory, width= 34-int(self.sysVar*0.4), textvariable= self.location1)   
        self.lok.grid(column= 1, row= 0, padx=10+self.sysVar*5, pady=(15,5), sticky="N")
        self.icon = PhotoImage(file=f'{self.filePath}/folder24dp.png')
        TButton1 = ttk.Style()
        TButton1.configure("New.TButton", width = 5, border = 2, padding= {0,0,0,0})
        self.dirButton = ttk.Button(self.win, image= self.icon, command= self.ask_dir, style='New.TButton')
        self.dirButton.grid(column= 1, row= 0, sticky="NE", padx=(10,20), pady=15)

        # execute tree view    
        super()._tree(self.win, path=self.os_drives)   
    
    # function creates widgets for preview
    def previewWidgets(self):
        def multiple_yview(*args):
            self.previewText.yview(*args)
            self.previewTextAfter.yview(*args)
        def on_textscroll(*args):
            scrollbarVer.set(*args)
            multiple_yview('moveto', args[0])
        
        self.previewFrame = ttk.LabelFrame(self.win, text=self.translateDict['Preview'][self.lang],labelanchor='n')
        self.previewFrame.grid(column=2, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.previewText = tk.Text(self.previewFrame, width=48, height=33-self.sysVar*0.2, wrap= tk.NONE, background='white', foreground='black')
        self.previewText.grid(column= 1, row= 0, rowspan=8, sticky="NSEW", padx=(10,0), pady=(10,10))
        self.previewTextAfter = tk.Text(self.previewFrame, width=48, height=23, wrap= tk.NONE, background='white', foreground='black',)
        self.previewTextAfter.grid(column= 2, row= 0, rowspan=8, sticky="NSEW", padx=(0,10), pady=(10,10))

        scrollbarVer = ttk.Scrollbar(self.previewFrame, command=multiple_yview, orient="vertical")
        self.previewText.configure(yscrollcommand=on_textscroll)
        self.previewTextAfter.configure(yscrollcommand=on_textscroll)
        scrollbarVer.grid(column=3, row=0, rowspan=8, sticky="ns", padx=2)

        scrollbarHor1 = ttk.Scrollbar(self.previewFrame, command=self.previewText.xview, orient="horizontal")
        scrollbarHor1.grid(column=1, row=9, sticky="ew", padx=2)
        self.previewText.configure(xscrollcommand=scrollbarHor1.set)
        
        scrollbarHor2 = ttk.Scrollbar(self.previewFrame, command=self.previewTextAfter.xview, orient="horizontal")
        scrollbarHor2.grid(column=2, row=9, sticky="ew", padx=2)
        self.previewTextAfter.configure(xscrollcommand=scrollbarHor2.set)
        
    #a function responsible for automatically adjusting the width of the text field for the preview
    def textFieldAutoFit(self, string):
        self.stringWidth = 0
        letterWidth = {'a':0.8, 'ą':0.8, 'b':0.8, 'c':0.8, 'ć':0.8, 'd':0.8, 'e':0.8, 'ę':0.8, 'f':0.8, 'g':0.8, 'h':0.8, 'i':0.33, 'j':0.33, 'k':0.8, 'l':0.33, 'ł':0.6, 'm':0.9, 'n':0.8,
                            'ń':0.8, 'o':0.8, 'ó':0.8, 'p':0.8, 'q':0.8, 'r':0.8, 's':0.8, 'ś':0.8, 't':0.8, 'u':0.8, 'v':0.8, 'w':0.9, 'x':0.8, 'y':0.9, 'z':0.8, 'ź':0.8, 'ż':0.8, 'A':1.1,
                            'Ą':1.1, 'B':1.1, 'C':1.1, 'Ć':1.1, 'D':1.1, 'E':1.2, 'Ę':1.1, 'F':1.1, 'G':1.2, 'H':1.1, 'I':0.35, 'J':1.1, 'K':1.2, 'L':1.1, 'Ł':1.1, 'M':1.3, 'N':1.1, 'Ń':1.1, 
                            'O':1.1, 'Ó':1.1, 'P':1.2, 'Q':1.2, 'R':1.1, 'S':1.1, 'Ś':1.1, 'T':1.1, 'U':1.1, 'V':1.1, 'W':1.3, 'X':1.1, 'Y':1.1, 'Z':1.1, 'Ź':1.1, 'Ż':1.1, '0':0.7, '1':0.65, 
                            '2':0.7, '3':0.7, '4':0.7, '5':0.7, '6':0.7, '7':0.7, '8':0.7, '9':0.7, '`':0.25, '~':0.5, '!':0.25, '@':1, '#':1, '$':1, '%':1.1, '^':0.6, '&':1, '*':0.4, '(':0.25, 
                            ')':0.25, '-':0.3, '_':0.8, '=':1, '+':1, '[':0.3, ']':0.3, '{':0.25, '}':0.25, '\\':1, '|':0.25, ';':0.25, ':':0.25, "'":0.25, '"':0.25, ',':0.25, '<':0.8, '.':0.25, 
                            '>':0.8, '/':0.5, '?':0.5, ' ':0.4, "    ":2.4, '—':0.8}
        
        for l in string:
            if l.islower():
                self.stringWidth += letterWidth[l] * 1.30
            elif l.isupper():
                self.stringWidth += letterWidth[l] * 1.25
            elif l.isdigit():
                self.stringWidth += letterWidth[l] * 1.43
            else:
                self.stringWidth += letterWidth[l] * 1.45
        del letterWidth
    
    # function that creates a preview before renaming files
    def _preview(self):
        newNameWidthList = []
        self.generatePreview = 'yes'
        
        super().action(self.generatePreview)
        if self.stopActionFunc == "Yes":
            pass
        else: 
            self.beforePreview()
            self.previewTextAfter.configure(state='normal')
            self.previewTextAfter.delete('1.0', tk.END)
           
            if self.addTextCheckVar.get() == 0:
                self.newText = ''
            else:
                self.newText = self.newTextVar.get()
            
            for f in range(len(self.newNameList)):
                self.previewTextAfter.insert(tk.INSERT, f"{self.newNameList[f]}\n") 
                self.textFieldAutoFit(self.newNameList[f])
                if self.changePartNameVar.get() == 1:
                    startIndexBefore = self.oldNameList[f].find(self.toConvert1.get())
                    startIndexAfter = self.newNameList[f].find(self.afterConvert1.get())
                    endIndexBefore = startIndexBefore + len(self.toConvert1.get())
                    endIndexAfter = startIndexAfter + len(self.afterConvert1.get())
                else:
                    startIndexBefore = int(self.startIVar)-1
                    startIndexAfter = self.newNameList[f].find(self.newText)
                    endIndexBefore = startIndexBefore + int(self.lengthIVar)
                    endIndexAfter = startIndexAfter + len(self.newText)
                
                if startIndexBefore != -1:
                    self.previewText.tag_add("before", f"{f+1}.{startIndexBefore}", f"{f+1}.{endIndexBefore}")
                    self.previewText.tag_configure("before", background="white", foreground="red") 
                    self.previewTextAfter.tag_add("after", f"{f+1}.{startIndexAfter}", f"{f+1}.{endIndexAfter}")
                    self.previewTextAfter.tag_configure("after", background="white", foreground="green")
                    if self.checkNumVar.get() == 1:
                        self.previewTextAfter.tag_add("after", f"{f+1}.{0}", f"{f+1}.{len(self.addNumList[f])}")
                        self.previewTextAfter.tag_configure("after", background="white", foreground="green")

                newNameWidthList.append(self.stringWidth)
             
            if round(max(newNameWidthList)) +  round(max(self.nameWidthList)) < 180:
                self.previewTextAfter.configure(width=round(max(newNameWidthList)))
            else: self.previewTextAfter.configure(width=180 - round(max(self.nameWidthList)) if round(max(self.nameWidthList)) <= 90 else 90)
            self.previewTextAfter.configure(state='disabled')
            del self.nameWidthList, newNameWidthList
    # function to undo changes after renaming files        
    def _back(self):
        self.backButton.configure(state='disabled')
        a = 0
        for f in self.newNameList:
            full_newName = os.path.join(self.location, f)
            full_oldName = os.path.join(self.location, self.oldNameList[a])
            if full_newName != full_oldName:
                os.rename(full_newName, full_oldName)
            a += 1
        self.beforePreview()
    
    # function clearing all entry and text fields
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
        
        self.startIndexVar.set('')
        self.lengthIndexVar.set('')
        self.newTextVar.set('') 
        self.standardNumeration.set('')
        self.seriesNumeration1.set('')
        self.seriesNumeration2.set('')
        self.sepVar.set('')

reNameObj = ReName() 
reNameObj.win.mainloop()

