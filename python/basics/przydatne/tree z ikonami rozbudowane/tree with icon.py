import tkinter as tk
from tkinter import ttk
import os, sys
from tkinter import PhotoImage
from tkinter import messagebox as mBox

# drzewo katalogów z ikonami (zmieniającymi sie w zależności od tego, czy są rozwinięte czy zwinięte oraz czy mamy do nich dostęp)
# oraz z messageboxami na kilka możliwych akcji z wyborami katalogów (próba wejścia do zastrzeżonego katalogu, próba rozwinięcia pliku zamiast katalogu)
# w headerze funkcja resetu drzewa  

class tree:
    def __init__(self):
        self.win = tk.Tk()
        self.filePath = os.path.dirname(sys.argv[0])
        self._tree(self.win, path='\\')
        self.tree.bind("<Double-1>", self.OnDoubleClick)
    
    def _tree(self, master, path):
        def _treeReset(): 
            self._tree(self.win, path='\\')
            self.tree.bind("<Double-1>",self.OnDoubleClick)      
           
        self.fileIcon = PhotoImage(file=f'{self.filePath}/file18t.png')
        self.folderIcon = PhotoImage(file=f'{self.filePath}/folder18t.png')
        self.openfolderIcon = PhotoImage(file=f'{self.filePath}/openfolder18t.png')
        self.errorfolderIcon = PhotoImage(file=f'{self.filePath}/error folder.png')
        self.nodes = dict()
        self.nodesAll = dict()
        self.treeFrame = ttk.Frame(master, height=20)
        self.treeFrame.grid(column=1, row=0, sticky="NSEW", padx=10, pady=(55,10),)
        self.tree = ttk.Treeview(self.treeFrame, height=20, show='tree headings')
        ysb = ttk.Scrollbar(self.treeFrame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self.treeFrame, orient='horizontal', command=self.tree.xview)
        self.tree.heading('#0', text='Reset tree', anchor='w',command=_treeReset)
        self.tree.column('#0', minwidth=620, stretch=True, anchor='w', width=300 )
        self.tree.configure(xscrollcommand=xsb.set, yscrollcommand=ysb.set, )
        
        self.tree.grid(column=0, row=1)
        ysb.grid(row=1, column=1, sticky='ns')
        xsb.grid(row=2, column=0, sticky='ew')
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

    def OnDoubleClick(self, event):
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
            self.path = os.path.join(*node, i)
            
            try:
                os.listdir(self.path) 
            except PermissionError or ValueError:
                pass
        else:
            mBox.showinfo('To nie jest katalog', 'Nie da się wejść do wskazanej lokalizacji ponieważ nie jest to katalog.\nWskaż inną lokalizację')
            pass
obj = tree()
obj.win.mainloop()

# wyciągnięcie lier wszystkich dysków
'''
import os, string
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
print(available_drives)
'''