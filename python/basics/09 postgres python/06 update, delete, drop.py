import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
conn.autocommit = True
cursor = conn.cursor()

#Fetching all the rows before the update - tabela przed operacją update
print("Contents of the employee table: ") 
sql = '''SELECT * from employee'''# pobieram dane z tabeli przy pomocy zapytania SELECT (do zmiennej sql)
cursor.execute(sql)
print(cursor.fetchall())

sql = "UPDATE employee SET AGE = AGE + 1 WHERE SEX = 'M'" # zapytanie dokonuje aktualizacji w tabeli przy pomocy klauzuli UPDATE 
cursor.execute(sql)
print("Table updated...... ")
#Fetching all the rows after the update - tabela po operacji update
print("Contents of the employee table after the update operation: ")
sql = '''SELECT * from employee'''
cursor.execute(sql)
print(cursor.fetchall())
conn.commit()

cursor.execute('''DELETE FROM employee WHERE AGE > 25''') # zapytanie dokonuje udunięcia wierszy, w których AGE > 25 prz pomocy klauzuli DELETE 
#Retrieving data after delete tabela po operacji DELETE
print("Contents of the table after delete operation ")
cursor.execute("SELECT * from employee")
print(cursor.fetchall())
conn.commit()

conn.close()

# cursor.execute("DROP TABLE empployee") - usunięcie całej tabeli employee