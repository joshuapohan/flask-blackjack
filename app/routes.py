from flask import render_template, flash, redirect, url_for, request, jsonify

from blackjack.app import app
from blackjack.app.models.card import Card
from blackjack.app.models.deck import Deck
from blackjack.app.models.game import Game
from blackjack.app.models.player import Player
from blackjack.app.models.cardtypes import CardSuit, CardRanks

@app.route('/')
def home():
    new_deck = Deck()
    return new_deck.as_json()