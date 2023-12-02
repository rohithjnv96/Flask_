# rewrite below import
from flask_wtf import *
from wtforms import *
from wtforms.validators import *


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=5, max=20)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('SignUp')
