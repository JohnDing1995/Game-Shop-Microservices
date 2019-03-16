import requests
from flask_restplus import Resource
from flask import Flask, jsonify, request

from game.common.util import authenticate
from game.models import Game as Game_Model
from game import db, ma


class GameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("name", "category", "developer", "price", "developer_name")

class Game(Resource):
    def get(self, id=-1):
        if id is -1:
            game = Game_Model.query.all()
            return GameSchema(many=True).jsonify(game)
        else:
            game = Game_Model.query.filter_by(id=id).first()
            developer_detail = requests.get("address/users/"+str(id), )
            return GameSchema().jsonify(game)




    # @authenticate
    def post(self, **kwargs):
        game_info = request.get_json()
        name = game_info.get('name')
        developer_id = 1
        category = game_info.get('category')
        price = game_info.get('price')
        new_game = Game_Model(name=name, category=category, developer=developer_id, price=price)
        db.session.add(new_game)
        db.session.commit()
        return jsonify({'message':'user created'})


