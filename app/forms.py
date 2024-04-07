from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField,TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
	title = StringField('Movie Title', validators=[InputRequired()])
	description = TextAreaField('Summary of Movie', validators=[InputRequired()])
	poster = FileField('Poster', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Only Images!')])