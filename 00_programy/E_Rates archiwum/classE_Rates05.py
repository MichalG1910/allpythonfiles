import re, os, sys, math, datetime, requests
from tkinter import messagebox as mBox
import pandas as pd
from tabulate import tabulate
import PIL
import PIL._tkinter_finder
class Data:
    def __init__(self):
        
        self.filePath = os.path.dirname(sys.argv[0]) # ścieżka do naszego pliku exchange_rates
        self.today = datetime.date.today()
        
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
            self.reportCreate(startDate=None, endDate=None)
            self.terminalPrint()
            del self.data, self.response, self.printList, self.erDataList 
            self.start = None
            self.firstloopEDL = self.effectiveDateList[-1]

    def NBPratesUpDown(self):
        self.num = 1
        self.response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/last/2/?format=json")
        if self.response.ok == True:
            self.daysLen = 2
            self.data = self.response.json()[0:self.daysLen]
            self.dataFormatting()
        self.ratesUpDown = self.csvList
        del self.csvList
        
    def generateReport(self,startDate, endDate):
        self.num = 1
        if not re.match(r"^20[0-2][0-9][-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])$",startDate) or not re.match(r"^20[0-2][0-9][-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])$",endDate):
            mBox.showerror("Uwaga", "Nieprawidłowy format daty, wprowadź nową datę")
        else:
            date1_list = (list(startDate.split('-')))
            sdList = [int(i) for i in date1_list] 
            date2_list = (list(endDate.split('-')))
            edList = [int(i) for i in date2_list]
            self.sDate = datetime.date(sdList[0], sdList[1], sdList[2])
            self.eDate = datetime.date(edList[0], edList[1], edList[2])
            if self.sDate < datetime.date(2004,5,4):
                mBox.showinfo("Błędny format danych raportu NBP", "Możliwe jest pobranie raportu ze strony NBP\nzaczynając od daty 2004-05-04. Wcześniejsze raporty mają inny format danych. Więcej informaacji na stronie http://api.nbp.pl")
            elif self.eDate > self.today or self.sDate > self.eDate:
                mBox.showerror("Uwaga", "Niewłaściwa data, wprowadź nową datę")
            elif str(self.eDate) > str(self.firstloopEDL):
                mBox.showinfo("Raport NBP nie opublikowany", "Zwykle publikacja odbywa się w dni robocze około godziny 13:00\nWprowadź inną datę")
            else:
                self.step = 91
                self.sumdays = self.eDate - self.sDate
                self.daysLen = self.sumdays.days + 1
                self.response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/A/{startDate}/{endDate}/?format=json")
                if self.response.ok == False and self.daysLen < 91:
                    mBox.showinfo("Brak raportu NBP z tego dnia/dni!", "W tym przedziale dat nie opublikowano żadnego raportu.\nZwykle publikacja raportu odbywa się w dni robocze około godziny 13:00\nWprowadź inny zakres dat")
                else:
                    self.checkConnection()
                    self.ReportLoop()
                    self.dataFormatting()
                    self.reportCreate(startDate, endDate) 
                    self.csv_ER_report(startDate, endDate) 
                    del self.data, self.report, self.csvList, self.printList, self.erDataList, self.response
    
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
        self.csvList, self.printList, self.erDataList =[],[],[]
        
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
                    self.csvList.append([currency,self.code,self.effectiveDate,mid])

            erData = {'currency:': pd.Series(self.currencyList, index=range(1,len(self.rates)+1)),
                      'code:': pd.Series(self.codeList, index=range(1,len(self.rates)+1)),
                      'value:': pd.Series(self.valueList, index=range(1,len(self.rates)+1))}
            self.erDataList.append(erData)
            del erData
        
    def reportCreate(self, startDate, endDate):
        def file_write(fileWrite):
            erDataListLen = len(self.erDataList)
            rpt=0
            fileWrite.write(f'ilośc sprawdzanych dni: {self.daysLen}\nilość raportów NBP z tych dni (tylko dni pracujące): {len(self.data)}\n' )
            
            while rpt < erDataListLen:
                erFrame = pd.DataFrame(self.erDataList[rpt])
                fileWrite.write(f"\n\nExchange rates: {self.printList[rpt][0]},{self.printList[rpt][1]},{self.printList[rpt][2]}\n")
                fileWrite.write(tabulate(erFrame, showindex=True, headers=erFrame.columns))
                rpt += 1

            fileWrite.close()
            del erFrame, fileWrite

        if self.num == 1:
            self.createReportDir()
            self.report = open(f"{self.filePath}/reports/report_exchangerates_{startDate}_{endDate}.txt", "w")
            file_write(self.report)
        else:    
            self.start = open(f"{self.filePath}/reports/report_exchangerates_{self.effectiveDateList[-1]}.txt", "w")
            file_write(self.start)
        
    def csv_ER_report(self, startDate, endDate):
        csvLen = len(self.csvList)   
        exc=0
        self.csv = open(f"{self.filePath}/reports/CSV_exchangerates_{startDate}_{endDate}.csv", "w")           
        self.csv.write(f"currency,code,date,value\n")
            
        while exc < csvLen:
            self.csv.write(f"{self.csvList[exc][0]},{self.csvList[exc][1]},{self.csvList[exc][2]},{self.csvList[exc][3]}\n")
            exc += 1

        self.csv.close()
            
    def terminalPrint(self):
        printListLen = len(self.printList)
        rpt=0
        print(f'ilośc sprawdzanych dni: {self.daysLen}\nilość raportów NBP z tych dni (tylko dni pracujące):', len(self.data) )
        
        while rpt < printListLen:
            erFrame = pd.DataFrame(self.erDataList[rpt])
            print(f"\nExchange rates: {self.printList[rpt][0]},{self.printList[rpt][1]},{self.printList[rpt][2]}")
            print(tabulate(erFrame, showindex=True, headers=erFrame.columns))
            rpt += 1
        
    def getDataForGraph(self, currencyName, timeRange):
        self.code = (currencyName[0:3]).lower()
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

        if timeRange == "30 dni" or timeRange == "60 dni" or timeRange == "90 dni":
            self.dayRange, self.repeat, self.step = int(timeRange[0:2]), 1, int(timeRange[0:2])
            timeRangeLoop()
        elif timeRange == "pół roku":
            self.dayRange, self.repeat, self.step = 182, 2, 91
            timeRangeLoop()
        elif timeRange == "rok":
            self.dayRange, self.repeat, self.step = 364, 4, 91
            timeRangeLoop()
        elif timeRange == "2 lata":
            self.dayRange, self.repeat, self.step = 728, 8, 91
            timeRangeLoop() 
        elif timeRange == "5 lat":
            self.dayRange, self.repeat, self.step = 1820, 20, 91
            timeRangeLoop()
        elif timeRange == "10 lat":
            self.dayRange, self.repeat, self.step = 3640, 40, 91
            timeRangeLoop()   
        elif timeRange == "15 lat":
            self.dayRange, self.repeat, self.step = 5460, 60, 91
            timeRangeLoop()  
 
    
    





   


    

