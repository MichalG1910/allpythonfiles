import psycopg2, os, sys, datetime
import tkinter as tk
from tkinter import ttk
from functools import partial
from classE_Rates101_Data import Data
from classE_Rates101_Tooltip import ToolTip
import pandas as pd
from tabulate import tabulate

class Scenario:
   def operatingMode(self):
      self.logWin = tk.Tk()
      self.createLogWin()
      self.WinStyle(self.logWin)
      self.createFields()
      self.trace()
      self.today = datetime.date.today()
      self.logWin.protocol("WM_DELETE_WINDOW", self._exitApp)
      self.logWin.mainloop()
      
   def _exitApp(self):
      exit()

   def createLogWin(self):
      self.logWin.geometry('320x300+600+300')
      self.logWin.title('E_Rates')
   
   def WinStyle(self, logWindow):
        logWindow.tk.call('source', os.path.join(os.path.dirname(sys.argv[0]), 'azure.tcl'))
        logWindow.tk.call("set_theme", "dark")

   def createToolTip(self, widget, text, corX=0, corY=0): 
        toolTip = ToolTip(widget)
        def enter(event):
            toolTip.showtip(text, corX, corY)
        def leave(event): 
            toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

   def logwin_quit(self):
      self.logWin.quit()
      self.logWin.destroy()
   
   def start(self):
      if self.DBCheckVar.get() == 1:
         self.validateLogin()
         self.workingMode = 'Database'
      else:
         self.logwin_quit()
         self.workingMode = 'Online_No_Database'
   
   def validateLogin(self, username, password):
      print("username entered :", username.get())
      print("password entered :", password.get())
      self.updateDatabase()
     
      
   def createFields(self):
      self.username =  tk.StringVar()
      self.password =  tk.StringVar()
      self.noDBCheckVar = tk.IntVar()
      self.DBCheckVar = tk.IntVar()
      self.DBCheckVar.set(1) # ma być 0
      self.validateLogin = partial(self.validateLogin, self.username, self.password)

      scenarioFrame = ttk.LabelFrame(self.logWin, text='Wybierz tryb pracy programu', labelanchor="n", style='clam.TLabelframe')
      scenarioFrame.grid(column=0, row=0, padx=23, ipadx=5, pady=10, sticky=tk.EW,)
      noDatabaseLabel = ttk.Label(scenarioFrame, text="pracuj w trybie bez bazy danych")
      noDatabaseLabel.grid(column=0, columnspan=1, row=0, padx=10, pady=10, sticky=tk.W)
      DatabaseLabel = ttk.Label(scenarioFrame, text="pracuj w trybie z bazą danych")
      DatabaseLabel.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
      self.createToolTip(noDatabaseLabel, "aplikacja pracuje w trybie online, pobiera wszystkie dane bezpośrednio z serwerów NBP.\nGenerowanie niektórych danych może trwać dłużej")
      self.createToolTip(DatabaseLabel, "aplikacja tworzy bazę danych PostgreSQL (jeśli nie istnieje). W trakcie pracy wszystkie niezbędne dane\nsą pobierane z tej bazy danych. Uwaga, trzeba mieć zainstalowanego darmowego klienta PostgreSQL.\nWięcej na https://www.postgresql.org")
      self.noDBCheckButton = ttk.Checkbutton(scenarioFrame, variable=self.noDBCheckVar )
      self.noDBCheckButton.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E) # state= "disabled"
      self.DBCheckButton = ttk.Checkbutton(scenarioFrame, variable=self.DBCheckVar,)
      self.DBCheckButton.grid(column=1, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E) # state= "disabled"
      
      self.userLabel = ttk.Label(self.logWin, text="username: ", foreground='grey')
      self.userLabel.grid(column=0, row=2, padx=23, pady=10, sticky=tk.W)
      self.userEntry = ttk.Entry(self.logWin, textvariable=self.username)# state=disabled
      self.userEntry.insert(0,'postgres')# do usuniecia
      self.userEntry.grid(column=0, row=2, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      self.passwordLabel = ttk.Label(self.logWin, text="password: ", foreground='grey')
      self.passwordLabel.grid(column=0, row=3, padx=23, pady=10, sticky=tk.W)
      self.passwordEntry = ttk.Entry(self.logWin, textvariable=self.password, show=f"\u25CF" ) #state='disabled'
      self.passwordEntry.insert(0,'grabarzmichal1910')# do usuniecia
      self.passwordEntry.grid(column=0, row=3, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      loginButton = ttk.Button(self.logWin, text="Start", command=self.start, width=10).grid(column=0, row=4,  padx=10, pady=10)
      
   def scenarioSelection1(self, *ignoredArgs):
      self.noDBCheckVar.set(0) 
      self.DBCheckVar.set(1)
      self.userEntry.configure(state='disabled')
      self.passwordEntry.configure(state='disabled')
      self.userLabel.configure(foreground='grey')
      self.passwordLabel.configure(foreground='grey')
   
   def scenarioSelection2(self, *ignoredArgs):         
      self.DBCheckVar.set(0) 
      self.noDBCheckVar.set(1)
      self.userEntry.configure(state='normal')
      self.passwordEntry.configure(state='normal')
      self.userLabel.configure(foreground='white')
      self.passwordLabel.configure(foreground='white')
   
   def trace(self):         
      self.noDBCheckVar.trace('w', lambda unused0, unused1, unused2 : self.scenarioSelection1())
      self.DBCheckVar.trace('w', lambda unused0, unused1, unused2 : self.scenarioSelection2())
   
   def cursorObj(self, getusername, getpassword, DB="postgres"):
      self.conn = psycopg2.connect(database=DB, user=getusername, password=getpassword, host='127.0.0.1', port= '5432')
      self.cursor = self.conn.cursor()

   def createTabelRates(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      sql ='''CREATE TABLE IF NOT EXISTS rates       
      (
         rates_id SERIAL NOT NULL PRIMARY KEY,
         currency VARCHAR(30),
         code VARCHAR(20),
         date DATE,
         value VARCHAR(20),
         tablename_id INT NOT NULL
      )'''
      self.cursor.execute(sql)
      print("Table rates created successfully........")
      self.conn.commit()
      self.conn.close()
   
   def insertToTabelRates(self, mboxIgnore = 'yes'):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      dataObj = Data()
      dataObj.reporteErrorChecking(self.startDate, self.endDate, 'Online_No_Database', mboxIgnore)
      if dataObj.stop_RunReport == 'no':
         dataObj.ReportLoop()
         dataObj.dataFormatting("mid", self.tableName_id)
         insert_stmt = '''INSERT INTO rates (currency, code, date, 
         value, tablename_id) VALUES (%s, %s, %s, %s, %s)'''
         self.cursor.executemany(insert_stmt, dataObj.csvList)
         print("Data inserted to table rates........")
         self.printList = dataObj.printList
      mboxIgnore = 'yes'
      self.conn.commit()
      self.conn.close()
   
   def createTabelNames(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      sql ='''CREATE TABLE IF NOT EXISTS tablenames       
      (
         tablename_id SERIAL NOT NULL PRIMARY KEY,
         table_symbol VARCHAR(5),
         table_name VARCHAR(20),
         date DATE
      )'''
      self.cursor.execute(sql)
      print("Table tablenames created successfully........")
      self.conn.commit()
      self.conn.close()
   
   def insertToTabelNames(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      dataObj = Data()
      insert_stmt = '''INSERT INTO tablenames (table_symbol, table_name, date) VALUES (%s, %s, %s)'''
      self.cursor.executemany(insert_stmt, self.printList)
      print("Data inserted to tablenames........")
      self.conn.commit()
      self.conn.close()
   
   def createTabelBidAsk(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      sql ='''CREATE TABLE IF NOT EXISTS bidask       
      (
         bidask_id SERIAL NOT NULL PRIMARY KEY,
         currency VARCHAR(30),
         code VARCHAR(20),
         date Date,
         bid VARCHAR(20),
         ask VARCHAR(20),
         table_name VARCHAR(20)
      )'''
      self.cursor.execute(sql)
      print("Table bidask created successfully........")
      self.conn.commit()
      self.conn.close()
   
   def insertToTabelBidAsk(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      dataObj = Data()
      dataObj.NBPbidAsk()
      insert_stmt = '''INSERT INTO bidask (currency, code, date, 
      bid, ask, table_name) VALUES (%s, %s, %s, %s, %s, %s)'''
      self.cursor.executemany(insert_stmt, dataObj.csvListWithAsk)
      print("Data inserted to tabel bidask........")
      self.conn.commit()
      self.conn.close()
   
   def updateDatabase(self):
      
      def getLastDate():
         self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
         self.cursor.execute('''SELECT MAX(date) FROM rates''') # SELECT MAX(DATE date) from e_ratesdb
         self.fetchDate = str(self.cursor.fetchall()[0][0])
         self.conn.close()
      
      def getLastTabelNameId():
         self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
         self.cursor.execute('''SELECT MAX(tablename_id) FROM rates''') # SELECT MAX(DATE date) from e_ratesdb
         self.tableName_id = self.cursor.fetchall()[0][0]
         print(self.tableName_id)
         self.conn.close()
      
      self.cursorObj(self.username.get(), self.password.get())
      self.conn.autocommit = True
      self.endDate =str(self.today)

      try:
         self.cursor.execute('''CREATE DATABASE e_ratesdb''')
         self.tableName_id = 1
         self.startDate = '2004-05-04'
         print("Database created successfully........")
         self.conn.close()
         self.createTabelRates()
         self.insertToTabelRates()
         self.createTabelNames()
         self.insertToTabelNames()
         self.createTabelBidAsk()
         self.insertToTabelBidAsk()
         getLastDate()
         self.logwin_quit()
      except psycopg2.errors.DuplicateDatabase:
         getLastDate()
         getLastTabelNameId()
         print(f"Database already exist (last update: {self.fetchDate})........")
         lastDBDate = (list(self.fetchDate.split('-')))
         convertDate = [int(i) for i in lastDBDate] 
         lastDBUpdate = datetime.date(convertDate[0], convertDate[1], convertDate[2])
         if lastDBUpdate < self.today:
            self.startDate = str(lastDBUpdate + datetime.timedelta(days=1))
            self.fetchDate = str(self.today)
            try:
               dataObj = Data()
               self.mboxIgnore = 'yes'
               self.tableName_id += 1
               self.insertToTabelRates(self.mboxIgnore)
               if dataObj.stop_RunReport == 'no':
                  self.insertToTabelNames()
                  self.insertToTabelBidAsk()
                  print("Database updated........")
               getLastDate()
               self.logwin_quit()
            except AttributeError:
               print('Database not updated........')
               self.logwin_quit()
         else:
            self.logwin_quit()
      
   def latestNBPreportDB(self):
      self.currencyList, self.codeList, self.valueList, self.codeCurrencyDict =[],[],[],{}
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      self.cursor.execute('''SELECT rates_id, currency, code, value FROM rates WHERE date IN (SELECT MAX(date) FROM rates)''') 
      self.lastList = self.cursor.fetchall()
      
      for t in self.lastList:
         self.currencyList.append(t[1])
         self.codeList.append(t[2])  
         self.valueList.append(t[3])  
         self.codeCurrencyDict[t[2]] = t[1] ###################

      self.cursor.execute('''SELECT rates_id, currency, code, value FROM rates WHERE tablename_id IN (SELECT MAX(tablename_id) -1 FROM rates)''') 
      self.lastListMinus1Day = self.cursor.fetchall()
      self.ratesUpDown = self.lastListMinus1Day + self.lastList
      self.conn.close()

      del self.lastList, self.lastListMinus1Day

   def NBPbidAskDB(self):
      self.currencyList1, self.codeList1, self.valueList1, self.askList1, self.table_name1=[],[],[],[],[]
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      self.cursor.execute('''SELECT currency, code, bid, ask, table_name FROM bidask WHERE date IN (SELECT MAX(date) FROM bidask)''') 
      self.lastList = self.cursor.fetchall()
      
      for t in self.lastList:
         self.currencyList1.append(t[0])
         self.codeList1.append(t[1])  
         self.valueList1.append(t[2])  
         self.askList1.append(t[3])  
         self.table_name1.append(t[4])
      
      self.conn.close()

   def last30DataDB(self, code):
      self.last30EDList,self.last30MidList = [],[]
      self.cursorObj(self.username.get(), self.password.get(), "e_ratesdb")
      self.cursor.execute(f'''SELECT date, value FROM rates WHERE code = '{code[0:3]}' ORDER BY rates_id DESC LIMIT 30''') 
      self.last30List = self.cursor.fetchall()

      for t in self.last30List:
         self.last30EDList.append(str(t[0]))
         self.last30MidList.append(t[1])
      
      self.conn.close()
   def getDataForGraphDB(self, code, timeRange, oneOrMultiNum, username, password, firstloopEDL = None): # pwrd ostatnie 2 do del
      self.xValuesMultiGraph, self.yValuesMultiGraph, self.xValues, self.yValues = [],[],[],[]
   
      if timeRange == "30 dni":
         limit = 30
      elif timeRange == "60 dni":
         limit = 60
      elif timeRange == "90 dni":
         limit = 90       
      elif timeRange == "pół roku":
         limit = 182
      elif timeRange == "rok":
         limit = 364
      elif timeRange == "2 lata":
         limit = 728
      elif timeRange == "5 lat":
         limit = 1820
      elif timeRange == "10 lat":
         limit = 3640 
      elif timeRange == "15 lat":
         limit = 5460
         

      self.cursorObj(username, password, "e_ratesdb") 
      self.cursor.execute(f'''SELECT date, value FROM rates WHERE code = '{code[0:3]}' AND date > (SELECT MAX(date) - INTERVAL '{limit} days' FROM rates)''') 
      
      xyValues = self.cursor.fetchall()
      if oneOrMultiNum == 2:
         for t in xyValues:
            self.xValuesMultiGraph.append(str(t[0]))
            self.yValuesMultiGraph.append(float(t[1]))
         self.codeMulti = (code[0:3]).lower()
      else:
         for t in xyValues:
            self.xValues.append(str(t[0]))
            self.yValues.append(float(t[1]))
         self.codeOne = (code[0:3]).lower()
      
      self.conn.close()

   def ReportLoopDB(self, startDate, endDate):
      self.erDataList = []
      startDateGet = (list(startDate.split('-')))
      convertDateS = [int(i) for i in startDateGet] 
      startDate = datetime.date(convertDateS[0], convertDateS[1], convertDateS[2])
      #startDate1 = startDate

      endDateGet = (list(endDate.split('-')))
      convertDateE = [int(i) for i in endDateGet] 
      endDate = datetime.date(convertDateE[0], convertDateE[1], convertDateE[2])
      print(startDate, endDate)
      interval = list(str(endDate - startDate).split(' '))
      print(interval)
      self.daysInterval = int(interval[0])

      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb")
      
      self.currencyList, self.codeList, self.valueList = [],[],[]
      self.cursor.execute(f'''SELECT currency, code, value FROM rates WHERE date BETWEEN '{startDate}' AND '{endDate}' ''') # beetween
      self.reportLoopList = self.cursor.fetchall()
      print(self.reportLoopList)
      for a in self.reportLoopList:
         self.currencyList.append(a[0]) 
         self.codeList.append(a[1]) 
         self.valueList.append(a[2]) 
         
      erData = {'currency:': pd.Series(self.currencyList, index=range(1,len(self.currencyList)+1)),
                  'code:': pd.Series(self.codeList, index=range(1,len(self.currencyList)+1)),
                  'value:': pd.Series(self.valueList, index=range(1,len(self.currencyList)+1))}
      self.erDataList.append(erData)
      del erData
         
      
      """
      for a in range(self.daysInterval + 1):
         self.currencyList, self.codeList, self.valueList = [],[],[]
         self.cursor.execute(f'''SELECT currency, code, value FROM rates WHERE date = '{startDate1}' ''') # beetween
         self.reportLoopList = self.cursor.fetchall()
         if self.reportLoopList == []:
            pass
         else:
            for b in self.reportLoopList:
               self.currencyList.append(b[0]) 
               self.codeList.append(b[1]) 
               self.valueList.append(b[2]) 
               
            erData = {'currency:': pd.Series(self.currencyList, index=range(1,len(self.currencyList)+1)),
                        'code:': pd.Series(self.codeList, index=range(1,len(self.currencyList)+1)),
                        'value:': pd.Series(self.valueList, index=range(1,len(self.currencyList)+1))}
            self.erDataList.append(erData)
            del erData
            
         startDate1 = startDate1 + datetime.timedelta(days=1)
      """
      
      self.cursor.execute(f'''SELECT table_symbol, table_name, date FROM tablenames WHERE date BETWEEN '{startDate}' AND '{endDate}' ''')
      self.printList = self.cursor.fetchall()
      
      self.cursor.execute(f'''SELECT currency, code, date, value FROM rates WHERE date BETWEEN '{startDate}' AND '{endDate}' ''') 
      self.csvList = self.cursor.fetchall()
      
      self.conn.close()
         


