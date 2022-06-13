# loan = {'loan_type': 'personal', 'customer_id': 1, 'amount': 70000.0, 'interest': 10.0}
# print(*loan.values())


# class LoanModel:
#     def __init__(self, loan_id, loan_type, customer_id, amount, interest):
#         self.loan_id = loan_id
#         self.loan_type = loan_type
#         self.customer_id = customer_id
#         self.amount = amount
#         self.interest = interest
#
#     def json(self):
#         return {'loan_id': self.loan_id,
#                 'loan_type': self.loan_type,
#                 'customer_id': self.customer_id,
#                 'amount': self.amount,
#                 'interest': self.interest}
#
#
# loan = LoanModel(1, 'personal', 1, 70000, 10)
# print(loan.json())

# from functools import wraps
# import sqlite3
#
#
# def db_connect(f):
#     @wraps(f)
#     def wrapper(*args):
#         print('Inside decorator')
#         f(*args)
#     return wrapper
#
# @db_connect
# def func(a):
#     print(a)
#
# func('HIFI')
