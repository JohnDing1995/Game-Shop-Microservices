from flask import Blueprint, jsonify

from user.models import User
from user.utils import authenticate

users_blueprint = Blueprint('user', __name__, url_prefix='/users')


@users_blueprint.route('/me', methods=['GET'])
@authenticate
def get_my_info(user_id):
    my = User.query.filter_by(id=user_id).first()
    if my is None:
        return jsonify({'message': 'user not exists'}), 404
    else:
        return jsonify({'id': my.id,
                        'email': my.email,
                        'name': my.username}), 200
