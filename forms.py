from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import Length, Regexp, DataRequired, EqualTo
from wtforms import ValidationError

from src.models import db, User

# form to login user
class LoginForm(FlaskForm):
    class Meta:
        csrf = False

username = StringField('username')
username = StringField('password')

submit = SubmitField('Log In')

def validate_username(self, field):
    if db.session.query(User).filter_by(username=field.data).count() == 0:
        raise ValidationError('Incorrect Username.')

# form to signup user
class SignupForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('first_name')
    username = StringField('last_name')
    username = StringField('username')
    password = PasswordField('password')

    submit = SubmitField('Submit')

    def validate_username(self, field):
        if db.session.query(User).filter_by(username=field.data).count() != 0:
            raise ValidationError('Username already in use.')