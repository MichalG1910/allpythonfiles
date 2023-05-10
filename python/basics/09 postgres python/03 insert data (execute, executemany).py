import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
conn.autocommit = False # wyłączamy automatyczne zatwierdzanie zmian w DB
cursor = conn.cursor()

# zapytania SQL dodające dane do naszej tabeli employee
cursor.execute('''INSERT INTO employee(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')
cursor.execute('''INSERT INTO employee(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
cursor.execute('''INSERT INTO employee(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
cursor.execute('''INSERT INTO employee(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
cursor.execute('''INSERT INTO employee(FIRST_NAME, LAST_NAME, AGE, SEX,
    INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

# konstrukcja z executemany(), która dodaje wiele wierszy do naszej tabeli w jednym bloku
insert_stmt = '''INSERT INTO employee (FIRST_NAME, LAST_NAME, AGE, SEX, 
    INCOME) VALUES (%s, %s, %s, %s, %s)''',
data = [('Krishna', 'Sharma', 19, 'M', 2000), 
   ('Raj', 'Kandukuri', 20, 'M', 7000),
   ('Ramya', 'Ramapriya', 25, 'M', 5000),
   ('Mac', 'Mohan', 26, 'M', 2000)]
cursor.executemany(insert_stmt, data) # executemany(zapytanie, dane do zapytania)

conn.commit()
print("Records inserted........")
conn.close()