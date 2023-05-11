import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432') 
cursor = conn.cursor()

cursor.execute("ALTER TABLE employee ADD COLUMN contact_id SERIAL NOT NULL ") # dodajemy kolumne do tabeli employee (dzięki typowi SERIAL zostanie ona automatycznie wypełniona kolejnymi numerami)
cursor.execute("SELECT * from employee")
print(cursor.fetchall())
conn.commit()

# tworzymy tabelę contact w DB 
sql ='''CREATE TABLE contact       
(
   contact_id SERIAL NOT NULL PRIMARY KEY,
   e_mail VARCHAR(50),
   city VARCHAR(50)
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit() 

insert_stmt = '''INSERT INTO contact (e_mail, city) VALUES (%s, %s)'''
data = [('Tripthi@email.com', 'Bombaj'), 
   ('Vinay@email.com', 'Delhi', ),
   ('Krishna@email.com', 'Kalkuta'),
   ('Raj@email.com', 'New York')]
cursor.executemany(insert_stmt, data)
conn.commit() 

# używamy JOIN do wyciągnięcia danych z obu tabel
cursor.execute('''SELECT * from employee AS e INNER JOIN contact As c ON e.contact_id = c.contact_id''')
print(cursor.fetchall())
'''
[('Tripthi', 'Mishra', 24, 'F', 6000.0, 1, 1, 'Tripthi@email.com', 'Bombaj'), 
('Vinay', 'Battacharya', 21, 'M', 6000.0, 2, 2, 'Vinay@email.com', 'Delhi'), 
('Krishna', 'Sharma', 20, 'M', 2000.0, 3, 3, 'Krishna@email.com', 'Kalkuta'), 
('Raj', 'Kandukuri', 21, 'M', 7000.0, 4, 4, 'Raj@email.com', 'New York')]
'''
conn.commit() 

conn.close()





