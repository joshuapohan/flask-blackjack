from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField 

class TableForm(FlaskForm):
	hit = SubmitField(label='Hit')
	stand = SubmitField(label='Stand')