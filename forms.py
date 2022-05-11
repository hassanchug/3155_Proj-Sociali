from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import Length, Regexp, DataRequired, EqualTo
from wtforms import ValidationError

from src.models import db, Users

# form to login user
class LoginForm(FlaskForm):
    class Meta:
        csrf = False

username = StringField('username', [DataRequired()])
username = StringField('password', [DataRequired()])

submit = SubmitField('Log In')

def validate_username(self, field):
    if db.session.query(Users).filter_by(username=field.data).count() == 0:
        raise ValidationError('Incorrect Username.')

# form to signup user
class SignupForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('first_name', [DataRequired()])
    username = StringField('last_name', [DataRequired()])
    username = StringField('username', [DataRequired()])
    password = PasswordField('password', [DataRequired()])

    submit = SubmitField('Submit')

    def validate_username(self, field):
        if db.session.query(Users).filter_by(username=field.data).count() != 0:
            raise ValidationError('Username already in use.')