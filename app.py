from flask import Flask
from flask_restful import Api
from resources.customer import Customer, CustomerList
from resources.loan import Loan, LoanList, LoanTypeList
from resources.user import UserRegister, User
from flask_jwt import JWT
from security import authenticate, identity

app = Flask(__name__)
# Keep secret key in .env file and retrieve it from there
app.secret_key = 'non-public secret'
jwt = JWT(app, authenticate, identity)
api = Api(app)

api.add_resource(CustomerList, '/customers')
api.add_resource(Loan, '/loan/<loan_id>')
api.add_resource(LoanList, '/loans')
api.add_resource(LoanTypeList, '/loans/<loan_type>')
api.add_resource(UserRegister, '/user/register')
api.add_resource(User, '/users')
api.add_resource(Customer, '/customer/<customer_id>')
if __name__ == '__main__':
    app.run(port=5001, debug=True)
