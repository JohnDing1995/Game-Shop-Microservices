from flask_restplus import Resource, fields, Api

from .gameModel import Game


api = Api()

game = api.model('Game', {
    'id': fields.String(required=True, description='The game id'),
    'name': fields.String(required=True, description='The game name'),
    'developer_id': fields.String(required=True, description='The game developer\'s name'),
    'price': fields.Float(required=True, description='The game\'s price'),
    'category': fields.String(required=False, description='The game\'s category')
})


@api.route('/')
class GameList(Resource):
    @api.doc('list_games')
    @api.marshal_list_with(game)
    def get(self):
        '''List all games'''
        games = Game.query.all()
        return games