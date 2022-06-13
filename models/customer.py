import sqlite3


class CustomerModel:
    def __init__(self, customer_id, name):
        self.id = customer_id
        self.name = name

    def json(self):
        return {'id': self.id, 'name': self.name}

    @classmethod
    def find_by_id(cls, customer_id):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM Customer WHERE customer_id=?'
        result = cursor.execute(query, (customer_id,))
        row = result.fetchone()
        if row:
            return cls(*row)

    def insert(self):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        insert_query = 'INSERT INTO Customer VALUES(?, ?)'
        cursor.execute(insert_query, (self.id, self.name))
        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        loan_update_query = 'UPDATE Customer SET name = ? WHERE customer_id=?'
        cursor.execute(loan_update_query, (self.name, self.id))
        connection.commit()
        connection.close()

    def delete(self):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        loan_delete_query = 'DELETE FROM Customer WHERE customer_id=?'
        cursor.execute(loan_delete_query, (self.id,))
        connection.commit()
        connection.close()
