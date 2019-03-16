from flask import Flask
from flask_restplus import Api
from game.resources.game import Game
from game import db, app



api = Api(app)
api.add_resource(Game, '/games', '/games/<int:id>')
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)