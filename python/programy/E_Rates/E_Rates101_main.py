import os, math, time, sys, subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import PIL
import PIL._tkinter_finder
from classE_Rates101_Data import Data
from classE_Rates101_Graph import Graph
from classE_Rates101_Tooltip import ToolTip
import gc
from tkinter import messagebox as mBox
from tkinter import Menu
class Main:
    agr_number = 0
    
    def __init__(self):
        self.win = tk.Tk()
        dataObj.checkConnection()
        dataObj.createReportDir()
        dataObj.NBPbidAsk()
        dataObj.NBPratesUpDown()
        dataObj.latestNBPreport()
        self.winStyle(self.win)
        self.themeButton(self.win)
        self.quitButton()
        graphObj.emptyGraph(self.win)
        self.exchangeRatesTabel()
        self.graphGui()
        self.generateReportGui()
        self.win.protocol("WM_DELETE_WINDOW", self._exit)
        self.win.title("E_Rates v.1.1".center(int(self.win.winfo_width()/1.7)))
        self.menu()
        
    def menu(self):
        self.menuBar = Menu(self.win)
        self.win.config(menu=self.menuBar)
        
        fileMenu = Menu(self.menuBar, tearoff=0)
        fileMenu.add_command(label="Pliki", command=self.openFileDir)
        fileMenu.add_command(label="Info", command=self.info)
        fileMenu.add_command(label="Restart", command=self._restart)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._exit)
        
        self.menuBar.add_cascade(label="File", menu=fileMenu)
        self.menuBar.add_command(command=self.change_theme,image=self.icon)
        self.menuBar.add_command(label = "__", command = self._minimalize)
        self.menuBar.add_command(label = "x", command = self._exit)
        self.menuBar.image = self.icon
    
    def openFileDir(self):
        def openPlatform():
            if sys.platform == 'linux': subprocess.Popen(['xdg-open', f"{dataObj.filePath}/reports"])
            else: os.startfile(f"{dataObj.filePath}/reports")
        
        if os.path.exists(f"{dataObj.filePath}/reports"):
            openPlatform()
        else:
            os.mkdir(os.path.join(dataObj.filePath, "reports")) 
            openPlatform()
        
    def info(self):
        infoWin = tk.Tk()
        infoWin.geometry("335x180+800+400")
        self.winStyle(infoWin)
        ttk.Label(infoWin, text='E_Rates v1.01\napril 2022\nMichał Grabarz').grid(column=0, row=0, padx=55, pady=10)
        ttk.Label(infoWin, text='-ta aplikacja została napisana w celu nauki jezyka Python\n-this app was written to learn python', font=("Segoe Ui",8,), foreground='grey').grid(column=0, row=1, padx=20, pady=10)
        ttk.Button(infoWin, text="Zamknij", command=infoWin.destroy).grid(column=0, row=2, padx=55)

    def _restart(self):
        self.win.quit()
        self.win.destroy()
        if sys.platform == 'linux': os.execl(sys.executable, sys.executable, *sys.argv)
        else: subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')   
    
    def _exit(self):
        self.win.quit()
        self.win.destroy()

    def _minimalize(self):
        self.win.iconify()
    
    def gcCollect(self):
        gc.collect()
    
    def createToolTip(self, widget, text, corX=0, corY=0): 
        toolTip = ToolTip(widget)
        def enter(event):
            toolTip.showtip(text, corX, corY)
        def leave(event): 
            toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)
    
    def quitButton(self):
        boldStyle = ttk.Style()
        boldStyle.configure ("Bold.TButton", weight = "bold", foreground='black', font=20)
        quitB = ttk.Button(self.win,text="X", command=self._exit, width=2, style = "Bold.TButton")
        quitB.grid(row=0, column=13, ipadx=9.4, pady=5, columnspan=3, sticky=tk.E)
        self.createToolTip(quitB, "Zamknij", -50, 20)

    def winStyle(self, window):
        window.tk.call('source', os.path.join(dataObj.filePath, 'azure.tcl'))
        window.tk.call("set_theme", "dark")
        #window.attributes("-fullscreen", True) # okno otwiera się na pełnym ekranie
    
    def themeButton(self, window):            
        self.icon = PhotoImage(file=f'{dataObj.filePath}/light4.png')
        self.accentbutton = ttk.Button(window, image=self.icon, command=self.change_theme, width=2)
        self.accentbutton.image = self.icon
        self.accentbutton.grid(row=0, column=13,columnspan=2, ipadx=9.4, pady=5, sticky=tk.W)
        self.createToolTip(self.accentbutton, "motyw jasny/ciemny", -125, 20)
    
    def change_theme(self):
        if self.win.tk.call("ttk::style", "theme", "use") == "azure-dark":
            self.win.tk.call("set_theme", "light")
            self.icon = PhotoImage(file=f'{dataObj.filePath}/dark4.png')
            self.accentbutton.configure(image=self.icon)
            self.menuBar.destroy()
            self.menu()
            self.accentbutton.image = self.icon
            
            try:
                dataObj.xValues 
            except AttributeError:
                dataObj.xValues, dataObj.yValues, dataObj.codeOne = None, None, None
            graphObj.refreshGraph(self.win, self.timeRange.get(), dataObj.xValues, dataObj.yValues, dataObj.codeOne, dataObj.codeCurrencyDict)
            
        else:
            self.win.tk.call("set_theme", "dark")
            self.icon = PhotoImage(file=f'{dataObj.filePath}/light4.png')
            self.accentbutton.configure(image=self.icon)
            self.menuBar.destroy()
            self.menu()
            self.accentbutton.image = self.icon
            
            try:
                dataObj.xValues 
            except AttributeError:
                dataObj.xValues, dataObj.yValues, dataObj.codeOne = None, None, None
            graphObj.refreshGraph(self.win, self.timeRange.get(), dataObj.xValues, dataObj.yValues, dataObj.codeOne, dataObj.codeCurrencyDict)

    def exchangeRatesTabel(self):
        def mediumTab(): 
            tab1 = ttk.Frame(tabControl)
            
            tabControl.add(tab1,  text="Kursy", compound='left')  
            tabControl.grid(column=0, columnspan=4, rowspan=34, row=1, padx=4, pady=4, sticky=tk.N)
            echangeRateFrame = ttk.LabelFrame(tab1, text= f"Średnie kursy walut {dataObj.effectiveDateList[-1]}", labelanchor="n", style='clam.TLabelframe')  
            echangeRateFrame.grid(column=1, row=0, columnspan=4, rowspan=(len(dataObj.rates)+1), padx=5, sticky=tk.W)
            
            ttk.Label(echangeRateFrame, text= "Waluta", foreground="#007fff").grid(column=0, row=0, sticky=tk.W, padx=5)
            ttk.Label(echangeRateFrame, text= "Kod", foreground="#007fff").grid(column=1, row=0, sticky=tk.W, padx=5)
            ttk.Label(echangeRateFrame, text= "Kurs PLN", foreground="#007fff").grid(column=2, row=0, sticky=tk.W, padx=2)
            ttk.Label(echangeRateFrame, text= "Zmiana", foreground="#007fff").grid(column=3, row=0, sticky=tk.W, padx=2)
            
            for t in range(len(dataObj.rates)):
                ttk.Label(echangeRateFrame,  width=20, text= f'{dataObj.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=1, pady=1)
                ttk.Label(echangeRateFrame,  width=5, text= f'{dataObj.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=1, pady=1)
                ttk.Label(echangeRateFrame,  width=10, text= f'{dataObj.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=1, pady=1)
                if float(dataObj.ratesUpDown[t+33][3])>float(dataObj.ratesUpDown[t][3]):
                    col = "Green"
                elif float(dataObj.ratesUpDown[t+33][3])<float(dataObj.ratesUpDown[t][3]):
                    col = "Red"
                else:
                    col = "White"
                procent = round((((float(dataObj.ratesUpDown[t+33][3])/float(dataObj.ratesUpDown[t][3])) -1) * 100), 2)
                if procent > 0:
                    ttk.Label(echangeRateFrame,  width=8, text= f'\u25B2 {procent}%', foreground=col).grid(column=3, row=t+1, sticky=tk.W, padx=1, pady=1)
                elif procent == 0:
                    ttk.Label(echangeRateFrame,  width=8, text= f'    {procent}%', foreground=col).grid(column=3, row=t+1, sticky=tk.W, padx=1, pady=1)
                else: 
                    ttk.Label(echangeRateFrame,  width=8, text= f'\u25BC {abs(procent)}%', foreground=col).grid(column=3, row=t+1, sticky=tk.W, padx=1, pady=1)
        
        def bidAskTab():
            tab2 = ttk.Frame(tabControl)
            tabControl.add(tab2, text="kupno/sprzedaż")
            buySellFrame = ttk.LabelFrame(tab2, text= f"Kupno / Sprzedaż {dataObj.effectiveDateList[-1]}", labelanchor="n", style='clam.TLabelframe')  
            buySellFrame.grid(column=1, row=1, columnspan=4, rowspan=(len(dataObj.rates1)+1), padx=5, sticky=tk.W)
            
            ttk.Label(buySellFrame, text= "Waluta", foreground="#007fff").grid(column=0, row=0, sticky=tk.W, padx=5)
            ttk.Label(buySellFrame, text= "Kod", foreground="#007fff").grid(column=1, row=0, sticky=tk.W, padx=5)
            ttk.Label(buySellFrame, text= "Kupno", foreground="#007fff").grid(column=2, row=0, sticky=tk.W, padx=2)
            ttk.Label(buySellFrame, text= "Sprzedaż", foreground="#007fff").grid(column=3, row=0, sticky=tk.W, padx=2)
            ttk.Label(tab2, text= f"\nTabela {dataObj.no1} zawiera tylko wybrane waluty").grid(columnspan=4, row=len(dataObj.rates1)+2, sticky=tk.W, padx=3, pady=3)
            
            for v in range(len(dataObj.rates1)):
                ttk.Label(buySellFrame,  width=20, text= f'{dataObj.currencyList1[v]}').grid(column=0, row=v+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(buySellFrame,  width=5, text= f'{dataObj.codeList1[v]}').grid(column=1, row=v+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(buySellFrame,  width=9, text= f'{dataObj.valueList1[v]}').grid(column=2, row=v+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(buySellFrame,  width=8, text= f'{dataObj.askList1[v]}').grid(column=3, row=v+1, sticky=tk.W, padx=3, pady=3)
        
        def currencyLast30():
            currencyLast30 = tk.StringVar()
            self.codeCurrencyList = []

            def getLast30Tabel():
                dataObj.last30Data(currencyLast30.get())
                for i in range(30):
                    ttk.Label(last30Frame,  width=10, text= f'{dataObj.last30EDList[i]}').grid(column=0, row=i+2, sticky=tk.W, padx=1, pady=1)
                    ttk.Label(last30Frame,  width=10, text= f'{dataObj.last30MidList[i]}').grid(column=1, row=i+2, sticky=tk.W, padx=1, pady=1)
                #rise fall
                for m in range(29):
                    if float(dataObj.last30MidList[m])>float(dataObj.last30MidList[m+1]): 
                        col = "Green"
                    elif float(dataObj.last30MidList[m])<float(dataObj.last30MidList[m+1]):
                        col = "Red"
                    else:
                        col = "White" 
                    procent = round((((float(dataObj.last30MidList[m])/float(dataObj.last30MidList[m+1])) -1) * 100), 2)
                    if procent > 0:
                        ttk.Label(last30Frame,  width=8, text= f'\u25B2 {procent}%', foreground=col).grid(column=2, row=m+2, sticky=tk.W, padx=1, pady=1)
                    elif procent == 0:
                        ttk.Label(last30Frame,  width=8, text= f'    {procent}%', foreground=col).grid(column=2, row=m+2, sticky=tk.W, padx=1, pady=1)
                    else:
                        ttk.Label(last30Frame,  width=8, text= f'\u25BC {abs(procent)}%', foreground=col).grid(column=2, row=m+2, sticky=tk.W, padx=1, pady=1)
                #rise fall 30
                if float(dataObj.last30MidList[0])>float(dataObj.last30MidList[-1]):
                    col1 = "Green"
                elif float(dataObj.last30MidList[0])<float(dataObj.last30MidList[-1]):
                    col1 = "Red"
                else:
                    col1 = "White" 
                procent = round((((float(dataObj.last30MidList[0])/float(dataObj.last30MidList[-1])) -1) * 100), 2)
                if procent > 0:
                    ttk.Label(last30Frame,  width=8, text= f'\u25B2 {procent}%', foreground=col1).grid(column=3, row=2, sticky=tk.W, padx=1, pady=1)
                elif procent == 0:
                    ttk.Label(last30Frame,  width=8, text= f'    {procent}%', foreground=col1).grid(column=3, row=2, sticky=tk.W, padx=1, pady=1)
                else:   
                    ttk.Label(last30Frame,  width=8, text= f'\u25BC {abs(procent)}%', foreground=col1).grid(column=3, row=2, sticky=tk.W, padx=1, pady=1)   
            
            tab3 = ttk.Frame(tabControl)
            tabControl.add(tab3, text="Waluta ostatnie 30")
            last30Frame = ttk.LabelFrame(tab3, text="Waluta ostatnie 30 notowań", labelanchor="n", style='clam.TLabelframe')  
            last30Frame.grid(column=1, row=1, columnspan=4, rowspan=30, padx=5, sticky=tk.W)
            self.createToolTip(last30Frame, "Generuje ostatnich 30 notowań dla wskazanej waluty") 
            
            for key,values in dataObj.codeCurrencyDict.items():
                self.codeCurrencyList.append(f"{key}  {values}")
            currencyChosen = ttk.Combobox(last30Frame, width= 30, textvariable= currencyLast30, state= "readonly")
            currencyChosen["values"] = self.codeCurrencyList 
            currencyChosen.grid(column= 0, columnspan=3, row= 0, padx=5,pady=5)
            currencyChosen.current(7)
            
            ttk.Button(last30Frame, text = "Pokaż", command = getLast30Tabel, width=8).grid(column = 3, row = 0, padx=5, sticky=tk.E)
            ttk.Label(last30Frame, text= "Data", foreground="#007fff").grid(column=0, row=1, sticky=tk.W, padx=5)
            ttk.Label(last30Frame, text= "Kurs PLN", foreground="#007fff").grid(column=1, row=1, sticky=tk.W, padx=2)
            ttk.Label(last30Frame, text= "Zmiana", foreground="#007fff").grid(column=2, row=1, sticky=tk.W, padx=2)
            ttk.Label(last30Frame, text= "Zmiana 30\n notowań", foreground="#007fff").grid(column=3, row=1, sticky=tk.W, padx=2)
            
        def multiGraph():
            ratesHalf = math.floor(len(dataObj.rates) / 2)
            self.timeRangeVariableList, self.chVariableList, self.codeVariableList, self.listchv, trl1, cvl1, code1 = [],[],[],[],[],[],[]
            

            def createView1():
                self.viewNum = 1
                self.timeRangeVariableList.clear()
                self.chVariableList.clear()
                for t in range(len(dataObj.rates)):
                    if t <= ratesHalf: ttk.Label(self.multiGraphFrame,  width=17, text= f'{dataObj.currencyList[t]}', font=("Segoe Ui",8)).grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
                    else: ttk.Label(self.multiGraphFrame,  width=18, text= f'{dataObj.currencyList[t]}', font=("Segoe Ui",8)).grid(column=3, row=t-ratesHalf, sticky=tk.W, padx=3, pady=3)
                    
                    globals()['timeRange{}'.format(t)] = tk.StringVar()
                    globals()['rangeChosen{}'.format(t)]= ttk.Combobox(self.multiGraphFrame, width= 8, textvariable= globals()['timeRange{}'.format(t)], state= "readonly",height=10, font=("Segoe Ui",8))
                    globals()['rangeChosen{}'.format(t)]["values"] = ("", "30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat") 
                    if t <= ratesHalf: globals()['rangeChosen{}'.format(t)].grid(column= 1, row= t+1, padx=2, pady=2)
                    else: globals()['rangeChosen{}'.format(t)].grid(column= 4, row=t-ratesHalf, padx=2, pady=2)
                    
                    globals()['chVar{}'.format(t)] = tk.IntVar() 
                    globals()['checkChosen{}'.format(t)] = ttk.Checkbutton(self.multiGraphFrame, variable=globals()['chVar{}'.format(t)] ) # state= "disabled"
                    if t <= ratesHalf: globals()['checkChosen{}'.format(t)].grid(column=2, row=t+1, sticky=tk.W)
                    else: globals()['checkChosen{}'.format(t)].grid(column=5, row=t-ratesHalf, sticky=tk.W)
                    
                    trl1.append(globals()['timeRange{}'.format(t)]) 
                    cvl1.append(globals()['chVar{}'.format(t)])
                    
                self.timeRangeVariableList += trl1
                self.chVariableList += cvl1
                trl1.clear()
                cvl1.clear()
            
            def createView2():
                self.viewNum = 2
                
                for f in range(15):
                    self.timeRangeVariableList.clear()
                    self.codeVariableList.clear()
                    self.chVariableList.clear()
                    globals()['codeVar{}'.format(f)] = tk.StringVar()
                    globals()['codeChosen{}'.format(f)]= ttk.Combobox(self.multiGraphFrame, width= 25, textvariable= globals()['codeVar{}'.format(f)], state= "readonly",height=10)
                    globals()['codeChosen{}'.format(f)]["values"] = self.codeCurrencyList
                    globals()['codeChosen{}'.format(f)].grid(column= 0, row=f, padx=4, pady=2.5)

                    globals()['timeRange{}'.format(f)] = tk.StringVar()
                    globals()['rangeChosen{}'.format(f)]= ttk.Combobox(self.multiGraphFrame, width= 25, textvariable= globals()['timeRange{}'.format(f)], state= "readonly",height=10,)
                    globals()['rangeChosen{}'.format(f)]["values"] = ("", "30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat") 
                    globals()['rangeChosen{}'.format(f)].grid(column= 1, row=f, padx=4, pady=2.5)
                    
                    globals()['chVar{}'.format(f)] = tk.IntVar() 
                    globals()['checkChosen{}'.format(f)] = ttk.Checkbutton(self.multiGraphFrame, variable=globals()['chVar{}'.format(f)] )
                    globals()['checkChosen{}'.format(f)].grid(column=2, row=f, sticky=tk.W)

                    trl1.append(globals()['timeRange{}'.format(f)]) 
                    code1.append(globals()['codeVar{}'.format(f)])
                    cvl1.append(globals()['chVar{}'.format(f)])

                self.timeRangeVariableList += trl1
                self.codeVariableList += code1
                self.chVariableList += cvl1
                
                trl1.clear()
                code1.clear()
                cvl1.clear()
                
            def changeView():
                if self.oneSubplotVarMulti.get() == 1:
                    self.allRange.current(0)
                    self.oneSubplotMultiGraph.invoke()
                
                for widget in self.multiGraphFrame.winfo_children():
                    widget.destroy()  
                if self.viewNum == 1: 
                    createView2()
                    startClearF()
                    markF()
                else: 
                    createView1()
                    startClearF()
                    markF()
            
            def clearView():
                for widget in self.multiGraphFrame.winfo_children():
                    widget.destroy() 
                if self.viewNum == 1:
                    createView1()
                    startClearF()
                    markF()
                else:
                    createView2()
                    startClearF()
                    markF()
            
            def createTab4():
                self.tab4 = ttk.Frame(tabMultiGraph)
                tabMultiGraph.add(self.tab4, text="wiele wykresów")
                tabMultiGraph.grid(column=10, columnspan=4, rowspan=len(dataObj.rates)+2, row=1, padx=4, pady=4, sticky=tk.N)
                self.multiGraphFrame = ttk.LabelFrame(self.tab4, text="Rysowanie wielu wykresów", labelanchor="n", style='clam.TLabelframe')  
                self.multiGraphFrame.grid(column=0, row=1, columnspan=6, rowspan=30, padx=5, sticky=tk.W)
            
            def startClearF():
                self.startclearFrame = ttk.LabelFrame(self.multiGraphFrame, text="wyczyść/rysuj", labelanchor="n", style='clam.TLabelframe', width=80)  
                self.startclearFrame.grid(column=0, row=len(dataObj.rates)+1, columnspan=6, padx=5, pady=5, sticky=tk.E)
                ttk.Button(self.startclearFrame, text = "wyczyść", command = clearView, width=7).grid(column = 0, row=0, padx=5, pady=5, sticky=tk.W)
                ttk.Button(self.startclearFrame, text = "rysuj", command = self.fullscreenGraphWindow, width=5).grid(column = 1, row=0, padx=5, pady=5, sticky=tk.E)
            
            def markF():
                self.a = 1
                self.b = 1
                def markAll():
                    if self.a % 2 != 0:
                        for t in range(len(self.chVariableList)): 
                            globals()['chVar{}'.format(t)].set(1)
                        
                    if self.a % 2 == 0:
                        for t in range(len(self.chVariableList)): 
                            globals()['chVar{}'.format(t)].set(0)
                    self.a += 1

                def markTimeRange():
                    if self.b % 2 != 0:
                        for u in range(len(self.chVariableList)):
                            if globals()['timeRange{}'.format(u)].get() != "": 
                                globals()['chVar{}'.format(u)].set(1)
                    
                    if self.b % 2 == 0:
                        for u in range(len(self.chVariableList)):
                            if globals()['timeRange{}'.format(u)].get() != "": 
                                globals()['chVar{}'.format(u)].set(0)
                                
                    if [i.get() for i in self.timeRangeVariableList].count("") != len(self.timeRangeVariableList):
                        self.b += 1
                    
                self.markFrame = ttk.LabelFrame(self.multiGraphFrame, text="zaznacz/odznacz", labelanchor="n", style='clam.TLabelframe', width=80)  
                self.markFrame.grid(column=0, row=len(dataObj.rates)+1, columnspan=6, padx=5, pady=5, sticky=tk.W)
                all = ttk.Button(self.markFrame, text = "wszystko", command = markAll, width=8)
                all.grid(column = 0, row=0, padx=5, pady=5, sticky=tk.W)
                withTimeRange = ttk.Button(self.markFrame, text = "z zakresem czasu", command = markTimeRange)
                withTimeRange.grid(column = 1, row=0, padx=5, pady=5, sticky=tk.E)
                self.createToolTip(all, "Zaznacz/odznacz wszystkie pola checkbox", 0, 20)
                self.createToolTip(withTimeRange, "Zaznacz/odznacz pola checkbox\nz wybranym zakresem czasu", 0, 20)
            
            def multiSettingsF():
                def otherOptions(*ignoredArgs):
                    if self.oneSubplotVarMulti.get() == 1:
                        if self.viewNum == 1:
                            for t in range(len(dataObj.rates)): 
                                globals()['rangeChosen{}'.format(t)].current(self.allRange["values"].index(self.allRangeVar.get()))  
                        else:
                            for f in range(15):
                                globals()['rangeChosen{}'.format(f)].current(self.allRange["values"].index(self.allRangeVar.get()))
                                
                        self.allRange.configure(state='enabled')
                        self.allRange.configure(state='readonly')
                        if self.trendLineVarMulti.get() == 1:
                            trendLineCheck.invoke()
                        trendLineCheck.configure(state= "disabled")
                        if self.annotateVarMulti.get() == 1: 
                            annotateCheck.invoke()  
                        annotateCheck.configure(state= "disabled")
                    else:
                        self.allRange.current(0)
                        clearView()
                        self.allRange.configure(state='disabled')
                        trendLineCheck.configure(state= "enabled")
                        annotateCheck.configure(state= "enabled")
                        
                self.trendLineVarMulti = tk.IntVar()
                self.annotateVarMulti = tk.IntVar()
                self.oneSubplotVarMulti = tk.IntVar()
                self.allRangeVar= tk.StringVar()
                
                self.multiSettingsFrame = ttk.LabelFrame(self.tab4, text="Ustawienia wykresów", labelanchor="n", style='clam.TLabelframe')  
                self.multiSettingsFrame.grid(column=0, row=len(dataObj.rates)+2, columnspan=6, padx=5, sticky=tk.E)
                viewButton = ttk.Button(self.multiSettingsFrame, text = "zmień widok", command = changeView)
                viewButton.grid(column = 0, row=0, padx=5, pady=5)
                self.createToolTip(viewButton, "widok 1 - standardowy\nwidok 2 - możliwość rysowania wielu wykresów dla jednej\nwaluty w różnych zakresach czasu (w jednym oknie) ", 0, 20) 
                ttk.Label(self.multiSettingsFrame, text= "linia trendu ").grid(column=0, row=2, sticky=tk.W, pady=5,padx=5)  
                trendLineCheck = ttk.Checkbutton(self.multiSettingsFrame, variable=self.trendLineVarMulti )
                trendLineCheck.grid(column=1, row=2, sticky=tk.W) 
                
                ttk.Label(self.multiSettingsFrame, text= "min/max wartość ").grid(column=0, row=3, sticky=tk.W, pady=5,padx=5)  
                annotateCheck = ttk.Checkbutton(self.multiSettingsFrame, variable=self.annotateVarMulti )
                annotateCheck.grid(column=1, row=3, sticky=tk.W) 
                
                multiLineFrame = ttk.LabelFrame(self.multiSettingsFrame, text= "rysuj na jednym wykresie ", labelanchor="n", style='clam.TLabelframe')
                multiLineFrame.grid(column=2, row=0, sticky=tk.W, pady=5,padx=5)
                self.createToolTip(multiLineFrame, "Narysuj wiele linii walut\nna jednym zbiorczym wykresie", -30, -10)  
                ttk.Label(multiLineFrame, text= "zakres czasu ").grid(column=2,rowspan=3, sticky=tk.W, pady=5,padx=5)  
                self.oneSubplotMultiGraph = ttk.Checkbutton(multiLineFrame, variable=self.oneSubplotVarMulti, command=otherOptions )
                self.oneSubplotMultiGraph.grid(column=4, row=0, sticky=tk.W) 
                self.allRange = ttk.Combobox(multiLineFrame, width=8, textvariable=self.allRangeVar, height=10, state='readonly')
                self.allRange.configure(state="disabled")
                self.allRange["values"]= ("", "30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat")
                self.allRange.grid(column= 3, row=0, padx=5, pady=5)
                self.allRangeVar.trace('w', lambda unused0, unused1, unused2 : otherOptions())
                
            createTab4()
            createView1()
            startClearF()
            markF()
            multiSettingsF()
             
        tabControl = ttk.Notebook(self.win)
        tabMultiGraph = ttk.Notebook(self.win)
        mediumTab()
        bidAskTab()
        currencyLast30()
        multiGraph()
        del dataObj.ratesUpDown
        
    def graphGui(self): 
        self.currencyName = tk.StringVar()
        self.timeRange = tk.StringVar()
        self.trendLineVar = tk.IntVar()
        self.annotateVar = tk.IntVar()

        def runSaveGraphPNG1():
            graphObj.saveGraphPNG(1, dataObj.codeOne, self.timeRange.get())
        
        def newGraph():
            graphObj.getVar(self.trendLineVar.get(), self.annotateVar.get())
            dataObj.checkConnection()
            dataObj.getDataForGraph(self.currencyName.get(), self.timeRange.get(), 1, dataObj.firstloopEDL)
            graphObj.refreshGraph(self.win, self.timeRange.get(), dataObj.xValues, dataObj.yValues, dataObj.codeOne, dataObj.codeCurrencyDict)
            
        tabControlGui = ttk.Notebook(self.win) 
        tab1, tab2 = ttk.Frame(tabControlGui), ttk.Frame(tabControlGui) 
        tabControlGui.add(tab1, text="Wykres")
        tabControlGui.add(tab2, text="Ustawienia")
        tabControlGui.grid(column=4, columnspan=3, rowspan=3,row=1, padx=4, pady=4)

        plotGraphFrame = ttk.LabelFrame(tab1, text= "Rysowanie wykresu", labelanchor="n")  
        plotGraphFrame.grid(column=4, row=1, columnspan=3, rowspan=3, padx=5, sticky=tk.E)
        ttk.Label(plotGraphFrame, text= "Waluta ").grid(column=4, row=1, sticky=tk.W, pady=5,padx=5) 
        ttk.Label(plotGraphFrame, text= "Przedział czasowy ").grid(column=4, row=2, sticky=tk.W, pady=5, padx=5)
            
        currencyChosen = ttk.Combobox(plotGraphFrame, width= 23, textvariable= self.currencyName, state= "readonly")
        currencyChosen["values"] = self.codeCurrencyList 
        currencyChosen.grid(column= 5, row= 1, padx=5,pady=5)
        currencyChosen.current(7)
    
        rangeChosen = ttk.Combobox(plotGraphFrame, width= 23, textvariable= self.timeRange, state= "readonly")
        rangeChosen["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat") 
        rangeChosen.grid(column= 5, row= 2, padx=5, pady=5)
        rangeChosen.current(0)
        ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = newGraph, width=12).grid(column = 6, row = 1, padx=3)  
        ttk.Button(plotGraphFrame, text = "Zapisz wykres", command = runSaveGraphPNG1, width=12).grid(column = 6, row = 2, padx=3)

        # ustawienia wykresów checkbox 
        ttk.Label(tab2, text= "linia trendu ").grid(column=2, row=2, sticky=tk.W, pady=5,padx=5)  
        trendLineCheck = ttk.Checkbutton(tab2, variable=self.trendLineVar ).grid(column=3, row=2, sticky=tk.W) 
        ttk.Label(tab2, text= "min/max wartość ").grid(column=2, row=3, sticky=tk.W, pady=5,padx=5)  
        annotateCheck = ttk.Checkbutton(tab2, variable=self.annotateVar ).grid(column=3, row=3, sticky=tk.W) 
        
    def generateReportGui(self):
        self.startDate = tk.StringVar()
        self.endDate = tk.StringVar()

        def runReport():
            dataObj.generateReport(self.startDate.get(), self.endDate.get()) 
        
        tabControlRep = ttk.Notebook(self.win) 
        tab1, tab2 = ttk.Frame(tabControlRep),  ttk.Frame(tabControlRep) 
        tabControlRep.add(tab1, text="Raporty")
        tabControlRep.add(tab2, text="Inne")
        tabControlRep.grid(column=7, columnspan=3, rowspan=3,row=1, padx=4, pady=4)
        
        reportFrame = ttk.LabelFrame(tab1, text= "Generuj Raport", labelanchor="n")
        reportFrame.grid(column=7, row=1, columnspan=3, rowspan=3, padx=5, sticky=tk.W)
        self.createToolTip(reportFrame, "wygeneruj i zapisz raporty (txt, csv) z wybranego\nokresu czasu w katalogu domyślnym 'Reports'", -80)
        ttk.Label(reportFrame, text= "data od (RRRR-MM-DD): ").grid(column=7, row=1, sticky=tk.W, pady=5, padx=5) 
        ttk.Label(reportFrame, text= "data do (RRRR-MM-DD):").grid(column=7, row=2, sticky=tk.W, pady=5, padx=5)
        startDateBox = ttk.Entry(reportFrame, width= 10, textvariable= self.startDate)
        startDateBox.grid(column= 8, row= 1, padx=5, pady=5)
        self.createToolTip(startDateBox, "Wpisz datę początkową raportu do wygenerowania.\nData ta nie może być starsza niż 2004-05-04")

        endDateBox = ttk.Entry(reportFrame, width= 10,  textvariable= self.endDate)
        endDateBox.grid(column= 8, row= 2, padx=5, pady=5)
        self.createToolTip(endDateBox, "Wpisz datę końcową raportu do wygenerowania\nDomyślnie data ostatniego dostępnego\nraporu na http://api.nbp.pl")
        endDateBox.insert(tk.END, dataObj.effectiveDateList[-1])
        ttk.Button(reportFrame, text = "Generuj", command = runReport, width=8).grid(column = 9, row = 0 , rowspan=3, padx=5, pady=5, sticky=tk.N)  
        gcCollectButton = ttk.Button(tab2, text = "Garbage Collector", command = self.gcCollect, width=16)
        gcCollectButton.grid(column = 6, row = 1, padx=5)
        self.createToolTip(gcCollectButton, "Ręczne uruchomienie Garbage Collector\n- inicjuje uruchomienie instrukcji, która odpowiada\nza automatyczne zwalnianie pamięci poprzez\nregularną weryfikację stanu pamięci i usuwanie\ntych obiektów, które uznane są za niepotrzebne ", 0, 20)
    
    def progressBar(self):
        graphObj.winFullSet()
        self.progressStep = 0
        self.loadGraph = None
        
        self.pb = ttk.Progressbar(graphObj.winFull,orient='horizontal',mode='determinate',length=1300)
        self.pb.grid(column=2, row=0, columnspan=6, padx=10, pady=10, sticky=tk.W)

        self.value_label = ttk.Label(graphObj.winFull, text=self.update_progress_label(), width=30)
        self.value_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky=tk.W)
    
    def update_progress_label(self):
        return f"{self.loadGraph}: {self.progressStep}/{sum([i.get() for i in self.chVariableList])}"

    def progress(self):
        self.progressStep += 1
        self.loadGraph = graphObj.multiCodeCurrencyList[self.progressStep-1]
        
        if self.pb['value'] < 100: 
            self.pb['value'] += (100/sum([i.get() for i in self.chVariableList]))
            self.value_label['text'] = self.update_progress_label()
            graphObj.winFull.update()
            if self.pb['value']>99:
                self.loadGraph = f'Wczytano'
                self.value_label['text'] = self.update_progress_label()
                time.sleep(0.5)
                self.pb.destroy()
           
    def fullscreenGraphWindow(self):
        self.progressBar()
        graphObj.multiGraphList(self.viewNum, dataObj.rates, [i.get() for i in self.timeRangeVariableList], [i.get() for i in self.chVariableList], [i.get() for i in self.codeVariableList], self.codeCurrencyList)
        
        def buttonCreate():
            ttk.Button(graphObj.winFull, text = "Zamknij", command = graphObj._quit, width=7).grid(column = 10, columnspan = 3, row = 0 , padx=5, pady=5, sticky=tk.E)
            ttk.Button(graphObj.winFull, text = "zapisz", command = graphObj.runSaveGraphPNG2, width=7).grid(column = 10, columnspan = 2, row = 0 , padx=5, pady=5, sticky=tk.W)
        
        def drawGraph():
            dataObj.checkConnection()
            self.winStyle(graphObj.winFull)
            graphObj.themeSet(self.win)
            graphObj.getVar(self.trendLineVarMulti.get(), self.annotateVarMulti.get(), self.oneSubplotVarMulti.get())
            graphObj.drawGraphLoop(dataObj.codeCurrencyDict, dataObj.firstloopEDL, self.progress)
            buttonCreate()
            graphObj.clearList()
            graphObj.winFull.mainloop()
         
        if self.oneSubplotVarMulti.get() != 1:   
            if sum([i.get() for i in self.chVariableList]) < 1 or sum([i.get() for i in self.chVariableList])> 15:     
                graphObj.winFull.destroy()
                mBox.showinfo("rysuj od 1 do 15 wykresów", "ilość rysowanych wykresów musi wynosić conajmniej 1, \ni nie więcej niż 15.\nSprawdź, czy w wykresy do narysowania są zaznaczone w checklist")
            elif "" in graphObj.multiCodeCurrencyList or "" in graphObj.multiTimeRangeList:
                graphObj.winFull.destroy()
                mBox.showinfo("uzupełnij wszystkie pola", "uzupełnij wszystkie pola wykresow zaznazczonych do narysowania")
            else:
                drawGraph()
        else:
            if "" in graphObj.multiCodeCurrencyList or "" in graphObj.multiTimeRangeList:
                graphObj.winFull.destroy()
                mBox.showinfo("uzupełnij wszystkie pola", "uzupełnij wszystkie pola wykresow zaznazczonych do narysowania")
            else:
                drawGraph()
                       
graphObj = Graph()   
dataObj = Data()
mainObj = Main()       
mainObj.win.mainloop()

          
    


    
    





   


    


