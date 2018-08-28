from hashlib import md5

from blackjack.app import db, login
from flask_login import UserMixin, current_user
from werkzeug.security import check_password_hash, generate_password_hash



class Player(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    chips = db.Column(db.Integer)
    games = db.relationship('Game', backref='player', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
	return Player.query.get(int(id))

