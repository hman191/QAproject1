from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, PasswordField, BooleanField

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
