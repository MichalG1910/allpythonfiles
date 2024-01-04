import psycopg2 # biblioteka postgres dla python 
import tkinter as tk
from tkinter import ttk
from functools import partial

class user:
   def __init__(self):
      self.win = tk.Tk()
      self.createWin()
      self.createFields()
      self.win.mainloop()
   ############################################### proste okno logowania #########################################
   def createWin(self):
      self.win.geometry('250x150+600+300')
   
   def validateLogin(self, username, password): # funkcja uruchamiająca tworzenie  bazy danych
      print("username entered :", username.get())
      print("password entered :", password.get())
      self.createDatabase()
      
   def createFields(self):
      self.username =  tk.StringVar()
      self.password =  tk.StringVar()
      self.validateLogin = partial(self.validateLogin, self.username, self.password) # klasa do sprawdzenia poprawności loginu i hasła

      userLabel = ttk.Label(self.win, text="username: ").grid(column=0, row=0, padx=10, pady=10)
      userEntry = ttk.Entry(self.win, textvariable=self.username).grid(column=1, row=0, padx=10, pady=10, sticky='nsew')
      passwordLabel = ttk.Label(self.win, text="password: " ).grid(column=0, row=1, padx=10, pady=10)
      passwordEntry = ttk.Entry(self.win, textvariable=self.password, show='*').grid(column=1, row=1, padx=10, pady=10, sticky='nsew') # show='*' - tekst wpisywany w polu entry zostanie wyświetlony jako * (przydatne do haseł, by nie były widoczne)
      loginButton = ttk.Button(self.win, text="Login", command=self.validateLogin, width=10).grid(column=1, row=2,  padx=10, pady=10, )
 ####################################################################################################################     
  
   def createDatabase(self): # funkcja tworząca bazę danych
      conn = psycopg2.connect(database="postgres", user=self.username.get(), password=self.password.get(), host='127.0.0.1', port= '5432') # tworzymy zmienną, ktora stabilizuje połączenie z serwerem Postgresem
      conn.autocommit = True # prawdopodobnie powoduje automatyczne zatwierzenie zmian w DB
      cursor = conn.cursor() # tworzymy obiekt cursor uzywając metody cursor()
      sqlQuery = '''CREATE database mydb'''; # zmienna przechowująca zapytanie w jezyku SQL (tworzące nową DB)
      cursor.execute(sqlQuery) # metoda wykonująca zapytanie w naszej zmiennej
      print("Database created successfully........")
      conn.close() # zamknięcie połączenia z serwerem postgres

logObj = user()

# Klasa kursora psycopg2 zapewnia różne metody wykonywania różnych poleceń PostgreSQL, pobierania rekordów i kopiowania danych. 
# Obiekt kursora można utworzyć za pomocą metody cursor() klasy Connection.
# Metoda execute() tej klasy przyjmuje zapytanie PostgreSQL jako parametr i wykonuje je.
# Dlatego, aby utworzyć bazę danych w PostgreSQL, wykonaj zapytanie CREATE DATABASE przy użyciu tej metody.