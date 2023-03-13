import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
import gc
import numpy as np
class A:
    def __init__(self):
        self.win = tk.Tk() 
        self.emptyGraph()   

    def emptyGraph(self):
        
        plt.style.use('Solarize_Light2')
        self.fig = plt.figure(figsize=(19,8), facecolor = "lightcyan")
        self.a = np.arange(1000)
        self.b = np.random.randn(1000)            
        
        self.axis = self.fig.add_subplot(111) 
        self.axis.plot(self.a, self.b) 
        self.axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
        self.axis.set_xlabel("Data") 
        self.axis.set_ylabel("PLN Złoty")
        self.fig.tight_layout()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.win) 
        self.canvas._tkcanvas.grid(column=0, row=3, columnspan=11, padx=5, pady=5) 
        self.win.update()
        self.win.deiconify()
        ttk.Button(self.win,text="refresh", command=self.refresh).grid(row=0, column=10, padx=5, pady=5, sticky="nsew")
    def refresh(self):
        self.fig.clf()
        plt.close(self.fig)
        del self.a, self.b, self.axis
        gc.collect()
        self.emptyGraph()
        
a = A()
a.win.mainloop()
'''
fig.clf()
plt.close()
del a, b
gc.collect()
'''