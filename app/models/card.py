from blackjack.app.models.cardtypes import CardSuit, CardRanks
from blackjack.app.models.deck import CardSet, Deck, Hand
from blackjack.app import db

class Card(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    deck_id = db.Column(db.Integer, enable_typechecks=False,db.ForeignKey('cardset.id'))
    rank = db.Column(db.Enum(CardRanks))
    suit = db.Column(db.Enum(CardSuit))

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if not (self.rank == CardRanks.Ace or self.rank == CardRanks.Jack or self.rank == CardRanks.Queen or self.rank == CardRanks.King):
            cardvalue = self.rank.value
        else:
            cardvalue = self.rank.name
        return str(cardvalue) + ' ' + self.suit.name

    def __repr__(self):
        return self.rank.name + ' ' + self.suit.name

    def as_json(self):
        return {'Card': self.__str__()}
