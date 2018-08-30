from flask import jsonify
from random import shuffle

#from blackjack.app.models.card import Card
from blackjack.app.models.cardtypes import CardSuit, CardRanks
from blackjack.app import db


class CardSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cards = db.relationship('Card',enable_typechecks=False, lazy='dynamic')
    #game = db.relationship('Game', backref='cardset', lazy='dynamic')
    #game = db.Column(db.Integer, db.ForeignKey('game.id'))


class Card(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    deck_id = db.Column(db.Integer, db.ForeignKey('card_set.id'))
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

class Deck(CardSet, db.Model):

    def __init__(self):
        self.cards = []

        temp_cards = []

        #suit_list = list(shuffle([x for x in CardSuit]))
        #rank_list = list(shuffle([x for x in CardRanks]))
        
        #for i,j in zip(suit_list, rank_list):
        #        current_card = Card(j,i)
        #        self.cards.append(current_card)

        for i in CardSuit:
            for j in CardRanks:
                current_card = Card(j,i)
                temp_cards.append(current_card)
        shuffle(temp_cards)

        for card in temp_cards:
            self.cards.append(card)
        
        db.session.add(self)
        db.session.commit()
    
    def get_one(self):
        card = list(self.cards).pop()
        db.session.commit()
        return card

    def as_json(self):
        return jsonify([x.as_json() for x in self.cards])
    
class Hand(CardSet, db.Model):

    def __init__(self):
        self.cards = []
        db.session.add(self)
        db.session.commit()

    def hit(self,card):
        self.cards.append(card)
        db.session.commit()
    
    def as_json(self):
        return jsonify([x.as_json() for x in self.cards])

