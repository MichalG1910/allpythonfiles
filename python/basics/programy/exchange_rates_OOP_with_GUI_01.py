import re
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import sv_ttk                                       # biblioteka ze stylem
import datetime
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt
import sys
import math

class EchangeRates():
    def __init__(self):
        self.win = tk.Tk()
        self.winStyle()
        
        self.filePath = os.path.dirname(sys.argv[0]) # ścieżka do naszego pliku exchange_rates
        self.today = datetime.date.today()
        self.getYesterday()
        self.Num = 0
        self.fileOpen()
        self.exchangeRatesTabel()
        self.plotGraphGui()
        self.generateRaportGui()
        self.raportRename()
       
    def winStyle(self):
        #sv_ttk.set_theme("light")
        #style.theme_use('vista') 
        #self.win.configure(background="black")
        self.win.geometry("1580x890")
        self.win.title("Exchange Rates from NBP v1.0")
        # https://trinket.io/pygame/f5af3f7500  paleta kolorów
        
        #style = ttk.Style(self.win)
        #self.win.tk.call("source", "https://github.com/rdbende/Azure-ttk-theme")
        #style.theme_use('azure') 
        
       
    def getYesterday(self): 
        yesterday = self.today - datetime.timedelta(days=1)
        return yesterday
        
    def fileOpen(self):
        if os.path.exists(f"{self.filePath}/raports"):
            pass
        else:
            path = os.path.join(self.filePath, "raports")
            os.mkdir(path)
        
        self.plik = open(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt", "w")
        self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
        self.daysLen = 1
        self.responseJson()
        self.dataFormatting()
        self.plik.close()  
        self.Num = 1 

    def raportOpen(self):
        if not re.match(r"^20[1-2][0-9][-](0[0-9]|1[0-2])[-]([0-1][0-9]|3[0-1])$",self.startDate.get()) or not re.match(r"^20[1-2][0-9][-](0[0-9]|1[0-2])[-]([0-1][0-9]|3[0-1])$",self.endDate.get()):
            mBox.showerror("Uwaga", "Nieprawidłowy format daty, wprowadź nową datę")
        else:
            date1_list = (list(self.startDate.get().split('-')))
            sdList = [int(i) for i in date1_list] 
            date2_list = (list(self.endDate.get().split('-')))
            edList = [int(i) for i in date2_list]
            sDate = datetime.date(sdList[0], sdList[1], sdList[2])
            eDate = datetime.date(edList[0], edList[1], edList[2])
        
            if eDate > self.today or sDate >= eDate:
                mBox.showerror("Uwaga", "Niepprawna data, wprowadź nową datę")
            else:
                self.raport = open(f"{self.filePath}/raports/raport_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt", "w")
                self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{self.startDate.get()}/{self.endDate.get()}/?format=json")
                
                sumdays = eDate - sDate
                self.daysLen = sumdays.days
                self.responseJson()
                self.dataFormatting()
                self.raport.close()   
                self.raportRename()
        
    def fileWrite(self,writeData):
        if self.Num == 0:
            if self.plik.writable():
                self.plik.write(writeData)
        else:
            if self.raport.writable():
                self.raport.write(writeData)
    
    
    
    def responseJson(self):
        if self.response.ok == True: # sprawdzenie, czy serwer odpowiada poprawnie
            if self.daysLen >=0:
                self.data = self.response.json()[0:self.daysLen] # parsowanie danych z formatu teksowego na format do odczytu w python
                print(f'ilośc sprawdzanych dni: {self.daysLen}\nilość raportów NBP z tych dni (tylko dni pracujące):', len(self.data) )
                daysResponse = (f'ilośc sprawdzanych dni: {self.daysLen}\nilość raportów NBP z tych dni (tylko dni pracujące): {len(self.data)}\n\n')
                self.fileWrite(daysResponse)
                self.daysLen = -1
            else:
                self.graphData = self.currencyResponse.json()
                self.graphData = [self.graphData] 
            
    def dataFormatting(self):           
        for dict in self.data:
            table = dict["table"]
            no = dict["no"]
            effectiveDate= dict["effectiveDate"]
            print("\nExchange rates: ", table, no, effectiveDate)
            exchRates = (f"Exchange rates: {table}, {no}, {effectiveDate}\n")
            self.fileWrite(exchRates)
            self.rates = dict["rates"]
            self.currencyList, self.codeList, self.valueList, self.effectiveDateList = [],[],[],[]
            self.effectiveDateList.append(effectiveDate)
            self.codeCurrencyDict = {}
            for rate in self.rates:
                self.currency = rate["currency"]
                self.code = rate["code"]
                self.mid = rate["mid"]
                print(self.currency, "code: ", self.code, "value: ", self.mid)
                currencyInfo = (f"{self.currency}, code: {self.code}, value: {self.mid}\n")
                self.fileWrite(currencyInfo)
                self.currencyList.append(self.currency)
                self.codeList.append(self.code)
                self.valueList.append(self.mid)
                self.codeCurrencyDict[self.code] = self.currency
            print('ilość walut: ',len(self.rates))
            currencyCount = (f"ilość walut: {len(self.rates)}\n\n")
            self.fileWrite(currencyCount)
    
    def raportRename(self):
        if self.startDate.get() == "":
            pass
        else:
            if os.path.exists(f"{self.filePath}/raports/raport_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt") or os.path.exists(f"{self.filePath}/raports/raport_exchangerates_{self.startDate.get()}_{self.getYesterday()}.txt"):
                pass
            else:
                os.rename(f"{self.filePath}/raports/raport_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt", f"{self.filePath}/raports/raport_exchangerates_{self.startDate.get()}_{self.getYesterday()}.txt" )
    def plikRename(self):            
        if os.path.exists(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt"):
            pass
        else:
            os.rename(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt", f"{self.filePath}/raports/raport_exchangerates_{self.getYesterday()}.txt" )
    
    def getDataForGraph(self):
        self.timeRange30_60_90 = int(self.timeRange.get()[0:2])
        startDate30_60_90 = self.today - datetime.timedelta(days=self.timeRange30_60_90)
        endDate30_60_90  = self.today
        code = (self.currencyName.get()[0:3]).lower()
        self.currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/{startDate30_60_90}/{endDate30_60_90}/?format=json")
        
        self.responseJson()

        for dict1 in self.graphData:
            self.graphCurrency = dict1["currency"]
            self.graphCode = dict1["code"]
            self.graphRates = dict1["rates"]
            self.graphMidList, self.graphEffectiveDateList = [],[]
            for rate in self.graphRates:
                self.graphEffectiveDate = rate["effectiveDate"]
                self.graphMid = rate["mid"]
                self.graphEffectiveDateList.append(self.graphEffectiveDate)
                self.graphMidList.append(self.graphMid)

    def generateGraphGui(self):
        self.getDataForGraph()
        # print(plt.style.available) # dostępne style wbudowane w matplotlib
        '''
        ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 
        'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 
        'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
        'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
        '''
        plt.style.use('dark_background')
        fig = Figure(figsize=(12,8), facecolor = "grey") # obiekt (prostokąt 12 x 8 pikseli) - będzie to prostokąt na którym umieścimy wykres

        axis = fig.add_subplot(111) # rozmieszczenie naszego wykresu w oknie fig (211- 2 to dwa rzędy w oknie, 1 to jedna kolumna, 1 to umieszczenie wykresu w 1 rzędzie )

        xValues = self.graphEffectiveDateList # wartości na naszym wykresie
        yValues = self.graphMidList
        xValuesLen = len(xValues)-1
        if xValuesLen > 8:
            a = math.ceil(xValuesLen / 7)
            b = list(range(1,xValuesLen, a))
            print(a)
            print(b)
            axis.plot(xValues, yValues) # drukowanie wartości na naszym wykresie
            xaxis = axis.get_xaxis()
            xaxis.set_ticks(b)
        else:
            pass

        axis.set_xlabel("Data") # etykiety naszych osi
        axis.set_ylabel("PLN Złoty")
        self.win.withdraw()
        canvas = FigureCanvasTkAgg(fig, master=self.win) # umieszczamy nasze okno wykresu fig na naszym głównym oknie root
        canvas._tkcanvas.grid(column=4, row=5, columnspan=8, padx=10, pady=10) # ułożenie naszego okna w głównym oknie

        self.win.update()
        self.win.deiconify()

    def exchangeRatesTabel(self):
        echangeRateFrame = ttk.LabelFrame(self.win, text= f"Średnie kursy walut {self.effectiveDateList[-1]}", labelanchor="n")  
        echangeRateFrame.grid(column=1, row=0, columnspan=3, rowspan=(len(self.rates)+1), padx=5, sticky=tk.W)
        self.currencyLabel = ttk.Label(echangeRateFrame, text= "Waluta:").grid(column=0, row=0, sticky=tk.W, padx=5)
        self.codeLabel = ttk.Label(echangeRateFrame, text= "Kod:").grid(column=1, row=0, sticky=tk.W, padx=5)
        self.valueLabel = ttk.Label(echangeRateFrame, text= "Wartość w PLN:").grid(column=2, row=0, sticky=tk.W, padx=2)
        for t in range(33):
            self.textbox1 = ttk.Label(echangeRateFrame, background= 'white', width=35, text= f'{self.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
            self.textbox2 = ttk.Label(echangeRateFrame, background= 'white', width=5, text= f'{self.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=3, pady=3)
            self.textbox3 = ttk.Label(echangeRateFrame, background= "white", width=12, text= f'{self.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=3, pady=3)
    
    def plotGraphGui(self):    
        plotGraphFrame = ttk.LabelFrame(self.win, text= "Rysowanie wykresu", labelanchor="n") # labelanchor="n" wyśrodkuje teks labelframe 
        plotGraphFrame.grid(column=4, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.E)
        ttk.Label(plotGraphFrame, text= "Waluta ").grid(column=4, row=1, sticky=tk.W, pady=2) 
        ttk.Label(plotGraphFrame, text= "Przedział czasowy ").grid(column=4, row=2, sticky=tk.W, pady=4)
        
        self.currencyName = tk.StringVar()
        codeCurrencyList = []
        for key,values in self.codeCurrencyDict.items():
            codeCurrencyList.append(f"{key}  {values}")
        currencyChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.currencyName, state= "readonly")
        currencyChosen["values"] = codeCurrencyList 
        currencyChosen.grid(column= 5, row= 1, padx=5)
        currencyChosen.current(7)
      

        self.timeRange = tk.StringVar() 
        rangeChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.timeRange, state= "readonly")
        rangeChosen["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "Rok", "2 lata", "5 lat", "10 lat") 
        rangeChosen.grid(column= 5, row= 2, padx=5)
        rangeChosen.current(0)

        drawGraph = ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = self.generateGraphGui) # tworzymy nasz przycisk, command- odnosi się do naszej funkcji ze zdefiniowanymi 
        drawGraph.grid(column = 6, row = 0 , rowspan=3)
    
    def generateRaportGui(self):    
        raportFrame = ttk.LabelFrame(self.win, text= "Generuj raport", labelanchor="n")
        raportFrame.grid(column=7, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.W)
        ttk.Label(raportFrame, text= "data początkowa(RRRR-MM-DD): ").grid(column=7, row=1, sticky=tk.W, pady=2) 
        ttk.Label(raportFrame, text= "data końcowa(RRRR-MM-DD):").grid(column=7, row=2, sticky=tk.W, pady=4)
        
        self.startDate = tk.StringVar() 
        startDateBox = ttk.Entry(raportFrame, width= 10, textvariable= self.startDate)
        startDateBox.grid(column= 8, row= 1, padx=5)
        
        self.endDate = tk.StringVar()
        endDateBox = ttk.Entry(raportFrame, width= 10,  textvariable= self.endDate)
        endDateBox.grid(column= 8, row= 2, padx=5)
        endDateBox.insert(tk.END, self.effectiveDateList[-1])

        createRaport = ttk.Button(raportFrame, text = "Generuj raport", command = self.raportOpen) # tworzymy nasz przycisk, command- odnosi się do naszej funkcji ze zdefiniowanymi 
        createRaport.grid(column = 9, row = 0 , rowspan=3)
    
        

oop = EchangeRates()
oop.win.mainloop()   


    


