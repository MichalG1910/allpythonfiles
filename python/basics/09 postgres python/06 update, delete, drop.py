import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='pssword', host='127.0.0.1', port= '5432')
conn.autocommit = True
cursor = conn.cursor()

#Fetching all the rows before the update - tabela przed operacją update
print("Contents of the employee table: ") 
sql = '''SELECT * from employee'''# pobieram dane z tabeli przy pomocy zapytania SELECT (do zmiennej sql)
cursor.execute(sql)
print(cursor.fetchall())
'''
[('Ramya', 'Rama priya', 27, 'F', 9000.0), 
('Vinay', 'Battacharya', 20, 'M', 6000.0), 
('Sharukh', 'Sheik', 25, 'M', 8300.0), 
('Sarmista', 'Sharma', 26, 'F', 10000.0), 
('Tripthi', 'Mishra', 24, 'F', 6000.0), 
('Krishna', 'Sharma', 19, 'M', 2000.0), 
('Raj', 'Kandukuri', 20, 'M', 7000.0), 
('Ramya', 'Ramapriya', 25, 'M', 5000.0), 
('Mac', 'Mohan', 26, 'M', 2000.0)]
'''

sql = "UPDATE employee SET AGE = AGE + 1 WHERE SEX = 'M'" # zapytanie dokonuje aktualizacji w tabeli przy pomocy klauzuli UPDATE 
cursor.execute(sql)

print("Table updated...... ")
#Fetching all the rows after the update - tabela po operacji update
print("Contents of the employee table after the update operation: ")
sql = '''SELECT * from employee'''
cursor.execute(sql)
print(cursor.fetchall())
'''
[('Ramya', 'Rama priya', 27, 'F', 9000.0), 
('Sarmista', 'Sharma', 26, 'F', 10000.0), 
('Tripthi', 'Mishra', 24, 'F', 6000.0), 
('Vinay', 'Battacharya', 21, 'M', 6000.0), 
('Sharukh', 'Sheik', 26, 'M', 8300.0), 
('Krishna', 'Sharma', 20, 'M', 2000.0), 
('Raj', 'Kandukuri', 21, 'M', 7000.0), 
('Ramya', 'Ramapriya', 26, 'M', 5000.0), 
('Mac', 'Mohan', 27, 'M', 2000.0)]
'''
conn.commit()

cursor.execute('''DELETE FROM employee WHERE AGE > 25''') # zapytanie dokonuje udunięcia wierszy, w których AGE > 25 prz pomocy klauzuli DELETE 
#Retrieving data after delete tabela po operacji DELETE
print("Contents of the table after delete operation ")
cursor.execute("SELECT * from employee")
print(cursor.fetchall())
'''
[('Tripthi', 'Mishra', 24, 'F', 6000.0), 
('Vinay', 'Battacharya', 21, 'M', 6000.0), 
('Krishna', 'Sharma', 20, 'M', 2000.0), 
('Raj', 'Kandukuri', 21, 'M', 7000.0)]
'''
conn.commit()

conn.close()

# cursor.execute("DROP TABLE empployee") - usunięcie całej tabeli employee