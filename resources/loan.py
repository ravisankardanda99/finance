import sqlite3
from flask_restful import Resource, reqparse
from models.loan import LoanModel
from flask_jwt import jwt_required


class Loan(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('loan_type',
                        type=str,
                        required=True,
                        help="This field cannot be empty"
                        )
    parser.add_argument('customer_id',
                        type=int,
                        required=True,
                        help="This field cannot be empty"
                        )
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help="This field cannot be empty"
                        )
    parser.add_argument('interest',
                        type=float,
                        required=True,
                        help="This field cannot be empty"
                        )

    def get(self, loan_id):
        loan = LoanModel.find_by_loan_id(loan_id)
        if loan:
            return loan.json()
        return {'message': 'loan not found'}, 404

    @jwt_required()
    def post(self, loan_id):
        if LoanModel.find_by_loan_id(loan_id):
            return {'message': f'Loan with {loan_id} already exists'}
        args = Loan.parser.parse_args()
        loan = LoanModel(loan_id, args['loan_type'], args['customer_id'], args['amount'], args['interest'])
        try:
            loan.insert()
        except:
            return {'message': 'An error occurred inserting loan.'}, 504
        return loan.json(), 201

    @jwt_required()
    def put(self, loan_id):
        args = Loan.parser.parse_args()
        loan = LoanModel(loan_id, args['loan_type'], args['customer_id'], args['amount'], args['interest'])
        if LoanModel.find_by_loan_id(loan_id):
            loan.update()
            return loan.json()
        try:
            print('I am here')
            loan.insert()
        except:
            return {'message': 'An error occurred inserting loan.'}, 504
        return loan.json(), 201

    @jwt_required()
    def delete(self, loan_id):
        if LoanModel.find_by_loan_id(loan_id):
            LoanModel.delete(loan_id)
            return {'message': 'Loan deleted successfully'}
        return {'message': f'There is no loan with loan_id {loan_id}'}


class LoanList(Resource):
    def get(self):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM Loan'
            results = cursor.execute(query)
            loans = []
            for row in results:
                loans.append(
                    {'loan_id': row[0], 'loan_type': row[1], 'customer_id': row[2], 'amount': row[3], 'interest': row[4]})
        return {'loans': loans}


class LoanTypeList(Resource):
    def get(self, loan_type):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM Loan WHERE loan_type=?'
            results = cursor.execute(query, (loan_type,))
            loans = []
            for row in results:
                loans.append(
                    {'loan_id': row[0], 'loan_type': row[1], 'customer_id': row[2], 'amount': row[3], 'interest': row[4]})
        return {'loans': loans}