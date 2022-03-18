from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed


class PropertyForm(FlaskForm):
	title = StringField('Property Title', validators=[InputRequired()])
	description = TextAreaField('Description', validators=[InputRequired()])
	bedrooms = StringField('No. of Rooms', validators=[InputRequired()])
	bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()])
	price = StringField('Price', validators=[InputRequired()])
	ptype = SelectField('Property Type', choices = [('House','House'),('Apartment','Apartment')], validators=[InputRequired()])
	location = StringField('Location', validators=[InputRequired()])
	photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only')])


