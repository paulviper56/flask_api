'''users = [
    {"id":1,"name":"samuel","email":"nnannasam@gmail.com","Age":25},
    {"id":2,"name":"uloma","email":"uloma@gmail.com","Age":20},
    {"id":3,"name":"oluchi","email":"oluchi@gmail.com","Age":18},
    {"id":4,"name":"borito","email":"borito@gmail.com","Age":9}

]'''
from app1 import db
class users(db.Model):
    id = db.Column(db.Integer, primary=True)
    name = db.Column(db.String(220), nullable=True)
    email = db.Column(db.String(120), nullable=True, unique=True)
    Age = db.Column(db.Integer, nullable=True)