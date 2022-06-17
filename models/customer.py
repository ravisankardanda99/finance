import sqlite3


class CustomerModel:
    def __init__(self, customer_id, name):
        self.id = customer_id
        self.name = name

    def json(self):
        return {'id': self.id, 'name': self.name}

    @classmethod
    def find_by_id(cls, customer_id):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM Customer WHERE customer_id=?'
            result = cursor.execute(query, (customer_id,))
            row = result.fetchone()
        if row:
            return cls(*row)

    def insert(self):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            insert_query = 'INSERT INTO Customer VALUES(?, ?)'
            cursor.execute(insert_query, (self.id, self.name))
            conn.commit()

    def update(self):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            loan_update_query = 'UPDATE Customer SET name = ? WHERE customer_id=?'
            cursor.execute(loan_update_query, (self.name, self.id))
            conn.commit()

    def delete(self):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            loan_delete_query = 'DELETE FROM Customer WHERE customer_id=?'
            cursor.execute(loan_delete_query, (self.id,))
            conn.commit()
