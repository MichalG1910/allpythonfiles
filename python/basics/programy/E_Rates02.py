import re, os, sys, math, datetime, requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import PhotoImage
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
from tabulate import tabulate
import PIL
import PIL._tkinter_finder

class EchangeRates():
    def __init__(self):
        
        self.filePath = os.path.dirname(sys.argv[0]) # ścieżka do naszego pliku exchange_rates
        self.today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.Num = 0
        self.createRaportDir()
        self.lastNBPraport()
        self.gui()
    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def createRaportDir(self):
        if os.path.exists(f"{self.filePath}/raports"):
            pass
        else:
            path = os.path.join(self.filePath, "raports")
            os.mkdir(path) 
             
           
    def fileWrite(self,writeData):
        if self.Num == 0:
            if self.start.writable():
                self.start.write(writeData)
        else:
            if self.raport.writable():
                self.raport.write(writeData)
    
    def fileRename(self):            
        if os.path.exists(f"{self.filePath}/raports/raport_exchangerates_{self.yesterday}.txt") and str(self.effectiveDateList[-1]) != str(self.today):
            os.remove(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt")
        else:
            if str(self.today) == str(self.effectiveDateList[-1]):
                pass
            else:
                os.rename(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt", f"{self.filePath}/raports/raport_exchangerates_{self.effectiveDateList[-1]}.txt" )
                
    def lastNBPraport(self):
        self.start = open(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt", "w")
        self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
        if self.response.ok == True:
            self.daysLen = 1
            self.data = self.response.json()[0:self.daysLen]
            self.dataFormatting(self.start)
            self.terminalPrint()
            self.fileRename() 
            self.Num = 1
            del self.data, self.response 
            self.start = None
        else:
            answer = mBox.askyesno("Brak połączenia z serwerem NBP", "Spróbować ponownie połączenia?") # przypisujemy zmienną do naszego pytania tak/nie
            if answer == True:
                self.restart_program()
            else:
                exit()
    
    def generateRaport(self):
        self.firstloopEDL = self.effectiveDateList[-1]

        if not re.match(r"^20[1-2][0-9][-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])$",self.startDate.get()) or not re.match(r"^20[1-2][0-9][-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])$",self.endDate.get()):
            mBox.showerror("Uwaga", "Nieprawidłowy format daty, wprowadź nową datę")
        else:
            date1_list = (list(self.startDate.get().split('-')))
            sdList = [int(i) for i in date1_list] 
            date2_list = (list(self.endDate.get().split('-')))
            edList = [int(i) for i in date2_list]
            sDate = datetime.date(sdList[0], sdList[1], sdList[2])
            eDate = datetime.date(edList[0], edList[1], edList[2])

            if eDate > self.today or sDate > eDate:
                mBox.showerror("Uwaga", "Niepoprawna data, wprowadź nową datę")
            elif str(eDate) > str(self.firstloopEDL):
                mBox.showinfo("Raport NBP nie opublikowany", "Zwykle publikacja odbywa się w dni robocze około godziny 13:00\nWprowadź inną datę")

            else:
                self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{self.startDate.get()}/{self.endDate.get()}/?format=json")
                if self.response.ok == True:
                    self.raport = open(f"{self.filePath}/raports/raport_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt", "w")
                    sumdays = eDate - sDate
                    self.daysLen = sumdays.days + 1
                    self.data = self.response.json()[0:self.daysLen]
                    self.dataFormatting(self.raport) 
                    self.excelERraport()
                    self.terminalPrint()  
                    del self.data, self.raport
                    
                else:
                    mBox.showinfo("Brak raportu NBP z tego dnia/dni!", "Zwykle publikacja odbywa się w dni robocze około godziny 13:00\nWprowadź inną datę") 
            
    def dataFormatting(self, whichRaport):
        self.excelList, self.printList, self.erDataList=[],[],[]
        
        for dict1 in self.data:
            self.table = dict1["table"]
            self.no = dict1["no"]
            self.effectiveDate= dict1["effectiveDate"]
            self.printList.append([self.table, self.no, self.effectiveDate])
            self.rates = dict1["rates"]
            self.currencyList, self.codeList, self.valueList, self.effectiveDateList, self.codeCurrencyDict= [],[],[],[],{}
            self.effectiveDateList.append(self.effectiveDate)
            for rate in self.rates:
                self.currency = rate["currency"]
                self.code = rate["code"]
                self.mid = rate["mid"]
                self.currencyList.append(self.currency), self.codeList.append(self.code), self.valueList.append(self.mid)
                self.codeCurrencyDict[self.code] = self.currency
                if whichRaport != self.start:
                    #self.excel.write(f"{self.currency},{self.code},{self.effectiveDate},{self.mid}\n")
                    self.excelList.append([self.currency,self.code,self.effectiveDate,self.mid])

            erData = {'currency:': pd.Series(self.currencyList, index=range(1,len(self.rates)+1)),
                      'code:': pd.Series(self.codeList, index=range(1,len(self.rates)+1)),
                      'value:': pd.Series(self.valueList, index=range(1,len(self.rates)+1))}
            self.erDataList.append(erData)
        self.raportCreate(whichRaport)
        
    def raportCreate(self, fileWrite):
        erDataListLen = len(self.erDataList)
        rpt=0
        fileWrite.write(f'ilośc sprawdzanych dni: {self.daysLen}\nilość raportów NBP z tych dni (tylko dni pracujące): {len(self.data)}\n\n' )
        while rpt < erDataListLen:
            erFrame = pd.DataFrame(self.erDataList[rpt])
            fileWrite.write(f"\nExchange rates: {self.printList[rpt][0]},{self.printList[rpt][1]},{self.printList[rpt][2]}\n")
            fileWrite.write(tabulate(erFrame, showindex=True, headers=erFrame.columns))
            fileWrite.write(f'\nilość walut: {len(self.rates)}\n')
            rpt += 1
        fileWrite.close()

    def excelERraport(self):
        excelLen = len(self.excelList)
        exc=0
        self.excel = open(f"{self.filePath}/raports/EXCEL_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt", "w")           
        self.excel.write(f"currency,code,value,date\n")
            
        while exc < excelLen:
            self.excel.write(f"{self.excelList[exc][0]},{self.excelList[exc][1]},{self.excelList[exc][2]},{self.excelList[exc][3]}\n")
            exc += 1
        self.excel.close()
            

    def terminalPrint(self):
        printListLen = len(self.printList)
        rpt=0

        print(f'ilośc sprawdzanych dni: {self.daysLen}\nilość raportów NBP z tych dni (tylko dni pracujące):', len(self.data) )
        while rpt < printListLen:
            erFrame = pd.DataFrame(self.erDataList[rpt])
            print(f"\nExchange rates: {self.printList[rpt][0]},{self.printList[rpt][1]},{self.printList[rpt][2]}")
            print(tabulate(erFrame, showindex=True, headers=erFrame.columns))
            print('ilość walut: ',len(self.rates))
            rpt += 1
        
    def getDataForGraph(self):
        self.code = (self.currencyName.get()[0:3]).lower()
        self.graphMidList, self.graphEffectiveDateList, self.gdList = [],[],[]

        def timeRangeLoop():
            self.runDate = self.today - datetime.timedelta(days=self.dayRange)
            self.stepDate = self.runDate + datetime.timedelta(days=self.step)
            self.stepTimedelta = datetime.timedelta(days=self.step) + datetime.timedelta(days=1)
            
            while self.repeat > 0:  
                self.currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/{self.runDate}/{self.stepDate}/?format=json") 
                self.graphData = self.currencyResponse.json()
                self.graphData = [self.graphData]
                graphData = [dict["rates"] for dict in self.graphData].pop()
                self.gdList += graphData
                self.runDate = self.runDate + self.stepTimedelta
                if self.repeat == 2:
                    date1_list = (list(self.effectiveDateList[-1].split('-')))
                    sdList = [int(i) for i in date1_list] 
                    self.stepDate = datetime.date(sdList[0], sdList[1], sdList[2])
                else:
                    self.stepDate = self.stepDate + self.stepTimedelta
                self.repeat -= 1
            self.graphData = self.gdList 

            for rate in self.graphData:
                self.graphEffectiveDate = rate["effectiveDate"]
                self.graphMid = rate["mid"]
                self.graphEffectiveDateList.append(self.graphEffectiveDate)
                self.graphMidList.append(self.graphMid)
            del self.gdList
            del self.graphData

        if self.timeRange.get() == "30 dni" or self.timeRange.get() == "60 dni" or self.timeRange.get() == "90 dni":
            self.dayRange, self.repeat, self.step = int(self.timeRange.get()[0:2]), 1, int(self.timeRange.get()[0:2])
            timeRangeLoop()
        
        elif self.timeRange.get() == "pół roku":
            self.dayRange, self.repeat, self.step = 182, 2, 91
            timeRangeLoop()
        
        elif self.timeRange.get() == "rok":
            self.dayRange, self.repeat, self.step = 364, 4, 91
            timeRangeLoop()

        elif self.timeRange.get() == "2 lata":
            self.dayRange, self.repeat, self.step = 728, 8, 91
            timeRangeLoop()
                
        elif self.timeRange.get() == "5 lat":
            self.dayRange, self.repeat, self.step = 1820, 20, 91
            timeRangeLoop()
            
        elif self.timeRange.get() == "10 lat":
            self.dayRange, self.repeat, self.step = 3640, 40, 91
            timeRangeLoop()   
    
    def gui(self):
        
        def generateGraph():
            self.getDataForGraph()
            
            if win.tk.call("ttk::style", "theme", "use") == "azure-dark":
                plt.style.use('dark_background')
                fig = plt.figure(figsize=(12,8), facecolor = "dimgray")
            else:
                plt.style.use('Solarize_Light2')
                fig = plt.figure(figsize=(12,8), facecolor = "lightcyan")
            
            axis = fig.add_subplot(111) 
            axis.set_title(f"{self.code.upper()} {self.codeCurrencyDict[self.code.upper()]}", fontsize=16, color="silver")
            axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
            xValues = self.graphEffectiveDateList 
            yValues = self.graphMidList
            xValuesLen = len(xValues)-1
            a = math.ceil(xValuesLen / 20)
            b = list(range(1,xValuesLen, a))
            b.append(xValuesLen)
            axis.plot(xValues, yValues) 
            xaxis = axis.get_xaxis()
            xaxis.set_ticks(b)
            plt.xticks(rotation=45, fontsize=8)
            axis.set_xlabel("Data") 
            axis.set_ylabel("PLN Złoty")
             
            canvas = FigureCanvasTkAgg(fig, master=win) 
            canvas._tkcanvas.grid(column=4, row=6, columnspan=8, padx=5, pady=5) 
            
            win.update()
            win.deiconify()
            del xValues 
            del yValues 
            del self.graphEffectiveDateList
            del self.graphMidList

        def saveGraphPNG():
                plt.savefig(f"{self.filePath}/raports/{self.code.upper()} ostatnie {self.timeRange.get()}.png", dpi=200)
        
        def winStyle():
            win.tk.call('source', os.path.join(self.filePath, 'azure.tcl'))
            win.tk.call("set_theme", "dark")
            
        def emptyGraph():
            plt.style.use('dark_background')
            fig = plt.figure(figsize=(12,8), facecolor = "dimgray")
            axis = fig.add_subplot(111) 
            
            axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
            axis.set_xlabel("Data") 
            axis.set_ylabel("PLN Złoty")
             
            canvas = FigureCanvasTkAgg(fig, master=win) 
            canvas._tkcanvas.grid(column=4, row=6, columnspan=8, padx=10, pady=10) 
            
            win.update()
            win.deiconify()

        
        def themeButton():
            def change_theme():
            
                if win.tk.call("ttk::style", "theme", "use") == "azure-dark":
                    win.tk.call("set_theme", "light")
                    icon1 = PhotoImage(file=f'{self.filePath}/light.png')
                    self.accentbutton.configure(image=icon1)
                    self.accentbutton.image = icon1
                    generateGraph()
                    
                else:
                    win.tk.call("set_theme", "dark")
                    icon2 = PhotoImage(file=f'{self.filePath}/dark.png')
                    self.accentbutton.configure(image=icon2 )
                    self.accentbutton.image = icon2
                    generateGraph()
                    
            icon = PhotoImage(file=f'{self.filePath}/dark.png')
            self.accentbutton = ttk.Button(win, image=icon, command=change_theme)
            self.accentbutton.image = icon
            self.accentbutton.grid(row=0, column=11, padx=5, pady=5, sticky="nsew")

        def exchangeRatesTabel():
            self.echangeRateFrame = ttk.LabelFrame(win, text= f"Średnie kursy walut {self.effectiveDateList[-1]}", labelanchor="n", style='clam.TLabelframe')  
            self.echangeRateFrame.grid(column=1, row=0, columnspan=3, rowspan=(len(self.rates)+1), padx=5, sticky=tk.W)
            
            self.currencyLabel = ttk.Label(self.echangeRateFrame, text= "Waluta:").grid(column=0, row=0, sticky=tk.W, padx=5)
            self.codeLabel = ttk.Label(self.echangeRateFrame, text= "Kod:").grid(column=1, row=0, sticky=tk.W, padx=5)
            self.valueLabel = ttk.Label(self.echangeRateFrame, text= "Wartość w PLN:").grid(column=2, row=0, sticky=tk.W, padx=2)
            
            for t in range(33):
                self.col1 = ttk.Label(self.echangeRateFrame,  width=35, text= f'{self.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
                self.col2 = ttk.Label(self.echangeRateFrame,  width=5, text= f'{self.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=3, pady=3)
                self.col3 = ttk.Label(self.echangeRateFrame,  width=12, text= f'{self.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=3, pady=3)
            
        def graphGui():    
            plotGraphFrame = ttk.LabelFrame(win, text= "Rysowanie wykresu", labelanchor="n")  
            plotGraphFrame.grid(column=4, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.E)
            ttk.Label(plotGraphFrame, text= "Waluta ").grid(column=4, row=1, sticky=tk.W, pady=5,padx=5) 
            ttk.Label(plotGraphFrame, text= "Przedział czasowy ").grid(column=4, row=2, sticky=tk.W, pady=5, padx=5)
                
            self.currencyName = tk.StringVar()
            codeCurrencyList = []
            for key,values in self.codeCurrencyDict.items():
                codeCurrencyList.append(f"{key}  {values}")
            currencyChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.currencyName, state= "readonly")
            currencyChosen["values"] = codeCurrencyList 
            currencyChosen.grid(column= 5, row= 1, padx=5,pady=5)
            currencyChosen.current(7)
        
            self.timeRange = tk.StringVar() 
            rangeChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.timeRange, state= "readonly")
            rangeChosen["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat") 
            rangeChosen.grid(column= 5, row= 2, padx=5, pady=5)
            rangeChosen.current(0)

            drawGraph = ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = generateGraph, width=12)  
            drawGraph.grid(column = 6, row = 1, padx=5)
            saveGraph = ttk.Button(plotGraphFrame, text = "Zapisz wykres", command = saveGraphPNG, width=12) 
            saveGraph.grid(column = 6, row = 2, padx=5)
            
        def generateRaportGui():    
            raportFrame = ttk.LabelFrame(win, text= "Generuj raport", labelanchor="n")
            raportFrame.grid(column=7, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.W)
            ttk.Label(raportFrame, text= "data początkowa (RRRR-MM-DD): ").grid(column=7, row=1, sticky=tk.W, pady=5, padx=5) 
            ttk.Label(raportFrame, text= "data końcowa (RRRR-MM-DD):").grid(column=7, row=2, sticky=tk.W, pady=5, padx=5)
                
            self.startDate = tk.StringVar() 
            startDateBox = ttk.Entry(raportFrame, width= 10, textvariable= self.startDate)
            startDateBox.grid(column= 8, row= 1, padx=5, pady=5)
                
            self.endDate = tk.StringVar()
            endDateBox = ttk.Entry(raportFrame, width= 10,  textvariable= self.endDate)
            endDateBox.grid(column= 8, row= 2, padx=5, pady=5)
            endDateBox.insert(tk.END, self.effectiveDateList[-1])

            createRaport = ttk.Button(raportFrame, text = "Generuj raport", command = self.generateRaport, width=12)  
            createRaport.grid(column = 9, row = 0 , rowspan=3, padx=5)
        
        def themeButton():
            def change_theme():
            
                if win.tk.call("ttk::style", "theme", "use") == "azure-dark":
                    win.tk.call("set_theme", "light")
                    icon1 = PhotoImage(file=f'{self.filePath}/light.png')
                    self.accentbutton.configure(image=icon1)
                    self.accentbutton.image = icon1
                    generateGraph()
                    
                else:
                    win.tk.call("set_theme", "dark")
                    icon2 = PhotoImage(file=f'{self.filePath}/dark.png')
                    self.accentbutton.configure(image=icon2 )
                    self.accentbutton.image = icon2
                    generateGraph()
                    
            icon = PhotoImage(file=f'{self.filePath}/dark.png')
            self.accentbutton = ttk.Button(win, image=icon, command=change_theme)
            self.accentbutton.image = icon
            self.accentbutton.grid(row=0, column=11, padx=5, pady=5, sticky="nsew")
            
        win = tk.Tk()
        winStyle()
        emptyGraph()
        themeButton()
        exchangeRatesTabel()
        graphGui()
        generateRaportGui()
        win.mainloop()
        
oop = EchangeRates()



   


    


