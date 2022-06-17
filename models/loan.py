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
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM Loan WHERE loan_id=?'
            result = cursor.execute(query, (loan_id,))
            row = result.fetchone()
        if row:
            return cls(*row)

    def insert(self):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            insert_query = 'INSERT INTO Loan VALUES(?, ?, ?, ?, ?)'
            cursor.execute(insert_query, (self.loan_id,self.loan_type, self.customer_id, self.amount, self.interest))
            conn.commit()

    def update(self):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            loan_update_query = 'UPDATE Loan SET loan_type = ?, customer_id = ?, amount = ?, interest = ? WHERE loan_id=?'
            cursor.execute(loan_update_query, (self.loan_type, self.customer_id, self.amount, self.interest, self.loan_id))
            conn.commit()

    @staticmethod
    def delete(loan_id):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            loan_delete_query = 'DELETE FROM Loan WHERE loan_id=?'
            cursor.execute(loan_delete_query, (loan_id,))
            conn.commit()
