from flask import jsonify
from random import shuffle

from blackjack.app.models.card import Card
from blackjack.app.models.cardtypes import CardSuit, CardRanks


class Deck():

    def __init__(self):
        self.cards = []
        for i in CardSuit:
            for j in CardRanks:
                current_card = Card(j,i)
                self.cards.append(current_card)
        shuffle(self.cards)

    def as_json(self):
        return jsonify([x.as_json() for x in self.cards])
