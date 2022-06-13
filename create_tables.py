import sqlite3

connection = sqlite3.connect('finance.db')
cursor = connection.cursor()
create_users = 'CREATE TABLE User(id INTEGER primary key, username text, password text)'
cursor.execute(create_users)
create_loan = 'CREATE TABLE Loan(loan_id int , loan_type text, customer_id int, amount real, interest real)'
cursor.execute(create_loan)
print('Created Loan table successfully')
create_customer = 'CREATE TABLE Customer(customer_id INTEGER PRIMARY KEY, name text)'
cursor.execute(create_customer)
print('Created Customer table successfully')
customers = [
    (1, 'ravi'),
    (2, 'sankar'),
    (3, 'danda')
]
customer_insert = 'INSERT INTO Customer VALUES(?, ?)'
cursor.executemany(customer_insert, customers)
print('Inserted values into Customer table')
query = 'SELECT * FROM Customer'
results = cursor.execute(query)
customers = []
for customer in results:
    customers.append({'id': customer[0], 'name': customer[1]})
print(customers)

connection.commit()
connection.close()
