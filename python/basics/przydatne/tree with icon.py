import tkinter as tk
from tkinter import ttk
import os, sys
from tkinter import PhotoImage
class tree:
    def __init__(self):
        self.win = tk.Tk()
        self.filePath = os.path.dirname(sys.argv[0])
        self._tree(self.win, path='\\')
        self.tree.bind("<Double-1>", self.OnDoubleClick)
    
    def OnDoubleClick(self, event):
       
        item = self.tree.selection()[0]
        parent_iid = self.tree.parent(item)
        node = []
        # go backward until reaching root
        while parent_iid != '':
            node.insert(0, self.tree.item(parent_iid)['text'])
            parent_iid = self.tree.parent(parent_iid)
        i = self.tree.item(item, "text")
        path = os.path.join(*node, i)                               # można wykorzystać jako ścieżkę do zaznaczenoego katalogu
    
    def _tree(self, master, path):
        self.fileIcon = PhotoImage(file=f'{self.filePath}/file18t.png')
        self.folderIcon = PhotoImage(file=f'{self.filePath}/folder18t.png')
        self.openfolderIcon = PhotoImage(file=f'{self.filePath}/openfolder18t.png')
        self.nodes = dict()
        #self.treeFrame = ttk.LabelFrame(self.win, text='TREE',labelanchor='n')
        #self.treeFrame.grid(column=1, row=0,columnspan=1, sticky="NSEW", padx=10, pady=(10,10))
        self.treeFrame = ttk.Frame(master, height=20)
        self.treeFrame.grid(column=1, row=0, sticky="NSEW", padx=10, pady=20,)
        self.tree = ttk.Treeview(self.treeFrame, height=17, show='tree headings')
        ysb = ttk.Scrollbar(self.treeFrame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self.treeFrame, orient='horizontal', command=self.tree.xview)
        self.tree.heading('#0', text='Project tree', anchor='w')
        self.tree.column('#0', minwidth=620, stretch=True, anchor='w', width=300 )
        self.tree.configure(xscrollcommand=xsb.set, yscrollcommand=ysb.set, )
        
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
obj = tree()
obj.win.mainloop()
