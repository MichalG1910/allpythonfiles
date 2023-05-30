import psycopg2, os, sys, datetime
import tkinter as tk
from tkinter import ttk
from functools import partial
from classE_Rates101_Data import Data
from classE_Rates101_Tooltip import ToolTip
import pandas as pd
from tkinter import messagebox as mBox

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
         self.logWin.geometry('320x480+600+300')
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

   def updateDBProgressBar(self):
      self.progressStep = -1
      self.pb = ttk.Progressbar(self.logWin,orient='horizontal',mode='determinate',length=280,)
      self.pb.grid(column=0, row=9, padx=20, pady=5, sticky=tk.EW)

      self.value_label = ttk.Label(self.logWin, text=self.update_progress_label(), anchor= 'n')
      self.value_label.grid(column=0, row=8, columnspan=2, padx=10, pady=5, sticky=tk.EW)
      self.pb.update()
      
   def progress(self, repeating):
      
      if self.pb['value'] < 100: 
         self.pb['value'] += ((100/repeating)/2)* 0.99
         self.pb.update()
         
         if self.pb['value']>99:
               self.pb.destroy()
   
   def update_progress_label(self):
      self.loadGraph = [   
         "Database e_ratesdb created successfully........",
         "Table rates created successfully........",
         "sending requests/receiving data from API NBP........",
         "Data inserted to table rates........",
         "Table tablenames created successfully........",
         "Data inserted to tablenames........",
         "Table bidask created successfully........",
         "Data inserted to tabel bidask........"
         ]
      self.progressStep += 1
      return f"{self.loadGraph[self.progressStep]}"
   
   def start(self):
      if self.DBCheckVar.get() == 1:
         self.workingMode = 'Database'
         try:
            self.loginErrorLabel.configure(text="")
            self.validateLogin()
            
         except psycopg2.OperationalError:
            self.loginErrorLabel.configure(text="niepoprawne dane do logowania na serwer")
      else:
         self.workingMode = 'Online_No_Database'
         self.logwin_quit()
          
   def validateLogin(self, username, password, hostname, port):
      dataObj = Data()
      dataObj.checkConnection(self.workingMode)
      print("username entered :", username.get())
      print("password entered :", len(password.get()) * '\u25CF')
      print("hostname entered :", hostname.get())
      print("password entered :", port.get())
      
      if dataObj.checkConnectionFailure == False:
         self.updateDatabase()
      else:
         try:
            self.getLastDate()
            self.getLastTabelNameId()
            self.logwin_quit()
         except psycopg2.OperationalError:
            mBox.showinfo("Brak możliwości korzystania z programu", "Brak połączenia z internetem/\nBrak bazy danych do wykorzystania\nZamykanie programu")
            exit()
   
   def createFields(self):
      self.username =  tk.StringVar()
      self.password =  tk.StringVar()
      self.hostName = tk.StringVar() 
      self.port = tk.StringVar()
      self.noDBCheckVar = tk.IntVar()
      self.DBCheckVar = tk.IntVar()
      self.DBCheckVar.set(1) # ma być 0
      self.validateLogin = partial(self.validateLogin, self.username, self.password, self.hostName, self.port)

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
      
      self.loginErrorLabel = ttk.Label(self.logWin,foreground='red', justify='center',font=("Segoe Ui",10))
      self.loginErrorLabel.grid(columnspan=2, row=2, padx=23, sticky=tk.W)
      
      self.userLabel = ttk.Label(self.logWin, text="username: ", foreground='grey')
      self.userLabel.grid(column=0, row=3, padx=23, pady=10, sticky=tk.W)
      self.userEntry = ttk.Entry(self.logWin, textvariable=self.username, width=18)# state=disabled
      self.userEntry.insert(0,'postgres')# do usuniecia
      self.userEntry.grid(column=0, row=3, padx=23, ipadx=20, pady=10, sticky=tk.NE,)
      
      self.passwordLabel = ttk.Label(self.logWin, text="password: ", foreground='grey')
      self.passwordLabel.grid(column=0, row=4, padx=23, pady=10, sticky=tk.W)
      self.passwordEntry = ttk.Entry(self.logWin, textvariable=self.password, show=f"\u25CF", width=18) #state='disabled'
      self.passwordEntry.insert(0,'grabarzmichal1910')# do usuniecia
      self.passwordEntry.grid(column=0, row=4, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      
      self.hostNameLabel = ttk.Label(self.logWin, text="host name:\n(address) ", foreground='grey')
      self.hostNameLabel.grid(column=0, row=5, padx=23, pady=10, sticky=tk.W)
      self.hostNameEntry = ttk.Entry(self.logWin, textvariable=self.hostName, width=18) #state='disabled'
      self.hostNameEntry.insert(0,'127.0.0.1')# do usuniecia
      self.hostNameEntry.grid(column=0, row=5, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      
      self.portLabel = ttk.Label(self.logWin, text="port: ", foreground='grey')
      self.portLabel.grid(column=0, row=6, padx=23, pady=10, sticky=tk.W)
      self.portEntry = ttk.Entry(self.logWin, textvariable=self.port, width=18) #state='disabled'
      self.portEntry.insert(0,'5432')# do usuniecia
      self.portEntry.grid(column=0, row=6, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      
      loginButton = ttk.Button(self.logWin, text="Start", command=self.start, width=10).grid(column=0, row=7,  padx=10, pady=10)
      
   def scenarioSelection1(self, *ignoredArgs):
      self.noDBCheckVar.set(0) 
      self.DBCheckVar.set(1)
      self.userEntry.configure(state='disabled', foreground='grey')
      self.passwordEntry.configure(state='disabled', foreground='grey')
      self.userLabel.configure(foreground='grey')
      self.passwordLabel.configure(foreground='grey')
      self.hostNameEntry.configure(state='disabled', foreground='grey')
      self.portEntry.configure(state='disabled', foreground='grey')
      self.hostNameLabel.configure(foreground='grey')
      self.portLabel.configure(foreground='grey')
   
   def scenarioSelection2(self, *ignoredArgs):         
      self.DBCheckVar.set(0) 
      self.noDBCheckVar.set(1)
      self.userEntry.configure(state='normal', foreground='white')
      self.passwordEntry.configure(state='normal', foreground='white')
      self.userLabel.configure(foreground='white')
      self.passwordLabel.configure(foreground='white')
      self.hostNameEntry.configure(state='normal', foreground='white')
      self.portEntry.configure(state='normal', foreground='white')
      self.hostNameLabel.configure(foreground='white')
      self.portLabel.configure(foreground='white')
   
   def trace(self):         
      self.noDBCheckVar.trace('w', lambda unused0, unused1, unused2 : self.scenarioSelection1())
      self.DBCheckVar.trace('w', lambda unused0, unused1, unused2 : self.scenarioSelection2())
   
   def cursorObj(self, getusername, getpassword, DB="postgres", gethostname = '127.0.0.1', getport = '5432'):
      self.conn = psycopg2.connect(database=DB, user=getusername, password=getpassword, host=gethostname, port= getport)
      self.cursor = self.conn.cursor()

   def createTabelRates(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
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
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
      dataObj = Data()
      dataObj.reporteErrorChecking(self.startDate, self.endDate, 'Online_No_Database', mboxIgnore)
      
      if dataObj.stop_RunReport == 'no':
         dataObj.ReportLoop(self.progress)
         dataObj.dataFormatting("mid", self.tableName_id, self.progress )
         insert_stmt = '''INSERT INTO rates (currency, code, date, 
         value, tablename_id) VALUES (%s, %s, %s, %s, %s)'''
         self.cursor.executemany(insert_stmt, dataObj.csvList)
         print("Data inserted to table rates........")
         self.printList = dataObj.printList
         self.stop_RunReport = dataObj.stop_RunReport
      mboxIgnore = 'yes'
      self.conn.commit()
      self.conn.close()
   
   def createTabelNames(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
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
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
      dataObj = Data()
      insert_stmt = '''INSERT INTO tablenames (table_symbol, table_name, date) VALUES (%s, %s, %s)'''
      self.cursor.executemany(insert_stmt, self.printList)
      print("Data inserted to tablenames........")
      self.conn.commit()
      self.conn.close()
   
   def createTabelBidAsk(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
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
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
      dataObj = Data()
      dataObj.NBPbidAsk()
      insert_stmt = '''INSERT INTO bidask (currency, code, date, 
      bid, ask, table_name) VALUES (%s, %s, %s, %s, %s, %s)'''
      self.cursor.executemany(insert_stmt, dataObj.csvListWithAsk)
      print("Data inserted to tabel bidask........")
      self.conn.commit()
      self.conn.close()
   
   def getLastDate(self):
         self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
         self.cursor.execute('''SELECT MAX(date) FROM rates''') 
         self.fetchDate = str(self.cursor.fetchall()[0][0])
         self.conn.close()
      
   def getLastTabelNameId(self):
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
      self.cursor.execute('''SELECT MAX(tablename_id) FROM rates''') 
      self.tableName_id = self.cursor.fetchall()[0][0]
      self.conn.close()
   
   def updateDatabase(self):
      self.cursorObj(self.username.get(), self.password.get(),"postgres", self.hostName.get(), self.port.get())
      self.conn.autocommit = True
      self.endDate =str(self.today)

      try:
         self.cursor.execute('''CREATE DATABASE e_ratesdb''')
         self.updateDBProgressBar()
         self.tableName_id = 1
         self.startDate = '2004-05-04'
         print("Database created successfully........")
         self.value_label['text'] = self.update_progress_label()
         self.logWin.update()
         self.conn.close()
         self.createTabelRates()
         self.value_label['text'] = self.update_progress_label()
         self.logWin.update()
         self.insertToTabelRates()
         self.value_label['text'] = self.update_progress_label()
         self.logWin.update()
         self.createTabelNames()
         self.value_label['text'] = self.update_progress_label()
         self.logWin.update()
         self.insertToTabelNames()
         self.value_label['text'] = self.update_progress_label()
         self.logWin.update()
         self.createTabelBidAsk()
         self.value_label['text'] = self.update_progress_label()
         self.logWin.update()
         self.insertToTabelBidAsk()
         self.value_label['text'] = self.update_progress_label()
         self.logWin.update()
         self.getLastDate()
         self.logwin_quit()
      
      except psycopg2.errors.DuplicateDatabase:
         self.getLastDate()
         self.getLastTabelNameId()
         print(f"Database already exist (last update: {self.fetchDate})........")
         lastDBDate = (list(self.fetchDate.split('-')))
         convertDate = [int(i) for i in lastDBDate] 
         lastDBUpdate = datetime.date(convertDate[0], convertDate[1], convertDate[2])
         if lastDBUpdate < self.today:
            self.startDate = str(lastDBUpdate + datetime.timedelta(days=1))
            self.fetchDate = str(self.today)
            try:
               self.mboxIgnore = 'yes'
               self.tableName_id += 1
               self.insertToTabelRates(self.mboxIgnore)
               if self.stop_RunReport == 'no':
                  self.insertToTabelNames()
                  self.insertToTabelBidAsk()
                  print("Database updated........")
               self.getLastDate()
               self.logwin_quit()
            except AttributeError:
               print('Database not updated........')
               self.getLastDate()
               self.logwin_quit()
         else:
            self.logwin_quit()
      
   def latestNBPreportDB(self):
      self.currencyList, self.codeList, self.valueList, self.codeCurrencyDict =[],[],[],{}
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb",self.hostName.get(), self.port.get())
      self.cursor.execute('''SELECT rates_id, currency, code, value FROM rates WHERE date IN (SELECT MAX(date) FROM rates) ORDER BY rates_id''') 
      self.lastList = self.cursor.fetchall()
      
      for t in self.lastList:
         self.currencyList.append(t[1])
         self.codeList.append(t[2])  
         self.valueList.append(t[3])  
         self.codeCurrencyDict[t[2]] = t[1]

      self.cursor.execute('''SELECT rates_id, currency, code, value FROM rates WHERE tablename_id IN (SELECT MAX(tablename_id) -1 FROM rates) ORDER BY rates_id''') 
      self.lastListMinus1Day = self.cursor.fetchall()
      self.ratesUpDown = self.lastListMinus1Day + self.lastList
      self.conn.close()

      del self.lastList, self.lastListMinus1Day

   def NBPbidAskDB(self):
      self.currencyList1, self.codeList1, self.valueList1, self.askList1, self.table_name1=[],[],[],[],[]
      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
      self.cursor.execute('''SELECT currency, code, bid, ask, table_name FROM bidask WHERE date IN (SELECT MAX(date) FROM bidask) ORDER BY bidask_id''') 
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
      self.cursorObj(self.username.get(), self.password.get(), "e_ratesdb", self.hostName.get(), self.port.get())
      self.cursor.execute(f'''SELECT date, value FROM rates WHERE code = '{code[0:3]}' ORDER BY rates_id DESC LIMIT 30''') 
      self.last30List = self.cursor.fetchall()

      for t in self.last30List:
         self.last30EDList.append(str(t[0]))
         self.last30MidList.append(t[1])
      
      self.conn.close()
   def getDataForGraphDB(self, code, timeRange, oneOrMultiNum, username, password, hostName, port, firstloopEDL = None): 
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
         
      self.cursorObj(username, password, "e_ratesdb", hostName, port) 
      self.cursor.execute(f'''SELECT date, value FROM rates WHERE code = '{code[0:3]}' AND date > (SELECT MAX(date) - INTERVAL '{limit} days' FROM rates) ORDER BY rates_id''') 
      
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

      endDateGet = (list(endDate.split('-')))
      convertDateE = [int(i) for i in endDateGet] 
      endDate = datetime.date(convertDateE[0], convertDateE[1], convertDateE[2])
      interval = list(str(endDate - startDate).split(' '))
      self.daysInterval = int(interval[0])

      self.cursorObj(self.username.get(), self.password.get(),"e_ratesdb", self.hostName.get(), self.port.get())
      
      self.cursor.execute(f'''SELECT COUNT(date) FROM rates WHERE date BETWEEN '{startDate}' AND '{endDate}' GROUP BY date ORDER BY date''') 
      self.countDate = self.cursor.fetchall()
     
      self.cursor.execute(f'''SELECT currency, code, value FROM rates WHERE date BETWEEN '{startDate}' AND '{endDate}' ORDER BY rates_id ''')
      self.reportLoopList = self.cursor.fetchall()
      
      for b in self.countDate:
         c = b[0]-1
         self.currencyList, self.codeList, self.valueList = [],[],[]
         for a in self.reportLoopList:
            self.currencyList.append(a[0]) 
            self.codeList.append(a[1]) 
            self.valueList.append(a[2])
            #self.reportLoopList.remove(a) # self.reportLoopList.pop(0) - (0 - indeks)
            if c==0: break
            c -= 1
         del self.reportLoopList[0:b[0]] 
         
         erData = {'currency:': pd.Series(self.currencyList, index=range(1,len(self.currencyList)+1)),
                     'code:': pd.Series(self.codeList, index=range(1,len(self.currencyList)+1)),
                     'value:': pd.Series(self.valueList, index=range(1,len(self.currencyList)+1))}
         self.erDataList.append(erData)
      del erData
      
      self.cursor.execute(f'''SELECT table_symbol, table_name, date FROM tablenames WHERE date BETWEEN '{startDate}' AND '{endDate}' ORDER BY tablename_id''')
      self.printList = self.cursor.fetchall()
      
      self.cursor.execute(f'''SELECT currency, code, date, value FROM rates WHERE date BETWEEN '{startDate}' AND '{endDate}' ORDER BY rates_id''') 
      self.csvList = self.cursor.fetchall()
      
      self.conn.close()




