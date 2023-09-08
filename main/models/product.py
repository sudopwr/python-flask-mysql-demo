from dataclasses import dataclass
from main.db import db

@dataclass
class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key = True)
    name: str = db.Column(db.String(100), nullable = False)
    description: str = db.Column(db.Text, nullable = False)
    price: str = db.Column(db.Double, nullable = False)
    quantity: str = db.Column(db.Integer, nullable = False)
    image: str = db.Column(db.Text, nullable = False)
