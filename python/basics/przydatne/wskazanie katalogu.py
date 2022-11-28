import tkinter as tk
import tkinter.filedialog as fd

import tkinter.messagebox as msb

class Application:
    def __init__(self):
        self.window = tk.Tk()
        
        self.window.bind("<Button-1>", self.on_lbc)
        
        self.window.mainloop()
        
    def on_lbc(self, event):
        directory = fd.askdirectory() # wywołanie okna dialogowego do wskazania ścieżki do folderu docelowego
        
        if directory:
            msb.showinfo("Info", "Znaleziono taki folder {folder}".format( folder = directory ))
        
apl = Application()
