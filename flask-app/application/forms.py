from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from application.models import User, Deck, car_list
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField('Username',
        validators=[
            DataRequired(),
        ])

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ])
    username = StringField('username',
        validators = [
            DataRequired(),
            Length(min=4, max=20)
        ])
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ])
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()

        if users:
            raise ValidationError('Email already in use')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
    
    def validate_username(self,username):
        if username.data != current_user.username:
            usern = User.query.filter_by(username=username.data).first()
            if usern:
                raise ValidationError('Username already in use')
class deckForm(FlaskForm):
    Car1 = StringField('Car 1',
        validators=[
            DataRequired(),
        ])
    Car2 = StringField('Car 2',
        validators=[
            DataRequired(),
        ])
    Car3 = StringField('Car 3',
        validators=[
            DataRequired(),
        ])
    Car4 = StringField('Car 4',
        validators=[
            DataRequired(),
        ])
    Car5 = StringField('Car 5',
        validators=[
            DataRequired(),
        ])
    submit = SubmitField('Update')
    def validate_Car1(self, Car1):
        usercar1 = car_list.query.filter_by(car_id=Car1.data).first()
        if usercar1:
            return ('Success')
        else:
            raise ValidationError('Car not in list, please enter one listed below')
    def validate_Car2(self, Car2):
        usercar2 = car_list.query.filter_by(car_id=Car2.data).first()
        if usercar2:
            return ('Success')
        else:
            raise ValidationError('Car not in list, please enter one listed below')
    def validate_Car3(self, Car3):
        usercar3 = car_list.query.filter_by(car_id=Car3.data).first()
        if usercar3:
            return ('Success')
        else:
            raise ValidationError('Car not in list, please enter one listed below')
    def validate_Car4(self, Car4):
        usercar4 = car_list.query.filter_by(car_id=Car4.data).first()
        if usercar4:
            return ('Success')
        else:
            raise ValidationError('Car not in list, please enter one listed below')
    def validate_Car5(self, Car5):
        usercar5 = car_list.query.filter_by(car_id=Car5.data).first()
        if usercar5:
            return ('Success')
        else:
            raise ValidationError('Car not in list, please enter one listed below')
