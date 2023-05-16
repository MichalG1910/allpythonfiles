import psycopg2, os, sys, datetime
import tkinter as tk
from tkinter import ttk
from functools import partial
from classE_Rates101_Data import Data
from classE_Rates101_Tooltip import ToolTip

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
      self.noDBCheckVar.set(1)
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
      self.userEntry = ttk.Entry(self.logWin, textvariable=self.username, state='disabled')
      self.userEntry.grid(column=0, row=2, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      self.passwordLabel = ttk.Label(self.logWin, text="password: ", foreground='grey')
      self.passwordLabel.grid(column=0, row=3, padx=23, pady=10, sticky=tk.W)
      self.passwordEntry = ttk.Entry(self.logWin, textvariable=self.password, show='*', state='disabled')
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
   
   def cursorObj(self, DB="postgres"):
      self.conn = psycopg2.connect(database=DB, user=self.username.get(), password=self.password.get(), host='127.0.0.1', port= '5432')
      self.cursor = self.conn.cursor()

   def createTabelRates(self):
      self.cursorObj("e_ratesdb")
      sql ='''CREATE TABLE IF NOT EXISTS rates       
      (
         rates_id SERIAL NOT NULL PRIMARY KEY,
         currency VARCHAR(30),
         code VARCHAR(20),
         date DATE,
         value VARCHAR(20)
      )'''
      self.cursor.execute(sql)
      print("Table rates created successfully........")
      self.conn.commit()
      self.conn.close()
   
   def insertToTabelRates(self):
      self.cursorObj("e_ratesdb")
      dataObj = Data()
      dataObj.generateReport(self.startDate, self.endDate)
      insert_stmt = '''INSERT INTO rates (currency, code, date, 
      value) VALUES (%s, %s, %s, %s)'''
      self.cursor.executemany(insert_stmt, dataObj.csvList)
      print("Data inserted to tabel rates........")
      self.conn.commit()
      self.conn.close()
   
   def createTabelBidAsk(self):
      self.cursorObj("e_ratesdb")
      sql ='''CREATE TABLE IF NOT EXISTS bidask       
      (
         bidask_id SERIAL NOT NULL PRIMARY KEY,
         currency VARCHAR(30),
         code VARCHAR(20),
         date Date,
         bid VARCHAR(20),
         ask VARCHAR(20)
      )'''
      self.cursor.execute(sql)
      print("Table bidask created successfully........")
      self.conn.commit()
      self.conn.close()
   
   def insertToTabelBidAsk(self):
      self.cursorObj("e_ratesdb")
      dataObj = Data()
      dataObj.NBPbidAsk()
      insert_stmt = '''INSERT INTO bidask (currency, code, date, 
      bid, ask) VALUES (%s, %s, %s, %s, %s)'''
      self.cursor.executemany(insert_stmt, dataObj.csvListWithAsk)
      print("Data inserted to tabel bidask........")
      self.conn.commit()
      self.conn.close()
   
   def updateDatabase(self):
      
      def getLastDate():
         self.cursorObj("e_ratesdb")
         self.cursor.execute('''SELECT MAX(date) FROM rates''') # SELECT MAX(DATE date) from e_ratesdb
         self.fetchDate = str(self.cursor.fetchall()[0][0])
         self.conn.close()
      
      self.cursorObj()
      self.conn.autocommit = True
      self.endDate =str(self.today)

      try:
         self.cursor.execute('''CREATE DATABASE e_ratesdb''')
         self.startDate = '2004-05-04'
         print("Database created successfully........")
         self.conn.close()
         self.createTabelRates()
         self.insertToTabelRates()
         self.createTabelBidAsk()
         self.insertToTabelBidAsk()
         getLastDate()
         self.logwin_quit()
      except psycopg2.errors.DuplicateDatabase:
         getLastDate()
         print(f"Database already exist (last update: {self.fetchDate})........")
         lastDBDate = (list(self.fetchDate.split('-')))
         convertDate = [int(i) for i in lastDBDate] 
         lastDBUpdate = datetime.date(convertDate[0], convertDate[1], convertDate[2])
         if lastDBUpdate < self.today:
            self.startDate = str(lastDBUpdate + datetime.timedelta(days=1))
            self.insertToTabelRates()
            self.insertToTabelBidAsk()
            print("Database updated........")
            self.logwin_quit()
         else:
            self.logwin_quit()
      
   def latestNBPreportDB(self):
      self.currencyList, self.codeList, self.valueList =[],[],[]
      self.cursorObj("e_ratesdb")
      self.cursor.execute('''SELECT rates_id, currency, code, value FROM rates WHERE date IN (SELECT MAX(date) FROM rates)''') 
      #print(self.cursor.fetchall())
      self.lastList = self.cursor.fetchall()
      #print(self.lastList)
      for t in self.lastList:
         self.currencyList.append(t[1])
         self.codeList.append(t[2])  
         self.valueList.append(t[3])  

      self.cursor.execute('''SELECT rates_id, currency, code, value FROM rates WHERE date IN (SELECT MAX(date)- INTERVAL '1 days' FROM rates)''') 
      self.lastListMinus1Day = self.cursor.fetchall()
      print(self.lastListMinus1Day)
      self.ratesUpDown = self.lastListMinus1Day + self.lastList
      self.conn.close()

      #del self.currencyList, self.codeList, self.valueList, self.lastList, self.lastListMinus1Day, self.ratesUpDown

   def NBPbidAskDB(self):
      pass



