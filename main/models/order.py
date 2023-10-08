from dataclasses import dataclass
from main.db import db
import datetime

@dataclass
class Order(db.Model):
    id: int = db.Column(db.Integer, primary_key = True)
    product_id: int = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)
    user_id: str = db.Column(db.String(100), db.ForeignKey('user.id'), nullable = False)
    status: str = db.Column(db.String(100), nullable = False)
    quantity: str = db.Column(db.Integer, nullable = False)
    order_date: str = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)
