import sqlite3
from decorators import db_connect


class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def json(self):
        return {'id': self.id, 'username': self.username, 'password': self.password}

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM User WHERE username = ?'
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        connection.close()
        if row:
            return cls(*row)

    @classmethod
    def find_by_user_id(cls, user_id):
        connection = sqlite3.connect('finance.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM User WHERE id = ?'
        result = cursor.execute(query, (user_id,))
        row = result.fetchone()
        if row:
            return cls(*row)

    @staticmethod
    @db_connect
    def insert(username, password):
        query = 'INSERT INTO User(username, password) VALUES (?, ?)'
        cursor.execute(query, (username, password))


