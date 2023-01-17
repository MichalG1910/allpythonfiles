
import tkinter as tk
from tkinter import ttk
import datetime
import requests # import biblioteki requests niezbędnej do pobrania danych z serwera
# jeśli python nie widzi jakiejś biblioteki, trzeba ją zainstalować w terminalu:
# pip install requests
class echangeRates():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Exchange Rates from NBP v1.0")
        self.today = datetime.date.today()
        self.Num = 0
        self.fileOpen()
        self.sDate()
        # self.inputData()
        self.getRequest()
        self.responseJson()
        self.dataFormatting()
        self.fileClose()
        self.exchangeRatesTabel()
        self.plotGraph()
        self.generateRaport()
        
    
    def sDate(self):
        start_date = (f"data raportu: {self.today}\n\n")
        self.fileWrite(start_date)
        
    def fileOpen(self):
        self.plik = open(f"./allpythonfiles/python/basics/programy/raport_exchangerates_{self.today}.txt", "w")

    def fileWrite(self,writeData):
        if self.Num == 0:
            if self.plik.writable():
                self.plik.write(writeData)
        else:
            if self.raport.writable():
                self.raport.write(writeData)
            
    def fileClose(self):
        self.plik.close()
        self.Num = 1
    '''
    def inputData(self):    
        self.date1 = input('podaj datę początkową(RRRR-MM-DD):')
        self.date2 = input('podaj datę końcową(RRRR-MM-DD):')
        dateRange = (f"data początkowa(RRRR-MM-DD): {self.date1}\ndata końcowa(RRRR-MM-DD): {self.date2}\n\n")
        self.fileWrite(dateRange)
    '''
    
    def getRequest(self):    
        self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
        print('ilośc sprawdzanych dni: ', 1)
        daysRequest = ('ilość sprawdzanych dni: 1\n')
        self.fileWrite(daysRequest)
        self.daysLen = 1
    
    def raportRequest(self):
        self.raport = open(f"./allpythonfiles/python/basics/programy/raport_exchangerates_{self.startDate.get()}_{self.endDate.get()}.txt", "w")
        
        dateRange = (f"data początkowa(RRRR-MM-DD): {self.startDate.get()}\ndata końcowa(RRRR-MM-DD): {self.endDate.get()}\n\n")
        self.fileWrite(dateRange)    
        self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{self.startDate.get()}/{self.endDate.get()}/?format=json")
        date1_list = (list(self.startDate.get().split('-')))
        sdList = [int(i) for i in date1_list] # to samo co niżej, tylko uproszczone
        '''
        for i in data1_list:
                sdList.append(int(i))
        '''
        date2_list = (list(self.endDate.get().split('-')))
        edList = [int(i) for i in date2_list]
        sDate = datetime.date(sdList[0], sdList[1], sdList[2])
        eDate = datetime.date(edList[0], edList[1], edList[2])
        sumdays = eDate - sDate
        self.daysLen = sumdays.days
        daysRequest = (f'ilośc sprawdzanych dni: {self.daysLen}\n')
        print(f'\nilośc sprawdzanych dni: {self.daysLen}')
        self.fileWrite(daysRequest)
        self.responseJson()
        self.dataFormatting()
        self.raport.close()
    
    def responseJson(self):
        if self.response.ok == True: # sprawdzenie, czy serwer odpowiada poprawnie
            self.data = self.response.json()[0:self.daysLen] # parsowanie danych z formatu teksowego na format do odczytu w python
            print('ilość raportów NBP z tych dni (tylko dni pracujące):', len(self.data)) # wynik jest to lista która zawiera słownik. W tym słowniku mamy klucz "rates" którego wartość zawiera następną listę słowników, już z danymi nas interesującymi, czyli kursami walut
            daysResponse = (f'ilość raportów NBP z tych dni (tylko dni pracujące): {len(self.data)}\n\n')
            self.fileWrite(daysResponse)
            
    def dataFormatting(self):           
        for dict in self.data:
            table = dict["table"]
            no = dict["no"]
            effectiveDate= dict["effectiveDate"]
            print("\nExchange rates: ", table, no, effectiveDate)
            exchRates = (f"Exchange rates: {table}, {no}, {effectiveDate}\n")
            self.fileWrite(exchRates)
            self.rates = dict["rates"]
            self.currencyList, self.codeList, self.valueList = [],[],[]
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
            print('ilość walut: ',len(self.rates))
            currencyCount = (f"ilość walut: {len(self.rates)}\n\n")
            self.fileWrite(currencyCount)
    
    def exchangeRatesTabel(self):
        echangeRateFrame = ttk.LabelFrame(self.win, text= f"Kursy Walut {self.today}", labelanchor="n")  
        echangeRateFrame.grid(column=1, row=0, columnspan=3, rowspan=(len(self.rates)+1), padx=5, sticky=tk.W)
        self.currencyLabel = ttk.Label(echangeRateFrame, text= "Waluta:").grid(column=0, row=0, sticky=tk.W, padx=5)
        self.codeLabel = ttk.Label(echangeRateFrame, text= "Kod:").grid(column=1, row=0, sticky=tk.W, padx=5)
        self.valueLabel = ttk.Label(echangeRateFrame, text= "Wartość w PLN:").grid(column=2, row=0, sticky=tk.W, padx=2)
        for t in range(33):
            self.textbox1 = ttk.Label(echangeRateFrame, background= 'White', width=35, text= f'{self.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
            self.textbox2 = ttk.Label(echangeRateFrame, background= 'White', width=5, text= f'{self.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=3, pady=3)
            self.textbox3 = ttk.Label(echangeRateFrame, background= 'White', width=12, text= f'{self.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=3, pady=3)
    def plotGraph(self):    
        plotGraphFrame = ttk.LabelFrame(self.win, text= "Rysowanie wykresu", labelanchor="n") # labelanchor="n" wyśrodkuje teks labelframe 
        plotGraphFrame.grid(column=4, row=0, columnspan=3, rowspan=3, padx=5, sticky=tk.W)
        ttk.Label(plotGraphFrame, text= "Waluta ").grid(column=4, row=1, sticky=tk.W, pady=2) 
        ttk.Label(plotGraphFrame, text= "Przedział czasowy ").grid(column=4, row=2, sticky=tk.W, pady=4)
        
        self.currencyName = tk.StringVar() 
        currencyChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.currencyName, state= "readonly")
        currencyChosen["values"] = self.currencyList 
        currencyChosen.grid(column= 5, row= 1, padx=5)
        currencyChosen.current(7) 

        self.timeRange = tk.StringVar() 
        rangeChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.timeRange, state= "readonly")
        rangeChosen["values"] = ("tydzień", "2 tygodnie", "miesiąc", "pół roku", "Rok", "2 lata", "5 lat") 
        rangeChosen.grid(column= 5, row= 2, padx=5)
        rangeChosen.current(0)

        drawGraph = ttk.Button(plotGraphFrame, text = "Rysuj wykres", command = self.generateGraph) # tworzymy nasz przycisk, command- odnosi się do naszej funkcji ze zdefiniowanymi 
        drawGraph.grid(column = 6, row = 0 , rowspan=3)
    
    def generateRaport(self):    
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
        endDateBox.insert(tk.END, f"{self.today}")

        createRaport = ttk.Button(raportFrame, text = "Generuj raport", command = self.raportRequest) # tworzymy nasz przycisk, command- odnosi się do naszej funkcji ze zdefiniowanymi 
        createRaport.grid(column = 9, row = 0 , rowspan=3)
    
    def generateGraph(self):
        pass
        
        
oop = echangeRates()
oop.win.mainloop()   


    


