from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    sales = db.Column(db.BigInteger, nullable=False)
    developer = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, category, developer, sales=0):
        self.name = name
        self.category = category
        self.price = price
        self.sales = sales
        self.developer = developer
