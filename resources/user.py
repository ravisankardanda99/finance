from flask_restful import Resource, reqparse
from models.user import UserModel
import sqlite3


class User(Resource):
    def get(self):
        con = sqlite3.connect('finance.db')
        cur = con.cursor()
        query = 'SELECT * FROM User'
        result = cur.execute(query)
        rows = result.fetchall()
        users = []
        for row in rows:
            users.append({'id': row[0], 'username': row[1], 'password': row[2]})
        return {'users': users}


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Username cannot be empty')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='password cannot be empty')

    def post(self):
        args = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(args['username'])
        if user:
            return {'message': 'User already exists'}
        UserModel.insert(**args)
        return args

