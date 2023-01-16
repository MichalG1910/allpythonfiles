
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
        self.fileOpen()
        self.startDate()
        # self.inputData()
        self.getRequest()
        self.responseJson()
        self.dataFormatting()
        self.fileClose()
        self.widgets()
    
    def startDate(self):
        self.date1 = ''
        self.date2 = ''
        start_date = (f"data raportu: {self.today}\n\n")
        self.fileWrite(start_date)
    
    def fileOpen(self):
        self.plik = open(f"./allpythonfiles/python/basics/programy/raport_exchangerates_{self.today}.txt", "w")

    def fileWrite(self,writeData): 
        if self.plik.writable():
            self.plik.write(writeData)
            
    def fileClose(self):
        self.plik.close()
    
    def inputData(self):    
        self.date1 = input('podaj datę początkową(RRRR-MM-DD):')
        self.date2 = input('podaj datę końcową(RRRR-MM-DD):')
        dateRange = (f"data początkowa(RRRR-MM-DD): {self.date1}\ndata końcowa(RRRR-MM-DD): {self.date2}\n\n")
        self.fileWrite(dateRange)
    
    def getRequest(self):    
        if self.date1 == '' and self.date2 == '':
            self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
            print('ilośc sprawdzanych dni: ', 1)
            daysRequest = ('ilość sprawdzanych dni: 1\n')
            self.fileWrite(daysRequest)
            self.daysLen = 1
        else:   
            self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{self.date1}/{self.date2}/?format=json")

            date1_list = (list(self.date1.split('-')))
            sdList = [int(i) for i in date1_list] # to samo co niżej, tylko uproszczone
            '''
            for i in data1_list:
                sdList.append(int(i))
            '''
            date2_list = (list(self.date2.split('-')))
            edList = [int(i) for i in date2_list]
            startDate = datetime.date(sdList[0], sdList[1], sdList[2])
            endDate = datetime.date(edList[0], edList[1], edList[2])
            days = endDate - startDate
            self.daysLen = days.days
            print('ilośc sprawdzanych dni: ', self.daysLen)
            daysRequest = (f'ilośc sprawdzanych dni: {self.daysLen}\n')
            self.fileWrite(daysRequest)
    
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
    def widgets(self):
        self.currencyLabel = ttk.Label(self.win, text= "Waluta:").grid(column=0, row=0, sticky=tk.W, padx=5)
        self.codeLabel = ttk.Label(self.win, text= "Kod:").grid(column=1, row=0, sticky=tk.W, padx=5)
        self.valueLabel = ttk.Label(self.win, text= "Wartość w PLN:").grid(column=2, row=0, sticky=tk.W, padx=2)
        for t in range(33):
            self.textbox1 = ttk.Label(self.win, background= 'White', width=35, text= f'{self.currencyList[t]}').grid(column=0, row=t+1, sticky=tk.W, padx=3, pady=3)
            self.textbox2 = ttk.Label(self.win, background= 'White', width=5, text= f'{self.codeList[t]}').grid(column=1, row=t+1, sticky=tk.W, padx=3, pady=3)
            self.textbox3 = ttk.Label(self.win, background= 'White', width=12, text= f'{self.valueList[t]}').grid(column=2, row=t+1, sticky=tk.W, padx=3, pady=3)
        
        plotGraphFrame = ttk.LabelFrame(self.win, text= "Rysowanie wykresu", labelanchor="n") # labelanchor="n" wyśrodkuje teks labelframe 
        plotGraphFrame.grid(column=4, row=0, columnspan=3, rowspan=3, padx=5, sticky = 'W')
        ttk.Label(plotGraphFrame, text= "Waluta ").grid(column=4, row=1, sticky=tk.W, pady=2) 
        ttk.Label(plotGraphFrame, text= "Przedział czasowy ").grid(column=4, row=2, sticky=tk.W, pady=4)
        
        self.currencyName = tk.StringVar 
        numberChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.currencyName, state= "readonly")
        numberChosen["values"] = self.currencyList 
        numberChosen.grid(column= 5, row= 1, padx=5)
        numberChosen.current(7) 

        self.timeRange = tk.StringVar 
        rangeChosen = ttk.Combobox(plotGraphFrame, width= 32, textvariable= self.timeRange, state= "readonly")
        rangeChosen["values"] = ("tydzień", "2 tygodnie", "miesiąc", "pół roku", "Rok", "2 lata", "5 lat") 
        rangeChosen.grid(column= 5, row= 2, padx=5)
        rangeChosen.current(0)
 

oop = echangeRates()
oop.win.mainloop()   


