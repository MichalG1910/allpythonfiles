import os, math
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
import PIL
import PIL._tkinter_finder
from classE_Rates05 import Data

class Main:
    def __init__(self):
        self.win = tk.Tk()
        dataObj.checkConnection()
        dataObj.createReportDir()
        dataObj.NBPratesUpDown()
        dataObj.latestNBPreport()
        self.winStyle()
        self.themeButton()
        self.emptyGraph()
        self.exchangeRatesTabel()
        self.graphGui()
        self.generateReportGui()
        
    
    def winStyle(self):
        self.win.tk.call('source', os.path.join(dataObj.filePath, 'azure.tcl'))
        self.win.tk.call("set_theme", "dark")

    def themeButton(self):
        def change_theme():
            if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
                self.win.tk.call("set_theme", "light")
                icon1 = PhotoImage(file=f'{dataObj.filePath}/light.png')
                self.accentbutton.configure(image=icon1)
                self.accentbutton.image = icon1
                self.refreshGraph()
                
            else:
                self.win.tk.call("set_theme", "dark")
                icon2 = PhotoImage(file=f'{dataObj.filePath}/dark.png')
                self.accentbutton.configure(image=icon2 )
                self.accentbutton.image = icon2
                self.refreshGraph()
                
        icon = PhotoImage(file=f'{dataObj.filePath}/dark.png')
        self.accentbutton = ttk.Button(self.win, image=icon, command=change_theme)
        self.accentbutton.image = icon
        self.accentbutton.grid(row=0, column=11, padx=5, pady=5, sticky="nsew")
    
    def emptyGraph(self):
        if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            fig = plt.figure(figsize=(12,8), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
            fig = plt.figure(figsize=(12,8), facecolor = "lightcyan")
        
        axis = fig.add_subplot(111) 
        axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
        axis.set_xlabel("Data") 
        axis.set_ylabel("PLN Złoty")
        canvas = FigureCanvasTkAgg(fig, master=self.win) 
        canvas._tkcanvas.grid(column=4, row=3, columnspan=8, padx=10, pady=10) 
        self.win.update()
        self.win.deiconify()

    def newGraph(self):
        dataObj.getDataForGraph(self.currencyName.get(), self.timeRange.get())
        self.refreshGraph()

    def refreshGraph(self):
        try:
            dataObj.xValues 
        except AttributeError:
            dataObj.xValues = None
            
        if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            fig = plt.figure(figsize=(12,8), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
            fig = plt.figure(figsize=(12,8), facecolor = "lightcyan")
        
        if dataObj.xValues == None:
            self.emptyGraph()
        else:
            axis = fig.add_subplot(111) 
            axis.set_title(f"{dataObj.code.upper()} {dataObj.codeCurrencyDict[dataObj.code.upper()]}", fontsize=16, color="silver")
            axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
            xValuesLen = len(dataObj.xValues)-1
            a = math.ceil(xValuesLen / 20)
            b = list(range(1,xValuesLen, a))
            b.append(xValuesLen)
            axis.plot(dataObj.xValues, dataObj.yValues) 
            xaxis = axis.get_xaxis()
            xaxis.set_ticks(b)
            plt.xticks(rotation=45, fontsize=8)
            axis.set_xlabel("Data") 
            axis.set_ylabel("PLN Złoty")
            canvas = FigureCanvasTkAgg(fig, master=self.win) 
            canvas._tkcanvas.grid(column=4, row=3, columnspan=8, padx=5, pady=5) 
            self.win.update()
            self.win.deiconify()

    def saveGraphPNG(self):
        dataObj.createReportDir()
        plt.savefig(f"{dataObj.filePath}/reports/{dataObj.code.upper()} ostatnie {self.timeRange.get()}.png", dpi=200)

    def exchangeRatesTabel(self):
        tabControl = ttk.Notebook(self.win) 
        tab1 = ttk.Frame(tabControl) 
        tabControl.add(tab1, text="Średnie") 
        tab2 = ttk.Frame(tabControl) 
        tabControl.add(tab2, text="kupno/sprzedaż")
        tabControl.grid(column=0, columnspan=3, rowspan=10, row=0, padx=4, pady=4)
        
        echangeRateFrame = ttk.LabelFrame(tab1, text= f"Średnie kursy walut {dataObj.effectiveDateList[-1]}", labelanchor="n", style='clam.TLabelframe')  
        echangeRateFrame.grid(column=1, row=0, columnspan=3, rowspan=(len(dataObj.rates)+1), padx=5, sticky=tk.W)
        
        ttk.Label(echangeRateFrame, text= "Waluta").grid(column=0, row=0, sticky=tk.W, padx=5)
        ttk.Label(echangeRateFrame, text= "Kod").grid(column=1, row=0, sticky=tk.W, padx=5)
        ttk.Label(echangeRateFrame, text= "Kurs PLN").grid(column=2, row=0, sticky=tk.W, padx=2)
        ttk.Label(echangeRateFrame, text= "Zmiana").grid(column=3, row=0, sticky=tk.W, padx=2)
        
        for t in range(len(dataObj.rates)):
            ttk.Label(echangeRateFrame,  width=30, text= f'{dataObj.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
            ttk.Label(echangeRateFrame,  width=5, text= f'{dataObj.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=3, pady=3)
            ttk.Label(echangeRateFrame,  width=9, text= f'{dataObj.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=3, pady=3)
            if float(dataObj.ratesUpDown[t+33][3])>float(dataObj.ratesUpDown[t][3]):
                col = "Green"
            elif float(dataObj.ratesUpDown[t+33][3])<float(dataObj.ratesUpDown[t][3]):
                col = "Red"
            else:
                col = "White"
            procent = round((((float(dataObj.ratesUpDown[t+33][3])/float(dataObj.ratesUpDown[t][3])) -1) * 100), 2)
            ttk.Label(echangeRateFrame,  width=6, text= f'{procent}%', foreground=col).grid(column=3, row=t+1, sticky=tk.W, padx=3, pady=3)
        
        del dataObj.ratesUpDown
        
    def graphGui(self): 
        tabControlGui = ttk.Notebook(self.win) 
        tab1 = ttk.Frame(tabControlGui) 
        tabControlGui.add(tab1, text="Wykres")
        tab2 = ttk.Frame(tabControlGui)
        tabControlGui.add(tab2, text="Wiele wykresów")
        tabControlGui.grid(column=4, columnspan=3, rowspan=3,row=0, padx=4, pady=4)

        plotGraphFrame = ttk.LabelFrame(tab1, text= "Rysowanie wykresu", labelanchor="n")  
        plotGraphFrame.grid(column=4, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.E)
        ttk.Label(plotGraphFrame, text= "Waluta ").grid(column=4, row=1, sticky=tk.W, pady=5,padx=5) 
        ttk.Label(plotGraphFrame, text= "Przedział czasowy ").grid(column=4, row=2, sticky=tk.W, pady=5, padx=5)
            
        self.currencyName = tk.StringVar()
        codeCurrencyList = []
        for key,values in dataObj.codeCurrencyDict.items():
            codeCurrencyList.append(f"{key}  {values}")
        currencyChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.currencyName, state= "readonly")
        currencyChosen["values"] = codeCurrencyList 
        currencyChosen.grid(column= 5, row= 1, padx=5,pady=5)
        currencyChosen.current(7)
    
        self.timeRange = tk.StringVar() 
        rangeChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.timeRange, state= "readonly")
        rangeChosen["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat") 
        rangeChosen.grid(column= 5, row= 2, padx=5, pady=5)
        rangeChosen.current(0)
        ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = self.newGraph, width=12).grid(column = 6, row = 1, padx=5)  
        ttk.Button(plotGraphFrame, text = "Zapisz wykres", command = self.saveGraphPNG, width=12).grid(column = 6, row = 2, padx=5) 
        
    def generateReportGui(self): 
        def runReport():
            dataObj.generateReport(self.startDate.get(), self.endDate.get()) 
        
        tabControlRep = ttk.Notebook(self.win) 
        tab1 = ttk.Frame(tabControlRep) 
        tabControlRep.add(tab1, text="Raporty")
        tab2 = ttk.Frame(tabControlRep)
        tabControlRep.add(tab2, text="Inne")
        tabControlRep.grid(column=7, columnspan=3, rowspan=3,row=0, padx=4, pady=4)

        reportFrame = ttk.LabelFrame(tab1, text= "Generuj raport", labelanchor="n")
        reportFrame.grid(column=7, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.W)
        ttk.Label(reportFrame, text= "data początkowa (RRRR-MM-DD): ").grid(column=7, row=1, sticky=tk.W, pady=5, padx=5) 
        ttk.Label(reportFrame, text= "data końcowa (RRRR-MM-DD):").grid(column=7, row=2, sticky=tk.W, pady=5, padx=5)
            
        self.startDate = tk.StringVar() 
        ttk.Entry(reportFrame, width= 10, textvariable= self.startDate).grid(column= 8, row= 1, padx=5, pady=5)
        
        self.endDate = tk.StringVar()
        endDateBox = ttk.Entry(reportFrame, width= 10,  textvariable= self.endDate)
        endDateBox.grid(column= 8, row= 2, padx=5, pady=5)
        endDateBox.insert(tk.END, dataObj.effectiveDateList[-1])
        ttk.Button(reportFrame, text = "Generuj raport", command = runReport, width=12).grid(column = 9, row = 0 , rowspan=3, padx=5)  

dataObj = Data()
mainObj = Main() 
mainObj.win.mainloop()      
    


    
    





   


    


