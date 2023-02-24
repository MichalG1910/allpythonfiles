import os, math
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
import PIL
import PIL._tkinter_finder
from classE_Rates07 import Data

class Main:
    def __init__(self):
        self.win = tk.Tk()
        dataObj.checkConnection()
        dataObj.createReportDir()
        dataObj.NBPbidAsk()
        dataObj.NBPratesUpDown()
        dataObj.latestNBPreport()
        self.winStyle(self.win)
        self.themeButton()
        self.emptyGraph()
        self.exchangeRatesTabel()
        self.graphGui()
        self.generateReportGui()
        
    
    def winStyle(self, window):
        window.tk.call('source', os.path.join(dataObj.filePath, 'azure.tcl'))
        window.tk.call("set_theme", "dark")

    def themeButton(self):
        def change_theme():
            if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
                self.win.tk.call("set_theme", "light")
                icon1 = PhotoImage(file=f'{dataObj.filePath}/light.png')
                self.accentbutton.configure(image=icon1)
                self.accentbutton.image = icon1
                self.refreshGraph(self.win, 4, [11,8], 111)
                
            else:
                self.win.tk.call("set_theme", "dark")
                icon2 = PhotoImage(file=f'{dataObj.filePath}/dark.png')
                self.accentbutton.configure(image=icon2 )
                self.accentbutton.image = icon2
                self.refreshGraph(self.win, 4, [11,8], 111)
                
        icon = PhotoImage(file=f'{dataObj.filePath}/dark.png')
        self.accentbutton = ttk.Button(self.win, image=icon, command=change_theme)
        self.accentbutton.image = icon
        self.accentbutton.grid(row=0, column=11, padx=5, pady=5, sticky="nsew")
    
    def emptyGraph(self):
        if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            fig = plt.figure(figsize=(11,8), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
            fig = plt.figure(figsize=(11,8), facecolor = "lightcyan")
        
        axis = fig.add_subplot(111) 
        axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
        axis.set_xlabel("Data") 
        axis.set_ylabel("PLN Złoty")
        canvas = FigureCanvasTkAgg(fig, master=self.win) 
        canvas._tkcanvas.grid(column=4, row=3, columnspan=8, padx=10, pady=10) 
        self.win.update()
        self.win.deiconify()

    def newGraph(self):
        dataObj.checkConnection()
        dataObj.getDataForGraph(self.currencyName.get(), self.timeRange.get())
        self.refreshGraph(self.win, 4, [11,8], 111)

    def refreshGraph(self, window, col, fsize, subp):
        try:
            dataObj.xValues 
        except AttributeError:
            dataObj.xValues = None
            
        if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            self.fig = plt.figure(figsize=(fsize[0],fsize[1]), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
            self.fig = plt.figure(figsize=(11,8), facecolor = "lightcyan")
        
        if dataObj.xValues == None:
            self.emptyGraph()
        else:
            self.axis = self.fig.add_subplot(subp)
            self.axisCreate()
            self.putGraph(window, col, self.fig)
            
            
    def axisCreate(self):
        xValuesLen = len(dataObj.xValues)-1
        a = math.ceil(xValuesLen / 20)
        b = list(range(1,xValuesLen, a))
        b.append(xValuesLen)
         
        self.axis.set_title(f"{dataObj.code.upper()} {dataObj.codeCurrencyDict[dataObj.code.upper()]}", fontsize=16, color="silver")
        self.axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
        self.axis.plot(dataObj.xValues, dataObj.yValues) 
        xaxis = self.axis.get_xaxis()
        xaxis.set_ticks(b)
        plt.xticks(rotation=45, fontsize=8)
        self.axis.set_xlabel("Data") 
        self.axis.set_ylabel("PLN Złoty")
    
    def putGraph(self, window, col, fig):
        canvas = FigureCanvasTkAgg(fig, master=window) 
        canvas._tkcanvas.grid(column=col, row=3, columnspan=8, padx=5, pady=5) 
        window.update()
        window.deiconify()

    def saveGraphPNG(self):
        dataObj.createReportDir()
        plt.savefig(f"{dataObj.filePath}/reports/{dataObj.code.upper()} ostatnie {self.timeRange.get()}.png", dpi=200)
    
    def multiGraphList(self):
        listTR, listChVar, self.multiGraphDict = [], [], {}
        agr = -1

        for a in range(len(dataObj.rates)):
            listTR.append(globals()['timeRange{}'.format(a)].get())
            listChVar.append(globals()['chVar{}'.format(a)].get())
        for b in listTR:
            agr += 1
            if b != "" and listChVar[agr] == 1:
                self.multiGraphDict[self.codeCurrencyList[agr]] = listTR[agr]
                

        print(self.multiGraphDict)
        print(len(self.multiGraphDict))
        print(listTR)
        print(listChVar)
        print(self.codeCurrencyList)

        

    def exchangeRatesTabel(self):
        
        def mediumTab(): 
            tab1 = ttk.Frame(tabControl)
            iconSrednie = PhotoImage(file=f'{dataObj.filePath}/kursy.png')
            
            tabControl.add(tab1,  image=iconSrednie, compound='left')  
            tabControl.image = iconSrednie
            tabControl.grid(column=0, columnspan=4, rowspan=34, row=0, padx=4, pady=4)
            echangeRateFrame = ttk.LabelFrame(tab1, text= f"Średnie kursy walut {dataObj.effectiveDateList[-1]}", labelanchor="n", style='clam.TLabelframe')  
            echangeRateFrame.grid(column=1, row=0, columnspan=4, rowspan=(len(dataObj.rates)+1), padx=5, sticky=tk.W)
            
            ttk.Label(echangeRateFrame, text= "Waluta", foreground="#007fff").grid(column=0, row=0, sticky=tk.W, padx=5)
            ttk.Label(echangeRateFrame, text= "Kod", foreground="#007fff").grid(column=1, row=0, sticky=tk.W, padx=5)
            ttk.Label(echangeRateFrame, text= "Kurs PLN", foreground="#007fff").grid(column=2, row=0, sticky=tk.W, padx=2)
            ttk.Label(echangeRateFrame, text= "Zmiana", foreground="#007fff").grid(column=3, row=0, sticky=tk.W, padx=2)
            
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
        
        def bidAskTab():
            tab2 = ttk.Frame(tabControl)
            tabControl.add(tab2, text="kupno/sprzedaż")
            buySellFrame = ttk.LabelFrame(tab2, text= f"Kupno / Sprzedaż {dataObj.effectiveDateList[-1]}", labelanchor="n", style='clam.TLabelframe')  
            buySellFrame.grid(column=1, row=0, columnspan=4, rowspan=(len(dataObj.rates1)+1), padx=5, sticky=tk.W)
            
            ttk.Label(buySellFrame, text= "Waluta", foreground="#007fff").grid(column=0, row=0, sticky=tk.W, padx=5)
            ttk.Label(buySellFrame, text= "Kod", foreground="#007fff").grid(column=1, row=0, sticky=tk.W, padx=5)
            ttk.Label(buySellFrame, text= "Kupno", foreground="#007fff").grid(column=2, row=0, sticky=tk.W, padx=2)
            ttk.Label(buySellFrame, text= "Sprzedaż", foreground="#007fff").grid(column=3, row=0, sticky=tk.W, padx=2)
            ttk.Label(tab2, text= f"\nTabela {dataObj.no1} zawiera tylko wybrane waluty").grid(columnspan=4, row=len(dataObj.rates1)+2, sticky=tk.W, padx=3, pady=3)
            
            for v in range(len(dataObj.rates1)):
                ttk.Label(buySellFrame,  width=28, text= f'{dataObj.currencyList1[v]}').grid(column=0, row=v+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(buySellFrame,  width=5, text= f'{dataObj.codeList1[v]}').grid(column=1, row=v+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(buySellFrame,  width=9, text= f'{dataObj.valueList1[v]}').grid(column=2, row=v+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(buySellFrame,  width=8, text= f'{dataObj.askList1[v]}').grid(column=3, row=v+1, sticky=tk.W, padx=3, pady=3)
        
        def currencyLast30():
            currencyLast30 = tk.StringVar()
            self.codeCurrencyList = []

            def getLast30Tabel():
                dataObj.last30Data(currencyLast30.get())
                for i in range(30):
                    ttk.Label(last30Frame,  width=10, text= f'{dataObj.last30EDList[i]}').grid(column=0, row=i+2, sticky=tk.W, padx=3, pady=3)
                    ttk.Label(last30Frame,  width=10, text= f'{dataObj.last30MidList[i]}').grid(column=1, row=i+2, sticky=tk.W, padx=3, pady=3)
                
                for m in range(29):
                    if float(dataObj.last30MidList[m])>float(dataObj.last30MidList[m+1]): 
                        col = "Green"
                    elif float(dataObj.last30MidList[m])<float(dataObj.last30MidList[m+1]):
                        col = "Red"
                    else:
                        col = "White" 
                    procent = round((((float(dataObj.last30MidList[m])/float(dataObj.last30MidList[m+1])) -1) * 100), 2)
                    ttk.Label(last30Frame,  width=6, text= f'{procent}%', foreground=col).grid(column=2, row=m+2, sticky=tk.W, padx=3, pady=3)
                
                if float(dataObj.last30MidList[0])>float(dataObj.last30MidList[-1]):
                    col1 = "Green"
                elif float(dataObj.last30MidList[0])<float(dataObj.last30MidList[-1]):
                    col1 = "Red"
                else:
                    col1 = "White" 
                procent = round((((float(dataObj.last30MidList[0])/float(dataObj.last30MidList[-1])) -1) * 100), 2)
                ttk.Label(last30Frame,  width=6, text= f'{procent}%', foreground=col1).grid(column=3, row=2, sticky=tk.W, padx=3, pady=3)   
            
            tab3 = ttk.Frame(tabControl)
            tabControl.add(tab3, text="Waluta ostatnie 30")
            last30Frame = ttk.LabelFrame(tab3, text="Waluta ostatnie 30 notowań", labelanchor="n", style='clam.TLabelframe')  
            last30Frame.grid(column=1, row=0, columnspan=4, rowspan=30, padx=5, sticky=tk.W)
            
            for key,values in dataObj.codeCurrencyDict.items():
                self.codeCurrencyList.append(f"{key}  {values}")
            currencyChosen = ttk.Combobox(last30Frame, width= 40, textvariable= currencyLast30, state= "readonly")
            currencyChosen["values"] = self.codeCurrencyList 
            currencyChosen.grid(column= 0, columnspan=3, row= 0, padx=5,pady=5)
            currencyChosen.current(7)
            
            ttk.Button(last30Frame, text = "Pokaż", command = getLast30Tabel, width=8).grid(column = 3, row = 0, padx=5, sticky=tk.E)
            ttk.Label(last30Frame, text= "Data", foreground="#007fff").grid(column=0, row=1, sticky=tk.W, padx=5)
            ttk.Label(last30Frame, text= "Kurs PLN", foreground="#007fff").grid(column=1, row=1, sticky=tk.W, padx=2)
            ttk.Label(last30Frame, text= "Zmiana", foreground="#007fff").grid(column=2, row=1, sticky=tk.W, padx=2)
            ttk.Label(last30Frame, text= "Zmiana 30\n notowań", foreground="#007fff").grid(column=3, row=1, sticky=tk.W, padx=2)
        
        def multiGraph():
            self.tR1 = {}
            rangeChosen = []
            self.checkChosen = []
            ratesHalf = math.floor(len(dataObj.rates) / 2)
            print(ratesHalf)

            tab4 = ttk.Frame(tabControl)
            tabControl.add(tab4, text="wiele wykr.")
            self.multiGraphFrame = ttk.LabelFrame(tab4, text="Rysowanie wielu wykresów", labelanchor="n", style='clam.TLabelframe')  
            self.multiGraphFrame.grid(column=0, row=0, columnspan=6, rowspan=30, padx=5, sticky=tk.W)

            for t in range(len(dataObj.rates)):
                aaa = tk.StringVar()
                if t <= ratesHalf: ttk.Label(self.multiGraphFrame,  width=17, text= f'{dataObj.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
                else: ttk.Label(self.multiGraphFrame,  width=18, text= f'{dataObj.currencyList[t]}').grid(column=3, row=t-ratesHalf, sticky=tk.W, padx=3, pady=3)
                
                globals()['timeRange{}'.format(t)] = tk.StringVar()
                globals()['rangeChosen{}'.format(t)]= ttk.Combobox(self.multiGraphFrame, width= 8, textvariable= globals()['timeRange{}'.format(t)], state= "readonly",height=10)
                globals()['rangeChosen{}'.format(t)]["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat") 
                #globals()['rangeChosen{}'.format(t)].current(0)
                if t <= ratesHalf: globals()['rangeChosen{}'.format(t)].grid(column= 1, row= t+1, padx=5, pady=5)
                else: globals()['rangeChosen{}'.format(t)].grid(column= 4, row=t-ratesHalf, padx=5, pady=5)
                
                globals()['chVar{}'.format(t)] = tk.IntVar() 
                globals()['checkChosen{}'.format(t)] = ttk.Checkbutton(self.multiGraphFrame, variable=globals()['chVar{}'.format(t)] ) # state= "disabled"
                if t <= ratesHalf: globals()['checkChosen{}'.format(t)].grid(column=2, row=t+1, sticky=tk.W)
                else: globals()['checkChosen{}'.format(t)].grid(column=5, row=t-ratesHalf, sticky=tk.W)
                

        tabControl = ttk.Notebook(self.win)
        mediumTab()
        bidAskTab()
        currencyLast30()
        multiGraph()
        del dataObj.ratesUpDown

    def graphGui(self): 
        self.currencyName = tk.StringVar()
        self.timeRange = tk.StringVar() 

        tabControlGui = ttk.Notebook(self.win) 
        tab1, tab2 = ttk.Frame(tabControlGui), ttk.Frame(tabControlGui) 
        tabControlGui.add(tab1, text="Wykres")
        tabControlGui.add(tab2, text="Wiele wykresów")
        tabControlGui.grid(column=4, columnspan=3, rowspan=3,row=0, padx=4, pady=4)

        plotGraphFrame = ttk.LabelFrame(tab1, text= "Rysowanie wykresu", labelanchor="n")  
        plotGraphFrame.grid(column=4, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.E)
        ttk.Label(plotGraphFrame, text= "Waluta ").grid(column=4, row=1, sticky=tk.W, pady=5,padx=5) 
        ttk.Label(plotGraphFrame, text= "Przedział czasowy ").grid(column=4, row=2, sticky=tk.W, pady=5, padx=5)
            
        currencyChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.currencyName, state= "readonly")
        currencyChosen["values"] = self.codeCurrencyList 
        currencyChosen.grid(column= 5, row= 1, padx=5,pady=5)
        currencyChosen.current(7)
    
        rangeChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.timeRange, state= "readonly")
        rangeChosen["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat") 
        rangeChosen.grid(column= 5, row= 2, padx=5, pady=5)
        rangeChosen.current(0)
        ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = self.newGraph, width=12).grid(column = 6, row = 1, padx=5)  
        ttk.Button(plotGraphFrame, text = "Zapisz wykres", command = self.saveGraphPNG, width=12).grid(column = 6, row = 2, padx=5)

        # test button
        ttk.Button(tab2, text = "wez dane", command = self.fullscreenGraphWindow, width=12).grid(column = 6, row = 1, padx=5)  
        # test checkbox
        testV = tk.IntVar() 
        testch = ttk.Checkbutton(tab2, variable=testV ).grid(column=3, row=2, sticky=tk.W) 
        # test radiobutton
        self.radVar = tk.IntVar()
        #self.radVar.set(99)
        curRad = ttk.Radiobutton(tab2, variable=self.radVar) # command=self.radCall
        curRad.grid(column=2, row=2, sticky=tk.W)


        
    def generateReportGui(self):
        self.startDate = tk.StringVar()
        self.endDate = tk.StringVar()

        def runReport():
            dataObj.generateReport(self.startDate.get(), self.endDate.get()) 
        
        tabControlRep = ttk.Notebook(self.win) 
        tab1, tab2 = ttk.Frame(tabControlRep),  ttk.Frame(tabControlRep) 
        tabControlRep.add(tab1, text="Raporty")
        tabControlRep.add(tab2, text="Inne")
        tabControlRep.grid(column=7, columnspan=3, rowspan=3,row=0, padx=4, pady=4)

        reportFrame = ttk.LabelFrame(tab1, text= "Generuj raport", labelanchor="n")
        reportFrame.grid(column=7, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.W)
        ttk.Label(reportFrame, text= "data początkowa (RRRR-MM-DD): ").grid(column=7, row=1, sticky=tk.W, pady=5, padx=5) 
        ttk.Label(reportFrame, text= "data końcowa (RRRR-MM-DD):").grid(column=7, row=2, sticky=tk.W, pady=5, padx=5)
        ttk.Entry(reportFrame, width= 10, textvariable= self.startDate).grid(column= 8, row= 1, padx=5, pady=5)
        
        endDateBox = ttk.Entry(reportFrame, width= 10,  textvariable= self.endDate)
        endDateBox.grid(column= 8, row= 2, padx=5, pady=5)
        endDateBox.insert(tk.END, dataObj.effectiveDateList[-1])
        ttk.Button(reportFrame, text = "Generuj raport", command = runReport, width=12).grid(column = 9, row = 0 , rowspan=3, padx=5)  

    def fullscreenGraphWindow(self):
        def _quit():
            winFull.quit()
            winFull.destroy()

        winFull = tk.Tk()
        self.winStyle(winFull)
        winFull.attributes("-fullscreen", True)
        agr = 0
        
        dataObj.checkConnection()
        self.multiGraphList()
        listTrSum = len(self.multiGraphDict)
        
        if winFull.tk.call("ttk::style", "theme", "use") == "azure-dark":
            plt.style.use('dark_background')
            figFS = plt.figure(figsize=(19,10), facecolor = "dimgray")
        else:
            plt.style.use('Solarize_Light2')
            figFS = plt.figure(figsize=(19,10), facecolor = "lightcyan")
       
        for key,value in self.multiGraphDict.items():
            if listTrSum == 1: self.axis = figFS.add_subplot(111) 
            if listTrSum == 2: self.axis = figFS.add_subplot(121 + agr) 
            if listTrSum == 3: self.axis = figFS.add_subplot(221 + agr) 
            if listTrSum == 4: self.axis = figFS.add_subplot(221 + agr)  
            if listTrSum == 5: self.axis = figFS.add_subplot(231 + agr)  
            if listTrSum == 6: self.axis = figFS.add_subplot(231 + agr)  
            if listTrSum == 7: self.axis = figFS.add_subplot(241 + agr)  
            if listTrSum == 8: self.axis = figFS.add_subplot(241 + agr) 
            if listTrSum == 9: self.axis = figFS.add_subplot(331 + agr)  
            if listTrSum == 10: self.axis = figFS.add_subplot(3,4,1 + agr)  
            if listTrSum == 11: self.axis = figFS.add_subplot(3,4,1 + agr)  
            if listTrSum == 12: self.axis = figFS.add_subplot(3,4,1 + agr) 
            
            dataObj.getDataForGraph(key, value)
            figFS.tight_layout() # wykresy nie nachodzą na siebie
            self.axisCreate()
            agr += 1
        
        self.putGraph(winFull, 0, figFS)
        ttk.Button(winFull, text = "Zamknij okno", command = _quit, width=12).grid(column = 0, row = 0 , padx=5, pady=5, sticky=tk.W)

        winFull.mainloop()



dataObj = Data()
mainObj = Main() 
mainObj.win.mainloop()      
    


    
    





   


    


