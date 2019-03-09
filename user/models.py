import datetime

import jwt

from . import db, bcrypt
from sqlalchemy import Column, Integer, String

JWT_EXP_DELTA_MINS = 30
JWT_SECRET = 'thesecretoflogin'
JWT_ALGORITHM = 'HS256'
ENCRYPT_ROUND = 6


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    is_active = Column(db.Boolean, default=False)
    created_at = Column(db.DateTime, nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, username, email, password, is_active = False, created_at = datetime.datetime.utcnow()):
        self.username = username
        self.email = email
        self.is_active = is_active
        self.created_at = created_at
        self.password = bcrypt.generate_password_hash(
            password, ENCRYPT_ROUND).decode()

    def encode_token(self):
        payload = {
            'user_id': self.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXP_DELTA_MINS)
        }
        try:
            jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
            return jwt_token
        except Exception as e:
            return e

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, JWT_SECRET)
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
#
# def init_db():
#     db.create_all()
#     new_user = User('test', 'a@a.com', '123')
#     db.session.add(new_user)
#     db.session.commit()
#
#     new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
#     db.session.commit()
#
# if __name__ == '__main__':
#     init_db()
