from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('ConfirmPassword', validators=[DataRequired()])
    
