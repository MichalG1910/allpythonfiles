# Możesz pobrać dane z PostgreSQL za pomocą metody fetch() dostarczonej przez psycopg2.
# Klasa Cursor udostępnia trzy metody: fetchall(), fetchmany() i fetchone() gdzie:
# fetchall() - metoda pobiera wszystkie wiersze w zbiorze wyników zapytania i zwraca je jako listę krotek. (Jeśli wykonamy to po pobraniu kilku wierszy, zwróci pozostałe).
# fetchone() - metoda pobiera następny wiersz w wyniku zapytania i zwraca go jako krotkę.
# fetchmany() - metoda jest podobna do metody fetchone(), ale zamiast pojedynczego wiersza pobiera następny zestaw wierszy z zestawu wyników zapytania.
import psycopg2


conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
conn.autocommit = True
cursor = conn.cursor()
cursor.execute('''SELECT * from employee''') # zapytanie SQL zwracające wszystkie kolumny tabeli employee

result = cursor.fetchone(); # fetchone() - metoda pobiera następny wiersz w wyniku zapytania i zwraca go jako krotkę.
print(result) # ('Ramya', 'Rama priya', 27, 'F', 9000.0)
print()
result = cursor.fetchall(); # fetchall() - metoda pobiera wszystkie wiersze w zbiorze wyników zapytania i zwraca je jako listę krotek. (Jeśli wykonamy to po pobraniu kilku wierszy, zwróci pozostałe).
print(result) 
''' [('Vinay', 'Battacharya', 20, 'M', 6000.0),
    ('Sharukh', 'Sheik', 25, 'M', 8300.0),
    ('Sarmista', 'Sharma', 26, 'F', 10000.0),
    ('Tripthi', 'Mishra', 24, 'F', 6000.0)]
'''

conn.commit()
conn.close()