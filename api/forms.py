from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, IntegerField, RadioField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, HiddenField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
from api.models import User


class UserForm(FlaskForm):
	name = StringField('Name', validators = [DataRequired(), Length(max = 30)])
	about = StringField('About', validators = [DataRequired(), Length(max = 120)])
	password = PasswordField('Password', validators = [DataRequired()])
	submit = SubmitField('Done')

	def validateEmail(self, Email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email taken, enter a different one')