import psycopg2
import tkinter as tk
from tkinter import ttk
from functools import partial

class user:
   def __init__(self):
      self.win = tk.Tk()
      self.createWin()
      self.createFields()
      self.win.mainloop()
   
   def createWin(self):
      self.win.geometry('300x150+600+300')
   
   def validateLogin(self, username, password):
      print("username entered :", username.get())
      print("password entered :", password.get())
      self.createDatabase()
      
   def createFields(self):
      self.username =  tk.StringVar()
      self.password =  tk.StringVar()
      self.validateLogin = partial(self.validateLogin, self.username, self.password)

      userLabel = ttk.Label(self.win, text="username: ").grid(column=0, row=0, padx=10, pady=10)
      userEntry = ttk.Entry(self.win, textvariable=self.username, width=30).grid(column=1, row=0, padx=10, pady=10)
      passwordLabel = ttk.Label(self.win, text="password: " ).grid(column=0, row=1, padx=10, pady=10)
      passwordEntry = ttk.Entry(self.win, textvariable=self.password, show='*', width=30).grid(column=1, row=1, padx=10, pady=10)
      loginButton = ttk.Button(self.win, text="Login", command=self.validateLogin, width=10).grid(column=1, row=2,  padx=10, pady=10, )
      
   #establishing the connection
   def createDatabase(self):
      conn = psycopg2.connect(database="postgres", user=self.username, password=self.password, host='127.0.0.1', port= '5432')
      conn.autocommit = True
      #Creating a cursor object using the cursor() method
      cursor = conn.cursor()
      #Preparing query to create a database
      sql = '''CREATE database mydb''';
      #Creating a database
      cursor.execute(sql)
      print("Database created successfully........")
      #Closing the connection
      conn.close()

logObj = user()
