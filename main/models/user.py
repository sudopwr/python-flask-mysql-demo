from dataclasses import dataclass
from main.db import db

@dataclass
class User(db.Model):
    id: int = db.Column(db.String(100), primary_key = True)
    name: str = db.Column(db.String(100), nullable = False)
    email: str = db.Column(db.String(100), nullable = False)
    image: str = db.Column(db.Text, nullable = False)
