from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required

from blackjack.app import app, db
#from blackjack.app.models.card import Card
from blackjack.app.models.deck import Deck, Hand, CardSet, Card
from blackjack.app.models.game import Game
from blackjack.app.models.player import Player
from blackjack.app.models.cardtypes import CardSuit, CardRanks
from blackjack.app.forms.user import LoginForm, 

"""
To be improved upon:
delete records after every game ends by game id
manual query or use model? delete rows with game id

change cards to text instead of its own table
"""

@app.route('/')
def home():
    #return new_deck.as_json()
    return "Hello World"

@app.route('/getcards')
@login_required
def get_cards():
    new_deck = Deck()
    new_hand = Hand()
    new_hand.hit(new_deck.get_one())
    return new_hand.as_json()

@app.route('/game')
@login_required
def play_game():
    if current_user.is_authenticated:
        current_game = Game.query.filter_by(player_id=current_user.id).first()
        print(current_game)
        if not current_game:
            current_game = Game()
            current_game.player_id = current_user.id
            db.session.add(current_game)
            db.session.commit()
            new_deck = Deck()
            print(current_game)
            #new_deck.game = current_game
            current_game.deck_id = new_deck.id
            new_hand = Hand()
            #new_hand.game = current_game
            current_game.player_hand_id = new_hand.id
            #db.session.add(new_hand)
            db.session.commit()
            new_hand.hit(new_deck.get_one())
            new_hand.hit(new_deck.get_one())
            return new_hand.as_json()
        else:
            player_hand = Hand.query.filter_by(id = current_game.player_hand_id).first()
            deck = Deck.query.filter_by(id = current_game.deck_id).first()
            player_hand.hit(deck.get_one())
            return player_hand.as_json()
    else:
        redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Player.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('home'))
		login_user(user, remember=form.remember_me.data)

		next_page = url_for('home')
		return redirect(next_page)
	return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	registForm = RegistrationForm()
	if registForm.validate_on_submit():
		user = Player(username=registForm.username.data, email=registForm.email.data)
		user.set_password(registForm.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', registForm=registForm)