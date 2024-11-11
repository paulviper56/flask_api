from extensions import db
from dataclasses import dataclass


#because flask does not know how to serialize, dataclass from dataclasses is used to specify the datatype of the field
@dataclass
class users(db.Model):
    id : int
    name : str
    email : str
    age : int

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(220), nullable=True)
    email = db.Column(db.String(120), nullable=True, unique=True)
    age = db.Column(db.Integer, nullable=True)
