from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import Length, Regexp, DataRequired, EqualTo, Email
from wtforms import ValidationError

from models import Users
from src.models import db

# form to login user
class LoginForm(FlaskForm):
    class Meta:
        csrf = False

username = StringField('Username', DataRequired())
username = StringField('Username', DataRequired())

submit = SubmitField('Log In')

def validate_username(self, field):
    if db.session.query(Users).filter_by(username=field.data).count() == 0:
        raise ValidationError('Incorrect Username.')