from functools import wraps
from flask import request, jsonify
from user.models import User

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization').split(' ')[1]
        print(auth_header)
        if not auth_header:
            return jsonify({'message':'No request header'}), 403
        user_id = User.decode_token(auth_header)
        print(user_id)
        if isinstance(user_id, int):
            user = User.query.filter_by(id=user_id).first()
            if not user or not user.active:
                return jsonify({'message':user_id}), 401
        else:
            return jsonify({'message': user_id}), 401
        return func(user_id, *args, **kwargs)
    return wrapper






