import psycopg2, os, sys
import tkinter as tk
from tkinter import ttk
from functools import partial
from classE_Rates101_Data import Data

class Scenario:
   def __init__(self):
      self.win = tk.Tk()
      self.createWin()
      self.winStyle(self.win)
      self.createFields()
      self.win.mainloop()
   
   def createWin(self):
      self.win.geometry('320x250+600+300')
      self.win.title('E_Rates')
   
   def winStyle(self, window):
        window.tk.call('source', os.path.join(os.path.dirname(sys.argv[0]), 'azure.tcl'))
        window.tk.call("set_theme", "dark")
        
   
   def validateLogin(self, username, password):
      print("username entered :", username.get())
      print("password entered :", password.get())
      self.createDatabase()
      
   def createFields(self):
      self.username =  tk.StringVar()
      self.password =  tk.StringVar()
      self.noDBCheckVar = tk.IntVar()
      self.DBCheckVar = tk.IntVar()
      self.validateLogin = partial(self.validateLogin, self.username, self.password)

      scenarioFrame = ttk.LabelFrame(self.win, text='Wybierz tryb pracy programu', labelanchor="n", style='clam.TLabelframe',)
      scenarioFrame.grid(column=0, row=0, padx=23, ipadx=5, pady=10, sticky=tk.EW,)
      noDatabaseLabel = ttk.Label(scenarioFrame, text="pracuj w trybie bez bazy danych").grid(column=0, columnspan=1, row=0, padx=10, pady=10, sticky=tk.W)
      DatabaseLabel = ttk.Label(scenarioFrame, text="pracuj w trybie z bazą danych").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
      noDBCheckButton = ttk.Checkbutton(scenarioFrame, variable=self.noDBCheckVar ).grid(column=1, row=0, padx=10, pady=10, sticky=tk.E) # state= "disabled"
      DBCheckButton = ttk.Checkbutton(scenarioFrame, variable=self.DBCheckVar ).grid(column=1, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E) # state= "disabled"
      
      userLabel = ttk.Label(self.win, text="username: ").grid(column=0, row=2, padx=23, pady=10, sticky=tk.W)
      userEntry = ttk.Entry(self.win, textvariable=self.username).grid(column=0, row=2, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      passwordLabel = ttk.Label(self.win, text="password: " ).grid(column=0, row=3, padx=23, pady=10, sticky=tk.W)
      passwordEntry = ttk.Entry(self.win, textvariable=self.password, show='*').grid(column=0, row=3, padx=23, ipadx=20, pady=10, sticky=tk.NE)
      loginButton = ttk.Button(self.win, text="Login", command=self.validateLogin, width=10).grid(column=0, row=4,  padx=10, pady=10)
      
   def cursorObj(self):
      self.conn = psycopg2.connect(database="postgres", user=self.username.get(), password=self.password.get(), host='127.0.0.1', port= '5432')
      self.cursor = self.conn.cursor()
   
   def createDatabase(self):
      self.cursorObj()
      self.conn.autocommit = True
     
      sql = '''CREATE DATABASE IF NOT EXISTS mydb''';
      self.cursor.execute(sql)
      print("Database created successfully........")
      self.conn.close()
  
   def createTabel(self):
      self.cursorObj()
      sql ='''CREATE TABLE IF NOT EXISTS rates       
      (
         rates_id SERIAL NOT NULL PRIMARY KEY
         currency VARCHAR(20),
         code VARCHAR(20),
         value DECIMAL(10,8),
         date VARCHAR(10)
      )'''
      self.cursor.execute(sql)
      print("Table created successfully........")
      self.conn.commit()
      self.conn.close()

logObj = Scenario()
