from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(10), unique=True)
    original_url = db.Column(db.String(255), nullable=False)
