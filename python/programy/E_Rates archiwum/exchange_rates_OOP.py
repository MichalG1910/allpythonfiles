import datetime
import requests # import biblioteki requests niezbędnej do pobrania danych z serwera
# jeśli python nie widzi jakiejś biblioteki, trzeba ją zainstalować w terminalu:
# pip install requests
class echangeRates():
    def __init__(self):
        self.today = datetime.date.today()
        self.inputData()
        self.getRequest()
        self.responseJson()
        self.dataFormatting()

    def file(self,writeData):
        self.plik = open("./allpythonfiles/python/basics/programy/raport exchangerates.txt", "a") 
        if self.plik.writable():
            self.plik.write(writeData)
            self.plik.close()
    
    def inputData(self):    
        self.data1 = input('podaj datę początkową(RRRR-MM-DD):')
        self.data2 = input('podaj datę końcową(RRRR-MM-DD):')
        dateRange = (f"data początkowa(RRRR-MM-DD): {self.data1}\ndata końcowa(RRRR-MM-DD): {self.data2}\n\n")
        self.file(dateRange)
    
    def getRequest(self):    
        if self.data1 == '' and self.data2 == '':
            self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
            print('ilośc sprawdzanych dni: ', 1)
            daysRequest = ('ilość sprawdzanych dni: 1\n')
            self.file(daysRequest)
            self.daysLen = 1
        else:   
            self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{self.data1}/{self.data2}/?format=json")

            data1_list = (list(self.data1.split('-')))
            sdList = [int(i) for i in data1_list] # to samo co niżej, tylko uproszczone
            '''
            for i in data1_list:
                sdList.append(int(i))
            '''
            data2_list = (list(self.data2.split('-')))
            edList = [int(i) for i in data2_list]
            startDate = datetime.date(sdList[0], sdList[1], sdList[2])
            endDate = datetime.date(edList[0], edList[1], edList[2])
            days = endDate - startDate
            self.daysLen = days.days
            print('ilośc sprawdzanych dni: ', self.daysLen)
            daysRequest = (f'ilośc sprawdzanych dni: {self.daysLen}\n')
            self.file(daysRequest)
    
    def responseJson(self):
        if self.response.ok == True: # sprawdzenie, czy serwer odpowiada poprawnie
            self.data = self.response.json()[0:self.daysLen] # parsowanie danych z formatu teksowego na format do odczytu w python
            print('ilość raportów NBP z tych dni (tylko dni pracujące):', len(self.data)) # wynik jest to lista która zawiera słownik. W tym słowniku mamy klucz "rates" którego wartość zawiera następną listę słowników, już z danymi nas interesującymi, czyli kursami walut
            daysResponse = (f'ilość raportów NBP z tych dni (tylko dni pracujące): {len(self.data)}\n\n')
            self.file(daysResponse)
            
    def dataFormatting(self):           
        for dict in self.data:
            table = dict["table"]
            no = dict["no"]
            effectiveDate= dict["effectiveDate"]
            print("\nExchange rates: ", table, no, effectiveDate)
            exchRates = (f"Exchange rates: {table}, {no}, {effectiveDate}\n")
            self.file(exchRates)
            rates = dict["rates"]
            for rate in rates:
                currency = rate["currency"]
                code = rate["code"]
                mid = rate["mid"]
                print(currency, "code: ", code, "value: ", mid)
                currencyInfo = (f"{currency}, code: {code}, value: {mid}\n")
                self.file(currencyInfo)
            print('ilość walut: ',len(rates))
            currencyCount = (f"ilość walut: {len(rates)}\n\n")
            self.file(currencyCount)

oop = echangeRates()
    


