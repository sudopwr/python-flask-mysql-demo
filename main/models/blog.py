from main.db import db

class Blog(db.Model):
    id: int = db.Column(db.Integer, primary_key = True)
    title: str = db.Column(db.String(100), nullable = False)
    content: str = db.Column(db.Text, nullable = False)
