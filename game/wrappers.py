from functools import wraps
import requests
from flask import request, make_response

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("authenticating...")
        resp = requests.get('http://127.0.0.1:6000', headers=request.headers)
        if resp.status_code is 200:
            user_id = resp.json()['message']
            print('token valid, user id is', user_id)
            kwargs['id'] = user_id
            return func(*args, **kwargs)
        else:
            print("auth fail")
            return make_response(resp.json(), resp.status_code)
    return wrapper
