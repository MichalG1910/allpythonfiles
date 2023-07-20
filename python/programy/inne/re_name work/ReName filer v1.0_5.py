import tkinter as tk
from tkinter import ttk
import os, sys, string, re
import tkinter.filedialog as fd
from tkinter import PhotoImage
from os import listdir
import psutil
from tkinter import messagebox as mBox
#aaa = [sdiskpart(device='/dev/nvme0n1p7', mountpoint='/', fstype='ext4', opts='rw,relatime,errors=remount-ro', maxfile=255, maxpath=4096), sdiskpart(device='/dev/loop0', mountpoint='/snap/bare/5', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop1', mountpoint='/snap/core/15419', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop2', mountpoint='/snap/core/15511', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop3', mountpoint='/snap/core18/2751', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop4', mountpoint='/snap/core18/2785', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop5', mountpoint='/snap/core20/1950', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop6', mountpoint='/snap/core20/1974', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop7', mountpoint='/snap/core22/806', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop8', mountpoint='/snap/core22/817', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop9', mountpoint='/snap/cups/962', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop10', mountpoint='/snap/cups/974', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop11', mountpoint='/snap/curl/1679', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop12', mountpoint='/snap/curl/1754', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop14', mountpoint='/snap/dbeaver-ce/242', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop13', mountpoint='/snap/dbeaver-ce/239', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop15', mountpoint='/snap/firefox/2800', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop16', mountpoint='/snap/firefox/2850', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop17', mountpoint='/snap/gimp/393', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop19', mountpoint='/snap/gnome-3-38-2004/143', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop18', mountpoint='/snap/gnome-3-38-2004/140', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop21', mountpoint='/snap/gnome-42-2204/120', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop20', mountpoint='/snap/gnome-42-2204/111', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop22', mountpoint='/snap/gtk2-common-themes/13', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop23', mountpoint='/snap/gtk-common-themes/1535', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop24', mountpoint='/snap/snap-store/959', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop25', mountpoint='/snap/snapd/19361', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop26', mountpoint='/snap/snapd/19457', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop27', mountpoint='/snap/snapd-desktop-integration/57', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/loop28', mountpoint='/snap/snapd-desktop-integration/83', fstype='squashfs', opts='ro,nodev,relatime,errors=continue,threads=single', maxfile=256, maxpath=4096), sdiskpart(device='/dev/nvme0n1p7', mountpoint='/var/snap/firefox/common/host-hunspell', fstype='ext4', opts='ro,noexec,noatime,errors=remount-ro', maxfile=255, maxpath=4096), sdiskpart(device='/dev/nvme0n1p3', mountpoint='/boot/efi', fstype='vfat', opts='rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro', maxfile=1530, maxpath=4096), sdiskpart(device='/dev/nvme0n1p1', mountpoint='/media/micha/EFI', fstype='vfat', opts='rw,nosuid,nodev,relatime,uid=1000,gid=1000,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,showexec,utf8,flush,errors=remount-ro', maxfile=1530, maxpath=4096), sdiskpart(device='/dev/nvme0n1p4', mountpoint='/media/micha/2E8A5B568A5B1A23', fstype='fuseblk', opts='ro,nosuid,nodev,relatime,user_id=0,group_id=0,default_permissions,allow_other,blksize=4096', maxfile=255, maxpath=4096), sdiskpart(device='/dev/nvme0n1p6', mountpoint='/media/micha/Nowy', fstype='ntfs3', opts='rw,nosuid,nodev,relatime,uid=1000,gid=1000,iocharset=utf8,windows_names', maxfile=255, maxpath=4096), sdiskpart(device='/dev/nvme0n1p8', mountpoint='/media/micha/DriverCD', fstype='ntfs3', opts='rw,nosuid,nodev,relatime,uid=1000,gid=1000,iocharset=utf8,windows_names', maxfile=255, maxpath=4096)]
# mbox w dodaj/usuń - wprowadzony indeks i ilość znaków nie może być większa niż najkrotsza nazwa pliku - zrobiono

# mbox dla pustego pola z lokalizacją katalogu na którym pracujemy - zrobiono
# treeview - proba dodania katalogu bez plików do podglądu - bład ValueError zrobiono
# otwieranie katalogu bez uprawnień doniego - PermissionError: [WinError 5] Odmowa dostępu: 'N:\\Aster Integration Stream' 113 wiersz - zrobiono

class Tree():
    def __init__(self):
        self.filePath = os.path.dirname(sys.argv[0])
        self.home_directory = os.path.expanduser( '~' )
        self.getDrivesName()
        
    def getDrivesName(self):
        data1 = {} 
        self.linuxMountpoint = []   
        self.win_drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:\\' % d)]
        self.linux_drives = ['/dev/sda%s' % d for d in range(100) if os.path.exists('/dev/sda%s' % d)]
        self.psutil_drives = psutil.disk_partitions(all=False)
        #data = ({v.device : v.mountpoint for v in self.psutil_drives if v.fstype != 'squashfs' and v.device not in self.psutil_drives})
        for v in self.psutil_drives:
            if v.fstype != 'squashfs' and v.device not in data1.values():
                try:
                    os.listdir(v.mountpoint)
                    data1[v.mountpoint] = v.device
                    self.linuxMountpoint.insert(1,v.mountpoint)
                except PermissionError:
                    pass
        '''
        for p in self.psutil_drives:
            
            if p.mountpoint == '/':
                self.linux_drives.insert(0,p.device)
                self.linuxMountpoint.insert(1,p.mountpoint)
            
            if p.fstype != 'squashfs':
                self.linux_drives.insert(0,p.device)
                self.linuxMountpoint.insert(1,p.mountpoint)
    '''
        self.os_drives = set(self.win_drives + self.linuxMountpoint)
        self.os_drives = list(self.os_drives)
        #print(self.linux_drives)
        #print(self.linuxMountpoint)
    
    def diskButton(self):
        #pressedButton = ttk.Style()
        #pressedButton.configure("PRESS.TButton")
        #pressedButton.map('PRESS.TButton', foreground=[('pressed', 'gray'), ('active', 'white')], bordercolor=[('disabled', 'red'), ('active', 'green')])
        self.diskButName = []
        b = 0
        padAgr = 0
        for diskLetter in self.os_drives:
           
            globals()['diskButVar{}'.format(b)] = tk.StringVar() 
            globals()['diskButVar{}'.format(b)].set(f'{b}')
            globals()['diskBut{}'.format(b)] = ttk.Button(self.treeFrame, text=diskLetter,width=2, command=self.changeDiskLetter)
            globals()['diskBut{}'.format(b)].grid(column=0, row=0, padx=2 + padAgr ,sticky='W', pady=(0,5))
            globals()['diskBut{}'.format(0)].configure(state='normal')
            b += 1
            padAgr += 40
            self.diskButName.append('diskBut{}'.format(b))
        globals()['diskBut{}'.format(0)].configure(style='Accent.TButton')   
        print(self.diskButName)
    def changeDiskLetter(self):
        print('bio')
        '''
        takefocus = globals()['diskBut{}'.format(b)]['takefocus']
        for v in range(len(self.diskButName)):
            if self.diskButName[v]['style'] == 'Accent.TButton':
        '''
    

    def _tree(self, master, path):
        def _treeReset(): 
            self._tree(reNameObj.win, path=self.os_drives)
            self.tree.bind("<Double-1>",self.OnDoubleClick)      
           
        self.fileIcon = PhotoImage(file=f'{self.filePath}/file18t.png')
        self.folderIcon = PhotoImage(file=f'{self.filePath}/folder18t.png')
        self.openfolderIcon = PhotoImage(file=f'{self.filePath}/openfolder18t.png')
        self.errorfolderIcon = PhotoImage(file=f'{self.filePath}/error folder.png')
        self.nodes = dict()
        self.nodesAll = dict()
        #self.treeFrame = ttk.LabelFrame(self.win, text='TREE',labelanchor='n')
        #self.treeFrame.grid(column=1, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.treeFrame = ttk.Frame(master, height=20)
        self.treeFrame.grid(column=1, row=0, sticky="NSEW", padx=10, pady=(55,10),)
        #self.diskButton()
        self.tree = ttk.Treeview(self.treeFrame, height=20, show='tree headings')
        ysb = ttk.Scrollbar(self.treeFrame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self.treeFrame, orient='horizontal', command=self.tree.xview)
        self.tree.heading('#0', text='Reset tree', anchor='w',command=_treeReset)
        self.tree.column('#0', minwidth=620, stretch=True, anchor='w', width=300 )
        self.tree.configure(xscrollcommand=xsb.set, yscrollcommand=ysb.set, )
        
        self.tree.grid(column=0, row=1)
        ysb.grid(row=1, column=1, sticky='ns')
        xsb.grid(row=2, column=0, sticky='ew')
        self.insert_node('', self.home_directory, self.home_directory, self.folderIcon)
        for i in range(len(path)):
            abspath = os.path.abspath(path[i-1])
            driveText = abspath[abspath.rfind('/')+1:] 
            if len(driveText) > 15:
                a=i
                if a == 0: a=''
                driveText = f"Wolumin{a}"
            elif len(driveText) == 0: 
                driveText = "Ubuntu" 
            self.insert_node('', driveText, abspath, self.folderIcon)
            i += 1
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind('<<TreeviewClose>>', self.close_node)

    def insert_node(self, parent, text, abspath, img):
        self.parent = parent
        self.text = text
       # node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath) :
            node = self.tree.insert(parent, 'end', text=text, image=img, open=False)
            self.nodes[node] = abspath
            self.nodesAll[node] = abspath
            self.tree.insert(node, 'end')
            
        else:
            node = self.tree.insert(parent, 'end', text=text, image=img, open=False)
    
    def close_node(self,event):
        node = self.tree.focus()
        print(node)
        path = os.path.abspath(self.nodesAll[node])
        try:
            os.listdir(path)
            img=self.folderIcon
        except PermissionError:
            img=self.errorfolderIcon
        self.tree.item(node, image=img, open=False)

    def open_node(self, event):
        node = self.tree.focus()
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
                mBox.showerror("Brak dostępu", "Nie masz uprawnień do dostępu do tego katalogu")
                img=self.errorfolderIcon
                
                #self.insert_node(self.tree.parent(node), self.text, abspath, img)
                #self.tree.insert(self.path, 'end', image=img)

    def OnDoubleClick(self, event):
        reNameObj._clear()
        self.directory = False
        item = self.tree.selection()[0]
        parent_iid = self.tree.parent(item)
        node = []
        # go backward until reaching root
        while parent_iid != '':
            
            node.insert(0, self.nodesAll[parent_iid])
            parent_iid = self.tree.parent(parent_iid)
        i = self.nodesAll[item]
        self.path = os.path.join(*node, i)
        
        try:
            os.listdir(self.path)
            reNameObj.location1.set(self.path)
            reNameObj.beforePreview()    
        except PermissionError or ValueError:
            pass

class StartAction():
    def action(self,  preview = 'no'):
        self.actionVariable()
        self.checkAddnumeration()
        if self.stopActionFunc == "Yes":
            pass
        else: 
            self.actionLoop(preview)
    
    def regexNum(self, getNum):
        return getNum.isdigit()
    
    def actionVariable(self):
        self.numeration = ""
        self.numeration2 = ""
        self.newName = ""
        self.separator = ""
        self.location = reNameObj.location1.get()
        self.afterConvert = reNameObj.afterConvert1.get()
        self.toConvert = reNameObj.toConvert1.get()
        self.oldNameList, self.oldNameLenList, self.newNameList, self.addNumList = [],[],[],[]
        if reNameObj.deleteAddVar.get() == 1:
            if self.regexNum(reNameObj.startIndexVar.get()) == True and self.regexNum(reNameObj.lengthIndexVar.get()) == True:
                self.startIVar = int(reNameObj.startIndexVar.get())
                self.lengthIVar = int(reNameObj.lengthIndexVar.get())
            elif reNameObj.startIndexVar.get() != '' and self.regexNum(reNameObj.startIndexVar.get()) == False or reNameObj.lengthIndexVar.get() != '' and self.regexNum(reNameObj.lengthIndexVar.get()) == False:
                mBox.showerror("Uwaga", "wprowadź liczbę")
            else: 
                self.startIVar = 1
                self.lengthIVar = 0
        #self.addTextCheckVar = reNameObj.addTextCheckVar.get()
        self.newTxtVar = reNameObj.newTextVar.get()

    def checkAddnumeration(self):
        if reNameObj.checkNumVar.get() == 1 and reNameObj.standardVar.get() == 1:
            if self.regexNum(reNameObj.standardNumeration.get()) == True:
                self.numeration = int(reNameObj.standardNumeration.get())
                self.separator = reNameObj.sepVar.get()
                self.numeration2 = None
                self.stopActionFunc = 'No'
            else: 
                mBox.showerror("Uwaga", "wprowadź liczbę")
                self.stopActionFunc = 'Yes'

        elif reNameObj.checkNumVar.get() == 1 and reNameObj.seriesVar.get() == 1:
            if self.regexNum(reNameObj.seriesNumeration1.get()) == True and self.regexNum(reNameObj.seriesNumeration2.get()) == True:
                self.numeration = int(reNameObj.seriesNumeration1.get())
                self.numeration2 = int(reNameObj.seriesNumeration2.get())
                self.separator = reNameObj.sepVar.get()
                self.stopActionFunc = 'No'
            else: 
                mBox.showerror("Uwaga", "wprowadź liczbę")
                self.stopActionFunc = 'Yes'
        else: 
            self.numeration = None
            self.numeration2 = None
            self.stopActionFunc = 'No'
        return self.stopActionFunc
    
    def actionLoop(self,preview): 
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
        
        def renameFunc(oldName, newName, full_oldName):
            if oldName != newName:
                full_newName = os.path.join(self.location, newName)
                if preview == 'no':
                    os.rename(full_oldName, full_newName)
            self.oldNameLenList.append(len(oldName))
            self.newNameList.append(newName)
            self.oldNameList.append(oldName)
        
        def loop():
            for oldName in reNameObj.objsPreview:
                full_oldName = os.path.join(self.location, oldName)
                if os.path.isfile(full_oldName):                                # FRAME zmiana częsci nazwy
                    if reNameObj.changePartNameVar.get() == 1:
                        if self.numeration != None:                               # samo dodanie numeracji
                            if reNameObj.toConvert1.get() == '' and reNameObj.afterConvert1.get() == '':
                                addNumeration(oldName, self.afterConvert, self.toConvert)  
                            elif oldName.find(self.toConvert) != -1:             # dodanie numeracji i zmiana cześci nazwy
                                addNumeration(oldName, self.afterConvert, self.toConvert)
                            else:
                                self.newName = oldName.replace(self.toConvert, self.afterConvert, 1) 
                                self.addNumList.append(0)
                        else:                                               # standardowa zamiana/usuniecie części nazwy bez zamiany na inną bez numeracji
                            self.newName = oldName.replace(self.toConvert, self.afterConvert, 1)
                    else:                                                        # FRAME dodaj/usuń
                        if self.numeration != None:                               # samo dodanie numeracji
                            if self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 0:
                                self.afterConvert = ''
                                addNumeration(oldName, self.afterConvert)  
                            elif self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 1:             # dodanie numeracji i zmiana cześci nazwy
                                self.afterConvert = self.newTxtVar
                                addNumeration(oldName, self.afterConvert)
                            else:
                                # tu mbox
                                pass
                        else:                                               # standardowa zamiana/usuniecie części nazwy bez zamiany na inną bez numeracji
                            if self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 0:
                                self.afterConvert = ''
                            elif self.startIVar != '' and self.lengthIVar != '' and reNameObj.addTextCheckVar.get() == 1:             # dodanie numeracji i zmiana cześci nazwy
                                self.afterConvert = self.newTxtVar
                            if len(oldName)-len(oldName[oldName.rfind('.'):])+1 <= self.startIVar + self.lengthIVar-1:
                                mBox.showerror('nie można zmieniuć pliku', 'Przekroczono maksymalną liczbę zmienianych liter, wprowadź mniejszą liczbę')
                                self.stopActionFunc = 'Yes'
                                break 
                            self.newName = oldName.replace(oldName[(self.startIVar-1):(self.startIVar-1+self.lengthIVar)], self.afterConvert, 1)
                    renameFunc(oldName, self.newName, full_oldName)
        
        def ifNoPreview():
            if preview == 'no':
                reNameObj.toConvert1.set('')
                reNameObj.afterConvert1.set('')
                reNameObj.previewTextAfter.configure(state='normal')
                reNameObj.previewTextAfter.delete('1.0', tk.END)
                reNameObj.previewTextAfter.configure(state='disabled')
                #self.oldNameList = self.objsPreview
                reNameObj.beforePreview()
                reNameObj.backButton.configure(state='normal')
        
        if self.location != '': 
            loop()
            if self.stopActionFunc == 'No':        
                ifNoPreview()
            else:
                reNameObj._clear()
        else: 
            mBox.showerror("Nie wybrano katalogu roboczego", "Wybierz katalog roboczy, aby kontynuować")
            self.stopActionFunc ='Yes'
               
class ReName(Tree, StartAction):
    def __init__(self):
        self.win = tk.Tk()
        super().__init__()
        self.winStyle(self.win)
        self.win.title("ReName filer v1.0")
        self.directory = None
        self.widgets()
        self.previewWidgets()
        self.strLen = None
        self.dirButton.bind("<Button-1>", self.ask_dir)
        self.tree.bind("<Double-1>", super().OnDoubleClick)
        # self.win.iconbitmap('./ikona2.ico')

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
        
    def winStyle(self, window):
        window.tk.call('source', os.path.join(self.filePath, 'forest-dark.tcl'))
        ttk.Style().theme_use('forest-dark')
    
    def ask_dir(self, event):
        self._clear()
        self.directory = fd.askdirectory()
        self.beforePreview()
    
    def beforePreview(self):
        #objsPreviewLenList, multiplierList, winWidthDict = [],[],{}
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
                #objsPreviewLenList.append(len(self.objsPreview[a]))
                #multiplierList.append(self.multiplier)
                #winWidthDict[len(self.objsPreview[a])] = self.multiplier
                a += 1
        '''
        winWidthList = [key * winWidthDict[key] for key in winWidthDict]
        print(winWidthList)
        if (max(objsPreviewLenList)+round(max(winWidthList) / 3.2)) > 48:
            self.previewText.configure(width=max(objsPreviewLenList)+round(max(winWidthList) / 3.2))
        '''
        if self.nameWidthList == []: pass
        elif round(max(self.nameWidthList)) < 90:
            self.previewText.configure(width=round(max(self.nameWidthList)))
        else: self.previewText.configure( width = 90 )
        
        self.previewText.configure(state="disabled")
 
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
        self.numLabel = ttk.Label(self.numerationFrame, text = "Zacznij od:")
        self.numLabel.grid(column = 0, row = 1, sticky="W", padx=10, pady=2)
        self.num = ttk.Entry(self.numerationFrame, width= 6, textvariable=self.standardNumeration)
        self.num.grid(column= 0, row= 1, sticky = "W", padx=(80,0))
        self.sepLabel = ttk.Label(self.numerationFrame, text = "separator:")
        self.sepLabel.grid(column = 0, row = 1, sticky="W", padx=(180,0), pady=2)
        self.sepEntry = ttk.Entry(self.numerationFrame, width= 4, textvariable=self.sepVar)
        self.sepEntry.grid(column= 0, row= 1, sticky = "W", padx=(245,0), pady=(10,10))
    
    def activateSeriesEntry(self):
        try:
            self.numLabel.destroy()
            self.num.destroy()
            del self.numLabel, self.num
        except: pass
        
        self.numLabel = ttk.Label(self.numerationFrame, text = "")
        self.numLabel.grid(column = 0, row = 1, sticky="NSWE") # przysłania
        self.numLabel = ttk.Label(self.numerationFrame, text = "Zacznij od: S")
        self.numLabel.grid(column = 0, row = 1, sticky="W", padx=10, pady=2)
        self.num = ttk.Entry(self.numerationFrame, width= 2, textvariable=self.seriesNumeration1)
        self.num.grid(column= 0, row=1, sticky = "W", padx=(89,0))
        self.numLabel1 = ttk.Label(self.numerationFrame, text = "E")
        self.numLabel1.grid(column = 0, row = 1, sticky="W", padx=(122,0), pady=2)
        self.num1 = ttk.Entry(self.numerationFrame, width= 2, textvariable=self.seriesNumeration2)
        self.num1.grid(column= 0, row= 1, sticky = "W", padx=(136,0))
        self.sepLabel = ttk.Label(self.numerationFrame, text = "separator:")
        self.sepLabel.grid(column = 0, row = 1, sticky="W", padx=(180,0), pady=2)
        self.sepEntry = ttk.Entry(self.numerationFrame, width= 4, textvariable=self.sepVar)
        self.sepEntry.grid(column= 0, row= 1, sticky = "W", padx=(245,0), pady=(10,10))
    
    def chooseActivateEntry(self):
        if self.standardVar.get() == 1 and self.seriesVar.get() == 0:
            self.activateStandardEntry()
        elif self.standardVar.get() == 0 and self.seriesVar.get() == 1:
            self.activateSeriesEntry()
    
    def chooseActivateEntry1(self):
        if self.standardVar.get() == 0 and self.seriesVar.get() == 1:
            self.activateSeriesEntry()
        elif self.standardVar.get() == 1 and self.seriesVar.get() == 0:
            self.activateStandardEntry()
    
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
        
    def traceNumerationSelection(self):         
        self.standardVar.trace('w', lambda unused0, unused1, unused2 : self.numerationSelection1())
        self.seriesVar.trace('w', lambda unused0, unused1, unused2 : self.numerationSelection2())

    def ruleFrame1(self, *ignoredArgs):
        if self.changePartNameVar.get() == 0:
            self.deleteAddVar.set(1)
            self.changeStatePartName()
            self.changeStateDelAdd()
        elif self.changePartNameVar.get() == 1:         
            self.deleteAddVar.set(0)
            self.changeStatePartName()
            self.changeStateDelAdd()
            
    def ruleFrame2(self, *ignoredArgs):
        if self.deleteAddVar.get() == 0:
            self.changePartNameVar.set(1)
            self.changeStatePartName()
            self.changeStateDelAdd()
        elif self.deleteAddVar.get() == 1:         
            self.changePartNameVar.set(0)
            self.changeStatePartName()
            self.changeStateDelAdd() 
        
    def traceSelectRuleFrame(self):         
        self.changePartNameVar.trace('w', lambda unused0, unused1, unused2 : self.ruleFrame1())
        self.deleteAddVar.trace('w', lambda unused0, unused1, unused2 : self.ruleFrame2())
    
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

    def changeStateAddText(self):
        if self.addTextCheckVar.get() == 0:
            self.newTextEntry.configure(state='disabled')
        else: self.newTextEntry.configure(state='normal')          
    
    def widgets(self):
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
        
       
        #################################### kolumna 1 #######################################################
        #changePartNameChb.grid(column= 0, row= 7, sticky= tk.W, padx=10, pady=10)
        self.mainFrame = ttk.LabelFrame(self.win, labelanchor='n', text='dostępne akcje')
        self.mainFrame.grid(column=0, row=0,columnspan=1, sticky="NSWE", padx=10, pady=(10,10))
        
        # zmień fragment nazwy
        changePartNameChb = ttk.Checkbutton(variable=self.changePartNameVar,  text='zmień fragment nazwy', command= self.changeStatePartName,)
        self.changePartNameVar.set(1)
        self.changePartNameFrame = ttk.LabelFrame(self.mainFrame, labelanchor='n', labelwidget=changePartNameChb)
        self.changePartNameFrame.grid(column=0, row=0,columnspan=1, sticky="NSWE", padx=10, pady=(10,10))

        self.textToChangeLab = ttk.Label(self.changePartNameFrame, text = "Tekst do zmiany:")
        self.textToChangeLab.grid(column = 0, row = 1, padx=10, pady=(10,2))
        self.toConv = ttk.Entry(self.changePartNameFrame, width= 40, textvariable= self.toConvert1) 
        self.toConv.grid(column= 0, row= 2, padx=10, pady=(0,5))

        self.changeToLab = ttk.Label(self.changePartNameFrame, text = "Zmienić na:")
        self.changeToLab.grid(column = 0, row = 3, padx=10, pady=(10,2)) 
        self.aConv = ttk.Entry(self.changePartNameFrame, width= 40, textvariable= self.afterConvert1) 
        self.aConv.grid(column= 0, row= 4, padx=10, pady=(0,10))
        
        # usuń/dodja w nazwie 
        deleteAddChb = ttk.Checkbutton(variable=self.deleteAddVar,  text='usuń/dodaj w nazwie', command= self.changeStateDelAdd)
        self.deleteAddVar.set(0)
        self.deleteAddFrame = ttk.LabelFrame(self.mainFrame, labelanchor='n', labelwidget=deleteAddChb, width=320, height=180)
        self.deleteAddFrame.grid(column=0, row=1,columnspan=2, sticky="NSWE", padx=10, pady=(10,10))

        self.startIndex = ttk.Label(self.deleteAddFrame, text = "Indeks znaku:", state='disabled')
        self.startIndex.grid(column = 0, row = 0, padx=10, pady=(8,2), sticky = "W")
        self.startIndexEntry = ttk.Entry(self.deleteAddFrame, width= 3, textvariable= self.startIndexVar, state='disabled') 
        self.startIndexEntry.grid(column= 0, row= 0, padx=(100,10), pady=(10,10))
        
        self.lenght = ttk.Label(self.deleteAddFrame, text = "ilość znaków:", state='disabled')
        self.lenght.grid(column = 1, row = 0, pady=(8,2), sticky="W")
        self.lenghtEntry = ttk.Entry(self.deleteAddFrame, width= 3, textvariable= self.lengthIndexVar, state='disabled') 
        self.lenghtEntry.grid(column= 1, row= 0, padx=(87,10), pady=(10,10))

        self.addTextCheck = ttk.Checkbutton(self.deleteAddFrame, variable=self.addTextCheckVar,  text='zastąpić tekstem', command=self.changeStateAddText, state='disabled')
        self.addTextCheck.grid(column= 0, row= 1, padx=(10,10), pady=(0,10))
        self.newTextEntry = ttk.Entry(self.deleteAddFrame, textvariable= self.newTextVar, state='disabled') 
        self.newTextEntry.grid(column= 1, row= 1, padx=(0,10), pady=(0,10), sticky="NSWE")


        # numeracja
        checkNumerationWidget = ttk.Checkbutton(variable=self.checkNumVar, text= "Wprowadzić numerację?", command=self.changeStateNumeration) 
        self.checkNumVar.set(0)
        self.numerationFrame = ttk.LabelFrame(self.mainFrame, labelanchor='n', labelwidget=checkNumerationWidget, width=320, height=180)
        self.numerationFrame.grid(column=0, row=2,columnspan=2, sticky="NSWE", padx=10, pady=(10,10))
        
        self.checkStandard = ttk.Checkbutton(self.numerationFrame, text= "zwykła", variable=self.standardVar, command= self.chooseActivateEntry, state='disabled') 
        self.checkStandard.grid(column= 0, row= 0, sticky= tk.W, padx=10, pady=2)
        self.standardVar.set(1)
        self.checkSeries = ttk.Checkbutton(self.numerationFrame, text= "serialowa (np. S01E01)", variable=self.seriesVar, command= self.chooseActivateEntry1, state='disabled') 
        self.checkSeries.grid(column= 0, row= 0, sticky= tk.W, padx=(150,0), pady=2)
        self.traceNumerationSelection()
        self.activateStandardEntry()
        self.changeStateNumeration()
        self.traceSelectRuleFrame()
        
        # przyciski akcji
        startButton = ttk.Button(self.mainFrame, text= "Start", command= super().action)
        startButton.grid(column= 0, row= 11, sticky="W", padx=10, pady=10)
        previewButton = ttk.Button(self.mainFrame, text= "Podgląd", command= self._preview)
        previewButton.grid(column= 0, row= 11, sticky="N", padx=10, pady=10)
        exitButton = ttk.Button(self.mainFrame, text= "Zamknij", command= self._quit)
        exitButton.grid(column= 0, row= 11, sticky="E", padx=10, pady=10)
        disabledButton = ttk.Style()
        disabledButton.configure("DS.TButton")
        disabledButton.map('DS.TButton', foreground=[('disabled', 'gray'), ('active', 'white')])
        self.backButton = ttk.Button(self.mainFrame, text= "Cofnij", command= self._back, style='DS.TButton', state='disabled')
        self.backButton.grid(column= 0, row= 12, sticky="W", padx=10, pady=(0,10))
        clearButton = ttk.Button(self.mainFrame, text= "Wyczyść", command= self._clear)
        clearButton.grid(column= 0, row= 12, sticky="N", padx=10, pady=(0,10))
        
        # puste rzędy do przysłaniania
        #self.numLabel = ttk.Label(self.mainFrame)
        #self.numLabel.grid(column = 0, row = 3, sticky="W", padx=10, pady=10) # pełni rolę pustego rzędu
        #self.numLabel1 = ttk.Label(self.mainFrame).grid(column = 0, row = 4, sticky="W", padx=10, pady=10) # pełni rolę pustego rzędu
        #self.numLabel2 = ttk.Label(self.mainFrame).grid(column = 0, row = 5, sticky="W", padx=10, pady=10) # pełni rolę pustego rzędu
        
        ###################################### kolumna 2 ######################################################
        # wybór katalogu
        self.folderLocLab = ttk.Label(self.win, text = "folder:")
        self.folderLocLab.grid(column = 1, row = 0,  padx=10, pady=(20,5), sticky="NW")
        self.lok = ttk.Entry(self.win, text=self.directory, width= 34, textvariable= self.location1)   
        self.lok.grid(column= 1, row= 0, padx=10, pady=(15,5), sticky="N")
        self.icon = PhotoImage(file=f'{self.filePath}/folder24dp.png')
        TButton1 = ttk.Style()
        TButton1.configure("New.TButton", width = 5, border = 2, padding= {0,0,0,0})
        self.dirButton = ttk.Button(self.win, image= self.icon, command= self.ask_dir, style='New.TButton',)
        self.dirButton.grid(column= 1, row= 0, sticky="NE", padx=10, pady=15)

        # widok drzewa katalogów
        super()._tree(self.win, path=self.os_drives)   
    
    def previewWidgets(self):
        def multiple_yview(*args):
            self.previewText.yview(*args)
            self.previewTextAfter.yview(*args)
        def on_textscroll(*args):
            scrollbarVer.set(*args)
            multiple_yview('moveto', args[0])
        
        self.previewFrame = ttk.LabelFrame(self.win, text='Podgląd',labelanchor='n')
        self.previewFrame.grid(column=2, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.previewText = tk.Text(self.previewFrame, width=48, height=23, wrap= tk.NONE, background='white', foreground='black')
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
        

    def textFieldAutoFit(self, string):
        self.stringWidth = 0
        self.letterWidth = {'a':0.8, 'ą':0.8, 'b':0.8, 'c':0.8, 'ć':0.8, 'd':0.8, 'e':0.8, 'ę':0.8, 'f':0.8, 'g':0.8, 'h':0.8, 'i':0.33, 'j':0.33, 'k':0.8, 'l':0.33, 'ł':0.6, 'm':0.9, 'n':0.8,
                            'ń':0.8, 'o':0.8, 'ó':0.8, 'p':0.8, 'q':0.8, 'r':0.8, 's':0.8, 'ś':0.8, 't':0.8, 'u':0.8, 'v':0.8, 'w':0.9, 'x':0.8, 'y':0.9, 'z':0.8, 'ź':0.8, 'ż':0.8, 'A':1.1,
                            'Ą':1.1, 'B':1.1, 'C':1.1, 'Ć':1.1, 'D':1.1, 'E':1.2, 'Ę':1.1, 'F':1.1, 'G':1.2, 'H':1.1, 'I':0.35, 'J':1.1, 'K':1.2, 'L':1.1, 'Ł':1.1, 'M':1.3, 'N':1.1, 'Ń':1.1, 
                            'O':1.1, 'Ó':1.1, 'P':1.2, 'Q':1.2, 'R':1.1, 'S':1.1, 'Ś':1.1, 'T':1.1, 'U':1.1, 'V':1.1, 'W':1.3, 'X':1.1, 'Y':1.1, 'Z':1.1, 'Ź':1.1, 'Ż':1.1, '0':0.7, '1':0.65, 
                            '2':0.7, '3':0.7, '4':0.7, '5':0.7, '6':0.7, '7':0.7, '8':0.7, '9':0.7, '`':0.25, '~':0.5, '!':0.25, '@':1, '#':1, '$':1, '%':1.1, '^':0.6, '&':1, '*':0.4, '(':0.25, 
                            ')':0.25, '-':0.3, '_':1, '=':1, '+':1, '[':0.3, ']':0.3, '{':0.25, '}':0.25, '\\':1, '|':0.25, ';':0.25, ':':0.25, "'":0.25, '"':0.25, ',':0.25, '<':0.8, '.':0.25, 
                            '>':0.8, '/':0.5, '?':0.5, ' ':0.6, "    ":2.4, '—':0.8}
        
        for l in string:
            if l.islower():
                self.stringWidth += self.letterWidth[l] * 1.30
            elif l.isupper():
                self.stringWidth += self.letterWidth[l] * 1.2
            elif l.isdigit():
                self.stringWidth += self.letterWidth[l] * 1.43
            else:
                self.stringWidth += self.letterWidth[l] * 1.55

        
        '''
        upperLetter = len([i for i in string if i.isupper()==True])
        self.multiplier = upperLetter / len(string)
        if self.multiplier < 0.5:
            self.multiplier = 0.5
    '''
    def _preview(self):
        multiplierList, newNameLenList, winWidthDict, newNameWidthList = [],[],{},[]
        self.generatePreview = 'yes'
        
        super().action(self.generatePreview)
        if self.stopActionFunc == "Yes":
            pass
        else: 
           
            self.beforePreview()
            
            self.previewTextAfter.configure(state='normal')
            self.previewTextAfter.delete('1.0', tk.END)
            
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
                    startIndexAfter = self.newNameList[f].find(self.newTextVar.get())
                    endIndexBefore = startIndexBefore + int(self.lengthIVar)
                    endIndexAfter = startIndexAfter + len(self.newTextVar.get())
                
                if startIndexBefore != -1:
                    self.previewText.tag_add("before", f"{f+1}.{startIndexBefore}", f"{f+1}.{endIndexBefore}")
                    self.previewText.tag_configure("before", background="white", foreground="red") 
                    self.previewTextAfter.tag_add("after", f"{f+1}.{startIndexAfter}", f"{f+1}.{endIndexAfter}")
                    self.previewTextAfter.tag_configure("after", background="white", foreground="green")
                    if self.checkNumVar.get() == 1:
                        self.previewTextAfter.tag_add("after", f"{f+1}.{0}", f"{f+1}.{len(self.addNumList[f])}")
                        self.previewTextAfter.tag_configure("after", background="white", foreground="green")

                newNameWidthList.append(self.stringWidth)
                #multiplierList.append(self.multiplier)
                #newNameLenList.append(len(self.newNameList[f]))
                #winWidthDict[len(self.newNameList[f])] = self.multiplier
        
            #winWidthList = [key * winWidthDict[key] for key in winWidthDict]
            #if (max(newNameLenList)+round((max(winWidthList) / 3.2))) > 48:
                #self.previewTextAfter.configure(width=max(newNameLenList)+round((max(winWidthList) / 3.2)))
            if round(max(newNameWidthList)) +  round(max(self.nameWidthList)) < 180:
                self.previewTextAfter.configure(width=round(max(newNameWidthList)))
            else: self.previewTextAfter.configure(width=180 - round(max(self.nameWidthList)) if round(max(self.nameWidthList)) <= 90 else 90)
            self.previewTextAfter.configure(state='disabled')
            print(max(self.nameWidthList), ' ', max(newNameWidthList)) # prz 184 przestaje rozszerzać
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

#treeObj= Tree() 
reNameObj = ReName() 
reNameObj.win.mainloop()

