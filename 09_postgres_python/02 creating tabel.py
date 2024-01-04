import psycopg2

conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432') # korzystamy z DB "mydb", utworzonej według instrukcji 01
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employee") # jeśli tabela "employee" istnieje, zostanie usunięta 
# tworzymy zapytanie SQL tworzące tabele employee z kolumnami jak niżej
sql ='''CREATE TABLE employee       
(
   FIRST_NAME VARCHAR(20) NOT NULL,
   LAST_NAME VARCHAR(20),
   AGE INT,
   SEX VARCHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit() # zatwierdzamy

conn.close()