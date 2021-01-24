import sqlite3

def sql_connection():
    try:
        conn =sqlite3.connect('customer.db')
        return conn
    except:
        print("Error connecting database")
def sql_table(conn):
    cursor_obj =conn.cursor()
    #cursor_obj.execute("CREATE TABLE employees(id integer PRIMARY KEY,name text,salary real, department text,position text,hireDate text)")
    cursor_obj.execute("INSERT INTO employees VALUES(1,'Sarah',300000,'Research','Analyst','2020-01-19')")
    conn.commit()

conn = sql_connection()
sql_table(conn)


"""""CREATE TABLE patients(
user_id serial PRIMARY KEY,
username VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(50) NOT NULL,
email VARCHAR(355) UNIQUE NOT NULL,
signup TIMESTAMP NOT NULL,
minutesSpent time);
"""""


""""--SELECT COUNT (*) FROM city;
--SELECT COUNT (*) FROM customer;

---SELECT COUNT(email)
---FROM customer;

--SELECT COUNT(DISTINCT first_name)
--FROM customer;
--SELECT * FROM customer LIMIT 10;]

---SELECT first_name,email
--FROM customer
--ORDER BY first_name ASC LIMIT 10;

SELECT customer_id,amount 
FROM payment
ORDER BY amount DESC LIMIT 5;

--SELECT rental_id,amount
--FROM payment
--WHERE amount between 2.99 and 5.99

--SELECT amount,rental_id
--FROM payment
--WHERE rental_id between 2500 and 3000

--SELECT customer_id,rental_id,return_date
--FROM rental
--WHERE CUSTOMER_ID IN(1,2)
--ORDER BY customer_id


---SELECT first_name, last_name FROM customer WHERE last_name LIKE 'J%'


--SELECT COUNT (amount)
--FROM payment
--WHERE amount >5

--SELECT COUNT (DISTINCT(district))
--FROM address

--SELECT DISTINCT(district)
--FROM address

--SELECT count(*) FROM film WHERE title LIKE 'Truman%'
"""""""""""""""