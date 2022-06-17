import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.customer import CustomerModel


class Customer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='Name cannot be blank')

    def get(self, customer_id):
        customer = CustomerModel.find_by_id(customer_id)
        if customer:
            return customer.json()
        return {'message': f'No customer found with id {customer_id}'}

    @jwt_required()
    def post(self, customer_id):
        customer = CustomerModel.find_by_id(customer_id)
        if customer:
            return {'message': f'Customer with id {customer_id} already exists'}
        args = Customer.parser.parse_args()
        customer = CustomerModel(customer_id, args['name'])
        customer.insert()
        return customer.json(), 201

    @jwt_required()
    def put(self, customer_id):
        args = Customer.parser.parse_args()
        new_customer = CustomerModel(customer_id, args['name'])
        customer = CustomerModel.find_by_id(customer_id)
        if customer:
            new_customer.update()
            return new_customer.json()
        new_customer.insert()
        return new_customer.json(), 201

    @jwt_required()
    def delete(self, customer_id):
        customer = CustomerModel.find_by_id(customer_id)
        if customer:
            customer.delete()
            return {'message': f'Customer with id {customer_id} deleted'}
        return {'message': f'Customer with id {customer_id} does not exist'}


class CustomerList(Resource):
    @jwt_required()
    def get(self):
        with sqlite3.connect('finance.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM Customer'
            results = cursor.execute(query).fetchall()
            customers = []
            for customer in results:
                customers.append({'id': customer[0], 'name': customer[1]})
        return {'customers': customers}
