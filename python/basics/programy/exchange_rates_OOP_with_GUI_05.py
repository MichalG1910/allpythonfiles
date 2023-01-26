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
import PIL
#from PIL import TkImage
from PIL import Image
import matplotlib.pyplot as plt
import sys
import math
import pylab
class EchangeRates():
    def __init__(self):
        
        self.filePath = os.path.dirname(sys.argv[0]) # ścieżka do naszego pliku exchange_rates
        self.today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.Num = 0
        self.startOpen()
        self.gui()
           
    def fileWrite(self,writeData):
        if self.Num == 0:
            if self.start.writable():
                self.start.write(writeData)
        else:
            if self.raport.writable():
                self.raport.write(writeData)
    
    def plikRename(self):            
        if os.path.exists(f"{self.filePath}/raports/raport_exchangerates_{self.yesterday}.txt") and self.effectiveDateList[-1] != self.today:
            os.remove(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt")
        else:
            if str(self.today) == str(self.effectiveDateList[-1]):
                pass
            else:
                os.rename(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt", f"{self.filePath}/raports/raport_exchangerates_{self.effectiveDateList[-1]}.txt" )
        
    def startOpen(self):
        if os.path.exists(f"{self.filePath}/raports"):
            pass
        else:
            path = os.path.join(self.filePath, "raports")
            os.mkdir(path)
        
        self.start = open(f"{self.filePath}/raports/raport_exchangerates_{self.today}.txt", "w")
        self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
        self.daysLen = 1
        self.responseJson()
        self.dataFormatting(self.start)
        self.firstloopEDL = self.effectiveDateList[-1]
        self.plikRename()  
        self.Num = 1 

    def raportOpen(self):
        if not re.match(r"^20[1-2][0-9][-](0[0-9]|1[0-2])[-]([0-2][0-9]|3[0-1])$",self.startDate.get()) or not re.match(r"^20[1-2][0-9][-](0[0-9]|1[0-2])[-]([0-2][0-9]|3[0-1])$",self.endDate.get()):
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
            elif str(eDate) != str(self.firstloopEDL):
                print(self.firstloopEDL, type(self.firstloopEDL))
                print(eDate, type(eDate))
                print(self.today, type(self.today))
                mBox.showinfo("Raport NBP nie opublikowany", "Zwykle publikacja odbywa się w dni robocze około godziny 13:00\nWprowadź inną datę")

            else:
                self.raport = open(f"{self.filePath}/raports/raport_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt", "w")
                self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{self.startDate.get()}/{self.endDate.get()}/?format=json")
                
                sumdays = eDate - sDate
                self.daysLen = sumdays.days + 1
                print(self.daysLen)
                self.responseJson()
                self.dataFormatting(self.raport)
                     
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
            
    def dataFormatting(self, whichRaport):           
        for dict in self.data:
            self.table = dict["table"]
            self.no = dict["no"]
            self.effectiveDate= dict["effectiveDate"]
            print("\nExchange rates: ", self.table, self.no, self.effectiveDate)
            exchRates = (f"Exchange rates: {self.table}, {self.no}, {self.effectiveDate}\n")
            self.fileWrite(exchRates)
            self.rates = dict["rates"]
            self.currencyList, self.codeList, self.valueList, self.effectiveDateList, self.codeCurrencyDict= [],[],[],[],{}
            self.effectiveDateList.append(self.effectiveDate)
            for rate in self.rates:
                self.currency = rate["currency"]
                self.code = rate["code"]
                self.mid = rate["mid"]
                print(self.currency, "code: ", self.code, "value: ", self.mid)
                currencyInfo = (f"{self.currency}, code: {self.code}, value: {self.mid}\n")
                self.fileWrite(currencyInfo)
                self.currencyList.append(self.currency), self.codeList.append(self.code), self.valueList.append(self.mid)
                self.codeCurrencyDict[self.code] = self.currency
            print('ilość walut: ',len(self.rates))
            currencyCount = (f"ilość walut: {len(self.rates)}\n\n")
            self.fileWrite(currencyCount)
        whichRaport.close()

    def getDataForGraph(self):
        self.code = (self.currencyName.get()[0:3]).lower()
        if self.timeRange.get() == "30 dni" or self.timeRange.get() == "60 dni" or self.timeRange.get() == "90 dni":
            self.timeRange30_60_90 = int(self.timeRange.get()[0:2])
            startDate30_60_90 = self.today - datetime.timedelta(days=self.timeRange30_60_90)
            self.currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/{startDate30_60_90}/{self.today}/?format=json")
            self.responseJson()
            self.graphData = [dict0["rates"] for dict0 in self.graphData].pop()
        
        elif self.timeRange.get() == "pół roku":
            self.timeRange180 = 182
            repeat = 2
            startDate180 = self.today - datetime.timedelta(days=182)
            halfDate = startDate180 + datetime.timedelta(days=91)
            
            self.currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/{startDate180}/{halfDate}/?format=json") 
            self.responseJson()
            graphData1 = [dict1["rates"] for dict1 in self.graphData].pop()
            
            self.currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/{halfDate+datetime.timedelta(days=1)}/{self.today}/?format=json")
            self.responseJson()
            graphData2 = [dict2["rates"] for dict2 in self.graphData].pop()
            graphData1 += graphData2
            self.graphData = graphData1
        
        elif self.timeRange.get() == "rok":
            self.timeRange180 = 364
            repeat = 8
            pass
        elif self.timeRange.get() == "2 lata":
            timeRange = 728
            repeat = 8
            step = 91
            startDate = self.today - datetime.timedelta(days=timeRange)
            stepDate = startDate + datetime.timedelta(days=step)
            print(startDate, stepDate)
            stepTimedelta = datetime.timedelta(days=step) + datetime.timedelta(days=1)
            print(stepTimedelta)
            gdList = []
            while repeat > 0:
                
                self.currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/{startDate}/{stepDate}/?format=json") 
                self.responseJson()
                graphData = [dict["rates"] for dict in self.graphData].pop()
                gdList += graphData
                
                startDate = startDate + stepTimedelta
                if repeat == 2:
                    date1_list = (list(self.effectiveDateList[-1].split('-')))
                    sdList = [int(i) for i in date1_list] 
                    stepDate = datetime.date(sdList[0], sdList[1], sdList[2])
                    print(stepDate)
                else:
                    stepDate = stepDate + stepTimedelta
                print(startDate, stepDate)
                print(type(startDate), type(stepDate))
                repeat -= 1
            print(gdList)
            self.graphData = gdList 
                
        elif self.timeRange.get() == "5 lat":
            self.timeRange180 = 1820
            repeat = 20
            pass
        elif self.timeRange.get() == "10 lat":
            self.timeRange180 = 3640
            repeat = 40
            pass
        else:
            pass

        def timeRangeLoop():
            timeRange = 182
            repeat = 2
            startDate = self.today - datetime.timedelta(days=timeRange)
            step = startDate + datetime.timedelta(days=(timeRange / repeat))
            while repeat > 0:
                self.currencyResponse = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/{startDate}/{step}/?format=json") 
                self.responseJson()
                graphData = [dict["rates"] for dict in self.graphData].pop()
                self.graphData += graphData
                startDate += (step + datetime.timedelta(days=1))
                step += (step + datetime.timedelta(days=1))
                print(startDate, step) 
            print(self.graphData)
        
        self.graphMidList, self.graphEffectiveDateList = [],[]
        for rate in self.graphData:
            self.graphEffectiveDate = rate["effectiveDate"]
            self.graphMid = rate["mid"]
            self.graphEffectiveDateList.append(self.graphEffectiveDate)
            self.graphMidList.append(self.graphMid)
            

    def gui(self):

        def winStyle():
            sv_ttk.set_theme("dark")
            #style.theme_use('vista')  
            #self.win.configure(background="black") 
            #win.overrideredirect(True)
            #win.geometry("{0}x{1}".format(win.winfo_screenwidth(), win.winfo_screenheight()))
            #win.attributes("-zoomed", True) # otwiera pełne okno
            if win.winfo_screenwidth() < 1300:
                win.geometry("900x890")
            else:
                win.geometry("1680x890")
            win.title("Exchange Rates from NBP v1.0")
            # https://trinket.io/pygame/f5af3f7500  paleta kolorów
            
            #style = ttk.Style(self.win)
            #self.win.tk.call("source", "https://github.com/rdbende/Azure-ttk-theme")
            #style.theme_use('azure')
        
        def generateGraphGui():
            self.getDataForGraph()
            #print(plt.style.available) # dostępne style wbudowane w matplotlib
            '''
            ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 
            'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 
            'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 
            'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 
            'tableau-colorblind10']
            '''
            plt.style.use('dark_background')
            #fig = Figure(figsize=(12,8), facecolor = "grey") # obiekt (prostokąt 12 x 8 pikseli) - będzie to prostokąt na którym umieścimy wykres
            fig = plt.figure(figsize=(12,8), facecolor = "grey")
            axis = fig.add_subplot(111) # rozmieszczenie naszego wykresu w oknie fig (211- 2 to dwa rzędy w oknie, 1 to jedna kolumna, 1 to umieszczenie wykresu w 1 rzędzie )

            xValues = self.graphEffectiveDateList # wartości na naszym wykresie
            yValues = self.graphMidList
            xValuesLen = len(xValues)-1
            a = math.ceil(xValuesLen / 7)
            b = list(range(1,xValuesLen, a))
            print(a)
            print(b)
            axis.plot(xValues, yValues) # drukowanie wartości na naszym wykresie
            xaxis = axis.get_xaxis()
            xaxis.set_ticks(b)
            axis.set_xlabel("Data") # etykiety naszych osi
            axis.set_ylabel("PLN Złoty")
            
            
            canvas = FigureCanvasTkAgg(fig, master=win) # umieszczamy nasze okno wykresu fig na naszym głównym oknie root
            canvas._tkcanvas.grid(column=4, row=5, columnspan=8, padx=10, pady=10) # ułożenie naszego okna w głównym oknie
            
            win.update()
            win.deiconify()
        def saveGraphPNG():
                plt.savefig(f"{self.filePath}/raports/{self.code.upper()} ostatnie {self.timeRange.get()}.png", dpi=200)

        def exchangeRatesTabel():
            echangeRateFrame = ttk.LabelFrame(win, text= f"Średnie kursy walut {self.effectiveDateList[-1]}", labelanchor="n")  
            echangeRateFrame.grid(column=1, row=0, columnspan=3, rowspan=(len(self.rates)+1), padx=5, sticky=tk.W)
            self.currencyLabel = ttk.Label(echangeRateFrame, text= "Waluta:").grid(column=0, row=0, sticky=tk.W, padx=5)
            self.codeLabel = ttk.Label(echangeRateFrame, text= "Kod:").grid(column=1, row=0, sticky=tk.W, padx=5)
            self.valueLabel = ttk.Label(echangeRateFrame, text= "Wartość w PLN:").grid(column=2, row=0, sticky=tk.W, padx=2)
            for t in range(33):
                ttk.Label(echangeRateFrame, background= 'grey19', width=35, text= f'{self.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(echangeRateFrame, background= 'grey19', width=5, text= f'{self.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=3, pady=3)
                ttk.Label(echangeRateFrame, background= "grey19", width=12, text= f'{self.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=3, pady=3)
            
        def plotGraphGui():    
            plotGraphFrame = ttk.LabelFrame(win, text= "Rysowanie wykresu", labelanchor="n") # labelanchor="n" wyśrodkuje teks labelframe 
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
            rangeChosen["values"] = ("30 dni", "60 dni", "90 dni","pół roku", "rok", "2 lata", "5 lat", "10 lat") 
            rangeChosen.grid(column= 5, row= 2, padx=5)
            rangeChosen.current(0)

            drawGraph = ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = generateGraphGui) # tworzymy nasz przycisk, command- odnosi się do naszej funkcji ze zdefiniowanymi 
            drawGraph.grid(column = 6, row = 1)
            saveGraph = ttk.Button(plotGraphFrame, text = "Zapisz wykres", command = saveGraphPNG) # tworzymy nasz przycisk, command- odnosi się do naszej funkcji ze zdefiniowanymi 
            saveGraph.grid(column = 6, row = 2)
            
        def generateRaportGui():    
            raportFrame = ttk.LabelFrame(win, text= "Generuj raport", labelanchor="n")
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
        
        win = tk.Tk()
        winStyle()
        exchangeRatesTabel()
        plotGraphGui()
        generateRaportGui()
        win.mainloop()
        
oop = EchangeRates()



   


    

