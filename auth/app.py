from utils import decode_token
from flask import request, make_response, Flask
import json


app = Flask(__name__)

@app.route('/', methods=['GET'])
def authenticate():
    print("authenticating...")
    auth_header = request.headers.get('Authorization').split(' ')[1]
    if not auth_header:
        return make_response(json.dumps({'message': 'No authentication header'}), 403)
    user_id = decode_token(auth_header)
    if isinstance(user_id, int):
        print('token valid, user id is', user_id)
        return make_response(json.dumps({"message": user_id}), 200)
    else:
        print("auth fail")
        return make_response(json.dumps({"message": user_id}), 403)



