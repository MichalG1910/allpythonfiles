import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432') 
cursor = conn.cursor()

cursor.execute("ALTER TABLE employee ADD COLUMN contact_id SERIAL NOT NULL ") # dodajemy kolumne do tabeli employee
print(cursor.fetchall())
conn.commit()

# tworzymy tabelę contact w DB 
sql ='''CREATE TABLE contact       
(
   contact_id SERIAL NOT NULL PRIMARY KEY,
   e_mail VARCHAR(50),
   city VARCHAR(50),
)'''
cursor.execute(sql)
print("Table created successfully........")
print(cursor.fetchall())
conn.commit() 

insert_stmt = '''INSERT INTO contact (e_mail, city) VALUES (%s, %s)''',
data = [('Krishna@email.com', 'Sharma'), 
   ('Raj@email.com', 'Kandukuri', ),
   ('Ramya@email.com', 'Ramapriya'),
   ('Mac@email.com', 'Mohan')]
cursor.executemany(insert_stmt, data)
print(cursor.fetchall())
conn.commit() 

# używamy JOIN do wyciągnięcia danych z obu tabel
cursor.execute('''SELECT * from employee AS e INNER JOIN contact As c ON e.contact_id = c.contact_id''')
print(cursor.fetchall())
conn.commit() 

conn.close()





