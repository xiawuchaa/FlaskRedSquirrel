from Apps.models.user.user_model import User


def get_user(user_ident):

    if not user_ident:
        return None

    user = User.query.get(user_ident)

    if user:
        return user

    user = User.query.filter(User.phone == user_ident).first()

    if user:
        return user

    user = User.query.filter(User.username == user_ident).first()

    if user:
        return user

    return None

import uuid

USER = "user"
ADMIN_USER = "admin_user"
CINEMA_USER = "cinema_user"
# 生成token
def generate_token(prefix=None):
    token = prefix + uuid.uuid4().hex
    return token

def generate_user_token():
    return generate_token(prefix=MOVIE_USER)

def generate_admin_user_token():
    return generate_token(prefix=ADMIN_USER)

def generate_cinema_user_token():
    return generate_token(prefix=CINEMA_USER)
