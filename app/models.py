from app.init_app import db

class User(db.Model):

    def __init__(self):
        id = db.Column(db.Integer, primary_key=True)
        uEmail = db.Column(db.String(120), index=True, unique=True)
        pURL = db.Column(db.String(128))

    def __repr__(self):     # This method defines how objects should be printed
        return '<User {}>'.format(self.username)
