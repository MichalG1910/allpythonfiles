import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("SELECT * from employee WHERE AGE < 23") # zapytanie SQL z klauzulą WHERE
print(cursor.fetchall())
'''
[('Vinay', 'Battacharya', 20, 'M', 6000.0), 
('Krishna', 'Sharma', 19, 'M', 2000.0), 
('Raj', 'Kandukuri', 20, 'M', 7000.0)]
'''
conn.commit()

cursor.execute("SELECT * from employee ORDER BY AGE") # zapytanie SQL z klauzulą ORDER BY
print(cursor.fetchall())
'''
[('Krishna', 'Sharma', 19, 'M', 2000.0), 
('Raj', 'Kandukuri', 20, 'M', 7000.0), 
('Vinay', 'Battacharya', 20, 'M', 6000.0), 
('Tripthi', 'Mishra', 24, 'F', 6000.0), 
('Ramya', 'Ramapriya', 25, 'M', 5000.0), 
('Sharukh', 'Sheik', 25, 'M', 8300.0), 
('Mac', 'Mohan', 26, 'M', 2000.0), 
('Sarmista', 'Sharma', 26, 'F', 10000.0), 
('Ramya', 'Rama priya', 27, 'F', 9000.0)]
'''
conn.commit()

cursor.execute("SELECT * from employee LIMIT 2 OFFSET 2") # zapytanie SQL z klauzulą LIMIT, OFFSET
print(cursor.fetchall())
'''
[('Sharukh', 'Sheik', 25, 'M', 8300.0), 
('Sarmista', 'Sharma', 26, 'F', 10000.0)]
'''
conn.commit()

conn.close()