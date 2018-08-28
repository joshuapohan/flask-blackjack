import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	LOCAL_DB_URL = 'postgres://postgres:dijital2012@localhost:5432/blackjack'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	#SQLALCHEMY_DATABASE_URI = HEROKU_DB_URL
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		LOCAL_DB_URL or \
		'sqlite:///' + os.path.join(basedir,'nblog.db')
	SQLALCHEMY_TRACK_MODIFICATION = False