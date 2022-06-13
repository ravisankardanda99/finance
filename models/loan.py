import sqlite3


class LoanModel:
    def __init__(self, loan_id, loan_type, customer_id, amount, interest):
        self.loan_id = loan_id
        self.loan_type = loan_type
        self.customer_id = customer_id
        self.amount = amount
        self.interest = interest

    def json(self):
        return {'loan_id': self.loan_id,
                'loan_type': self.loan_type,
                'customer_id': self.customer_id,
                'amount': self.amount,
                'interest': self.interest}

    @classmethod
    def find_by_loan_id(cls, loan_id):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM Loan WHERE loan_id=?'
        result = cursor.execute(query, (loan_id,))
        row = result.fetchone()
        connection.close()
        if row:
            return cls(*row)

    def insert(self):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        insert_query = 'INSERT INTO Loan VALUES(?, ?, ?, ?, ?)'
        cursor.execute(insert_query, (self.loan_id,self.loan_type, self.customer_id, self.amount, self.interest))
        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        loan_update_query = 'UPDATE Loan SET loan_type = ?, customer_id = ?, amount = ?, interest = ? WHERE loan_id=?'
        cursor.execute(loan_update_query, (self.loan_type, self.customer_id, self.amount, self.interest, self.loan_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(loan_id):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        loan_delete_query = 'DELETE FROM Loan WHERE loan_id=?'
        cursor.execute(loan_delete_query, (loan_id,))
        connection.commit()
        connection.close()
