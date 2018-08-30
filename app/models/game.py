from blackjack.app import db
from blackjack.app.models.player import Player
from blackjack.app.models.deck import CardSet, Deck, Hand

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    deck_id = db.Column(db.Integer)
    deck = db.relationship('CardSet',enable_typechecks=False,foreign_keys=[deck_id],primaryjoin='Game.deck_id==CardSet.id')
    player_hand_id = db.Column(db.Integer)
    player_hand = db.relationship('CardSet',enable_typechecks=False,foreign_keys=[player_hand_id],primaryjoin='Game.player_hand_id==CardSet.id')
    #dealer_hand_id = db.Column(db.Integer, db.ForeignKey('d.id'))
    bet_pool = db.Column(db.Integer)
    current_bet = db.Column(db.Integer)
