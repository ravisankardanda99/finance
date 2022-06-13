from models.user import UserModel


def authenticate(username, password):

    user_obj = UserModel.find_by_username(username)
    if user_obj and password == user_obj.password:
        return user_obj


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_user_id(user_id)
