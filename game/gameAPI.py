import logging

from flask import request, jsonify
from flask_restplus import Resource, fields, Api, marshal_with
from sqlalchemy import exc
from .wrappers import authenticate
from .gameModel import Game,db


api = Api()
log = logging.getLogger(__name__)

game_ns = api.namespace('game/', description='Operations related to games')

game = api.model('Game', {
    'id': fields.String(required=True, description='The game id'),
    'name': fields.String(required=True, description='The game name'),
    'developer_id': fields.Integer(required=True, description='The game developer\'s id'),
    'price': fields.Float(required=True, description='The game\'s price'),
    'category': fields.String(required=False, description='The game\'s category')
})

create_success = {
    'message': fields.String,
    'status': fields.String,
    'game_id': fields.Integer
}


@game_ns.route('/')
@game_ns.doc()
class GameList(Resource):
    @game_ns.doc('list_games')
    @game_ns.marshal_list_with(game)
    def get(self):
        '''List all games'''
        games = Game.query.all()
        return games

    @game_ns.doc('put games')
    @game_ns.expect(fields=game)
    @marshal_with(create_success, skip_none=True)
    @authenticate
    def post(self):
        post_data = request.get_json()
        if not post_data:
            response_object = {
                'status': 'error',
                'message': 'Invalid payload.'
            }
            return jsonify(response_object), 400

        game_name = post_data.get('name')
        developer_id = post_data.get('developer_id')
        price = post_data.get('price')
        category = post_data.get('category')
        log.info("game_name:",game_name, "developer_id", developer_id, "price", price, "category", category)
        print("game_name:",game_name, "developer_id", developer_id, "price", price, "category", category)
        try:
            existed_game = Game.query.filter_by(name=game_name).first()
            if not existed_game:
                new_game = Game(
                    name=game_name,
                    developer=developer_id,
                    category=category,
                    price=price
                )
                db.session.add(new_game)
                db.session.commit()
                response_object = {
                    'status':'success',
                    'message':'New game added',
                    'game_id': int(Game.query.filter_by(name=game_name).first().id)
                }
                print(response_object)
                return response_object
            else:
                return {'status':'error', 'message':'duplicated game name not allowed'}
        except (exc.IntegrityError, ValueError, TypeError) as e:
            db.session().rollback()
            print(e)
            response_object = {
                'status': 'error',
                'message': str(e)
            }
            return response_object, 400






@game_ns.route('/<int:id>')
@game_ns.doc(params={'id':'Game ID'})
class GameID(Resource):
    @game_ns.doc('get game by id')
    @game_ns.marshal_with(game)
    def get(self, id):
        game = Game.query.filter_by(id=id).first()
        return game



