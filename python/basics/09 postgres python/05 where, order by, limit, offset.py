import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("SELECT * from employee WHERE AGE < 23") # zapytanie SQL z klauzulą WHERE
print(cursor.fetchall())
conn.commit()

cursor.execute("SELECT * from employee ORDER BY AGE") # zapytanie SQL z klauzulą ORDER BY
print(cursor.fetchall())
conn.commit()

cursor.execute("SELECT * from employee LIMIT 2 OFFSET 2") # zapytanie SQL z klauzulą LIMIT, OFFSET
print(cursor.fetchall())
conn.commit()

conn.close()