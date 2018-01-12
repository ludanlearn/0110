from . import db

class Username(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(64))
    addresses = db.relationship('Adress', backref="user")

class Adress(db.Model):
    __tablename__ = 'adress'
    location = db.Column(db.String(64))