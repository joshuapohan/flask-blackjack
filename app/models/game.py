from blackjack.app import db
from blackjack.app.models.player import Player

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_hand = db.Column(db.Text())
    dealer_hand = db.Column(db.Text())
    deck = db.Column(db.Text())
    bet_pool = db.Column(db.Integer)
    current_bet = db.Column(db.Integer)
