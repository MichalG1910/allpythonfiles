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
        self.checkConnection()
        self.createReportDir()
        self.latestNBPreport()
        self.gui()
    
    def checkConnection(self):
        hostname = "nbp.pl"
        if sys.platform == 'linux': 
            response = os.system("ping -c 1 " + hostname)
        else:
            response = os.system("ping -n 1 " + hostname)

        if response == 0:
            pass
        else:
            answer = mBox.askyesno("Brak połączenia z serwerem NBP", "Spróbować ponownie połączenia?\nNie = Opuść program") 
            if answer == True:
                self.checkConnection()
            else:
                exit()
            
    def createReportDir(self):
        if os.path.exists(f"{self.filePath}/reports"):
            pass
        else:
            os.mkdir(os.path.join(self.filePath, "reports")) 
     
    def latestNBPreport(self):
        self.num = 0
        self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
        if self.response.ok == True:
            self.daysLen = 1
            self.data = self.response.json()[0:self.daysLen]
            self.dataFormatting()
            self.reportCreate()
            self.terminalPrint()
            del self.data, self.response, self.printList, self.erDataList 
            self.start = None
            self.firstloopEDL = self.effectiveDateList[-1]
    
    def generateReport(self):
        self.num = 1
        if not re.match(r"^20[0-2][0-9][-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])$",self.startDate.get()) or not re.match(r"^20[0-2][0-9][-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])$",self.endDate.get()):
            mBox.showerror("Uwaga", "Nieprawidłowy format daty, wprowadź nową datę")
        else:
            date1_list = (list(self.startDate.get().split('-')))
            sdList = [int(i) for i in date1_list] 
            date2_list = (list(self.endDate.get().split('-')))
            edList = [int(i) for i in date2_list]
            self.sDate = datetime.date(sdList[0], sdList[1], sdList[2])
            self.eDate = datetime.date(edList[0], edList[1], edList[2])
            if self.sDate < datetime.date(2004,5,4):
                mBox.showinfo("Błędny format reportu NBP", "Możliwe jest pobranie reportu ze strony NBP\nzaczynając od daty 2004-05-04. Wcześniejsze reporty mają inny format danych. Więcej informaacji na stronie http://api.nbp.pl")
            elif self.eDate > self.today or self.sDate > self.eDate:
                mBox.showerror("Uwaga", "Niepoprawna data, wprowadź nową datę")
            elif str(self.eDate) > str(self.firstloopEDL):
                mBox.showinfo("Report NBP nie opublikowany", "Zwykle publikacja odbywa się w dni robocze około godziny 13:00\nWprowadź inną datę")
            else:
                self.step = 91
                self.sumdays = self.eDate - self.sDate
                self.daysLen = self.sumdays.days + 1
                self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{self.startDate.get()}/{self.endDate.get()}/?format=json")
                if self.response.ok == False and self.daysLen < 91:
                    mBox.showinfo("Brak raportu NBP z tego dnia/dni!", "W tym przedziale dat nie opublikowano żadnego raportu.\nZwykle publikacja raportu odbywa się w dni robocze około godziny 13:00\nWprowadź inny zakres dat")
                else:
                    self.checkConnection()
                    self.ReportLoop()
                    self.dataFormatting()
                    self.reportCreate() 
                    self.excel_ER_report() 
                    del self.data, self.report, self.excelList, self.printList, self.erDataList, self.response
    
    def ReportLoop(self):
        runDate = self.sDate
        self.repeat = math.ceil(self.daysLen / self.step) 
        stepDate = runDate + datetime.timedelta(days=self.step)
        stepTimedelta = datetime.timedelta(days=self.step) + datetime.timedelta(days=1)
        longerList = []

        while self.repeat > 0:
            if stepDate >= self.eDate: 
                stepDate = self.eDate
                self.repeat = 1
                 
            self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{runDate}/{stepDate}/?format=json") 
            self.data = self.response.json()[0:self.step]
            
            longerList += self.data
            runDate = runDate + stepTimedelta
            stepDate = stepDate + stepTimedelta
            self.repeat -= 1

        self.data = longerList
        del longerList     
            
    def dataFormatting(self):
        self.excelList, self.printList, self.erDataList =[],[],[]
        
        for dict in self.data:
            table = dict["table"]
            no = dict["no"]
            self.effectiveDate= dict["effectiveDate"]
            self.rates = dict["rates"]
            self.printList.append([table, no, self.effectiveDate])
            self.currencyList, self.codeList, self.valueList, self.effectiveDateList, self.codeCurrencyDict= [],[],[],[],{}
            self.effectiveDateList.append(self.effectiveDate)
            
            for rate in self.rates:
                currency = rate["currency"]
                self.code = rate["code"]
                mid = rate["mid"]
                self.currencyList.append(currency), self.codeList.append(self.code), self.valueList.append(mid)
                self.codeCurrencyDict[self.code] = currency
                if self.num == 1:
                    self.excelList.append([currency,self.code,self.effectiveDate,mid])

            erData = {'currency:': pd.Series(self.currencyList, index=range(1,len(self.rates)+1)),
                      'code:': pd.Series(self.codeList, index=range(1,len(self.rates)+1)),
                      'value:': pd.Series(self.valueList, index=range(1,len(self.rates)+1))}
            self.erDataList.append(erData)
            del erData
        
    def reportCreate(self):
        def file_write(fileWrite):
            erDataListLen = len(self.erDataList)
            rpt=0
            fileWrite.write(f'ilośc sprawdzanych dni: {self.daysLen}\nilość reportów NBP z tych dni (tylko dni pracujące): {len(self.data)}\n' )
            
            while rpt < erDataListLen:
                erFrame = pd.DataFrame(self.erDataList[rpt])
                fileWrite.write(f"\n\nExchange rates: {self.printList[rpt][0]},{self.printList[rpt][1]},{self.printList[rpt][2]}\n")
                fileWrite.write(tabulate(erFrame, showindex=True, headers=erFrame.columns))
                rpt += 1

            fileWrite.close()
            del erFrame, fileWrite

        if self.num == 1:
            self.createReportDir()
            self.report = open(f"{self.filePath}/reports/report_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt", "w")
            file_write(self.report)
        else:    
            self.start = open(f"{self.filePath}/reports/report_exchangerates_{self.effectiveDateList[-1]}.txt", "w")
            file_write(self.start)
        
    def excel_ER_report(self):
        excelLen = len(self.excelList)   
        exc=0
        self.excel = open(f"{self.filePath}/reports/EXCEL_exchangerates_{self.startDate.get()}_{self.endDate.get()}.csv", "w")           
        self.excel.write(f"currency,code,date,value\n")
            
        while exc < excelLen:
            self.excel.write(f"{self.excelList[exc][0]},{self.excelList[exc][1]},{self.excelList[exc][2]},{self.excelList[exc][3]}\n")
            exc += 1

        self.excel.close()
            
    def terminalPrint(self):
        printListLen = len(self.printList)
        rpt=0
        print(f'ilośc sprawdzanych dni: {self.daysLen}\nilość reportów NBP z tych dni (tylko dni pracujące):', len(self.data) )
        
        while rpt < printListLen:
            erFrame = pd.DataFrame(self.erDataList[rpt])
            print(f"\nExchange rates: {self.printList[rpt][0]},{self.printList[rpt][1]},{self.printList[rpt][2]}")
            print(tabulate(erFrame, showindex=True, headers=erFrame.columns))
            rpt += 1
        
    def getDataForGraph(self):
        self.code = (self.currencyName.get()[0:3]).lower()
        self.graphMidList, self.graphEffectiveDateList, self.gdList = [],[],[]

        def timeRangeLoop():
            runDate = self.today - datetime.timedelta(days=self.dayRange)
            stepDate = runDate + datetime.timedelta(days=self.step)
            stepTimedelta = datetime.timedelta(days=self.step) + datetime.timedelta(days=1)
            self.checkConnection()
            
            while self.repeat > 0:  
                currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/{runDate}/{stepDate}/?format=json") 
                graphData = currencyResponse.json()
                graphData = [graphData]
                graphData = [dict["rates"] for dict in graphData].pop()
                self.gdList += graphData
                runDate = runDate + stepTimedelta
                if self.repeat == 2:
                    date1_list = (list(self.firstloopEDL.split('-')))
                    sdList = [int(i) for i in date1_list] 
                    stepDate = datetime.date(sdList[0], sdList[1], sdList[2])
                else:
                    stepDate = stepDate + stepTimedelta
                self.repeat -= 1
            graphData = self.gdList 
            del self.gdList
            
            for rate in graphData:
                graphEffectiveDate = rate["effectiveDate"]
                graphMid = rate["mid"]
                self.graphEffectiveDateList.append(graphEffectiveDate)
                self.graphMidList.append(graphMid)

            self.xValues = self.graphEffectiveDateList 
            self.yValues = self.graphMidList
            del graphData, self.graphEffectiveDateList, self.graphMidList

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
        elif self.timeRange.get() == "15 lat":
            self.dayRange, self.repeat, self.step = 5460, 60, 91
            timeRangeLoop()   
    
    def gui(self):
        
        def refreshGraph():
            if win.tk.call("ttk::style", "theme", "use") == "azure-dark":
                plt.style.use('dark_background')
                fig = plt.figure(figsize=(12,8), facecolor = "dimgray")
            else:
                plt.style.use('Solarize_Light2')
                fig = plt.figure(figsize=(12,8), facecolor = "lightcyan")
            
            axis = fig.add_subplot(111) 
            axis.set_title(f"{self.code.upper()} {self.codeCurrencyDict[self.code.upper()]}", fontsize=16, color="silver")
            axis.grid(linestyle="solid", color="darkslategray",  linewidth=0.4)
            xValuesLen = len(self.xValues)-1
            a = math.ceil(xValuesLen / 20)
            b = list(range(1,xValuesLen, a))
            b.append(xValuesLen)
            axis.plot(self.xValues, self.yValues) 
            xaxis = axis.get_xaxis()
            xaxis.set_ticks(b)
            plt.xticks(rotation=45, fontsize=8)
            axis.set_xlabel("Data") 
            axis.set_ylabel("PLN Złoty")
            canvas = FigureCanvasTkAgg(fig, master=win) 
            canvas._tkcanvas.grid(column=4, row=6, columnspan=8, padx=5, pady=5) 
            win.update()
            win.deiconify()

        def newGraph():
            self.getDataForGraph()
            refreshGraph()

        def saveGraphPNG():
            self.createReportDir()
            plt.savefig(f"{self.filePath}/reports/{self.code.upper()} ostatnie {self.timeRange.get()}.png", dpi=200)
        
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
                    refreshGraph()
                    
                else:
                    win.tk.call("set_theme", "dark")
                    icon2 = PhotoImage(file=f'{self.filePath}/dark.png')
                    self.accentbutton.configure(image=icon2 )
                    self.accentbutton.image = icon2
                    refreshGraph()
                    
            icon = PhotoImage(file=f'{self.filePath}/dark.png')
            self.accentbutton = ttk.Button(win, image=icon, command=change_theme)
            self.accentbutton.image = icon
            self.accentbutton.grid(row=0, column=11, padx=5, pady=5, sticky="nsew")

        def exchangeRatesTabel():
            echangeRateFrame = ttk.LabelFrame(win, text= f"Średnie kursy walut {self.effectiveDateList[-1]}", labelanchor="n", style='clam.TLabelframe')  
            echangeRateFrame.grid(column=1, row=0, columnspan=3, rowspan=(len(self.rates)+1), padx=5, sticky=tk.W)
            
            ttk.Label(echangeRateFrame, text= "Waluta:").grid(column=0, row=0, sticky=tk.W, padx=5)
            ttk.Label(echangeRateFrame, text= "Kod:").grid(column=1, row=0, sticky=tk.W, padx=5)
            ttk.Label(echangeRateFrame, text= "Wartość w PLN:").grid(column=2, row=0, sticky=tk.W, padx=2)
            
            for t in range(33):
                ttk.Label(echangeRateFrame,  width=35, text= f'{self.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(echangeRateFrame,  width=5, text= f'{self.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(echangeRateFrame,  width=12, text= f'{self.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=3, pady=3)
            
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
            rangeChosen["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat", "15 lat") 
            rangeChosen.grid(column= 5, row= 2, padx=5, pady=5)
            rangeChosen.current(0)
            ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = newGraph, width=12).grid(column = 6, row = 1, padx=5)  
            ttk.Button(plotGraphFrame, text = "Zapisz wykres", command = saveGraphPNG, width=12).grid(column = 6, row = 2, padx=5) 
            
        def generateReportGui():    
            reportFrame = ttk.LabelFrame(win, text= "Generuj raport", labelanchor="n")
            reportFrame.grid(column=7, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.W)
            ttk.Label(reportFrame, text= "data początkowa (RRRR-MM-DD): ").grid(column=7, row=1, sticky=tk.W, pady=5, padx=5) 
            ttk.Label(reportFrame, text= "data końcowa (RRRR-MM-DD):").grid(column=7, row=2, sticky=tk.W, pady=5, padx=5)
                
            self.startDate = tk.StringVar() 
            ttk.Entry(reportFrame, width= 10, textvariable= self.startDate).grid(column= 8, row= 1, padx=5, pady=5)
            
            self.endDate = tk.StringVar()
            endDateBox = ttk.Entry(reportFrame, width= 10,  textvariable= self.endDate)
            endDateBox.grid(column= 8, row= 2, padx=5, pady=5)
            endDateBox.insert(tk.END, self.effectiveDateList[-1])
            ttk.Button(reportFrame, text = "Generuj raport", command = self.generateReport, width=12).grid(column = 9, row = 0 , rowspan=3, padx=5)  
            
        win = tk.Tk()
        winStyle()
        emptyGraph()
        themeButton()
        exchangeRatesTabel()
        graphGui()
        generateReportGui()
        win.mainloop()
        
oop = EchangeRates()



   


    


