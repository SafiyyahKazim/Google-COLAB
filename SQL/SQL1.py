import sqlite3
​
def sql_connection():
  try:
    conn = sqlite3.connect('test.db')
    print('Connection successful')
    return conn
  except:
    print('Error connecting to database')
​

def create_table(conn):
    try:
        cursor = conn.cursor()
        stmt = '''CREATE TABLE employees(id INTEGER PRIMARY KEY,
                                         name VARCHAR(255),
                                         salary integer,
                                         department VARCHAR(255),
                                         position VARCHAR(255),
                                         hireDate VARCHAR(255));'''
        cursor.execute(stmt)
        conn.commit()
        print('Table Created')
    except:
        print('An error occurred when creating the table')
​
def insert_to_table(conn, entry):
    try:
        cursor = conn.cursor()
        stmt = '''INSERT INTO employees(name, salary, department, position, hireDate) VALUES(?,?,?,?,?);'''
        cursor.execute(stmt, entry)
        conn.commit()
        print('Insertion successful')
    except:
        print('Insertion failed')
​
conn = sql_connection()
create_table(conn)
for i in range(10):
    name = input('Enter your name: ')
    dept = input('Enter your department: ')
    pos = input('Enter your position: ')
    entry = (name, 50000, dept, pos, '2021-01-21')
    insert_to_table(conn, entry)
​
conn.close()
​
"""
CREATE TABLE patients(
patientID SERIAL PRIMARY KEY,
firstName VARCHAR(25),
lastName VARCHAR(25) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
signup TIMESTAMP NOT NULL,
minutesSpent TIME);
"""