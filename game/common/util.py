from functools import wraps

import jwt
from flask import request, make_response
from flask_restful.representations import json

JWT_SECRET = 'thesecretoflogin'

def decode_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET)
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("authenticating...")
        auth_header = request.headers.get('Authorization').split(' ')[1]
        if not auth_header:
            return make_response(json.dumps({'message':'No authentication header'}), 403)
        user_id = decode_token(auth_header)
        if isinstance(user_id, int):
            print('token valid, user id is', user_id)
            kwargs['id'] = user_id
            return func(*args, **kwargs)
        else:
            print("auth fail")
            return make_response(json.dumps({"message": user_id}), 403)
    return wrapper


