from application import db
from application import login_manager
from flask_login import UserMixin

class car_list(db.Model):
    car_id = db.Column(db.String(30), primary_key=True)
    car_score = db.Column(db.Integer, nullable=False)
    top_speed = db.Column(db.Integer, nullable=False)
    acceleration = db.Column(db.Integer, nullable=False)
    handling = db.Column(db.Integer, nullable=False)
    horsepower = db.Column(db.Integer, nullable=False)
    cool_factor = db.Column(db.Integer, nullable=False)
    innovation = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return ''.join([
            'Car:              ', self.car_id, '\r\n',
            'Car Score:        ', self.car_score, '\r\n', 
            'Speed Score:      ', self.car_score, '\r\n',
            'Accel Score:      ', self.car_score, '\r\n',
            'Handling Score:   ', self.car_score, '\r\n',
            'HP Score:         ', self.car_score, '\r\n',
            'Coolness Score:   ', self.car_score, '\r\n',
            'Innovation Score: ', self.car_score, '\r\n', 
            ])

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40),unique=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    def get_id(self):
        return self.user_id
    def __repr__(self):
        return ''.join([
            'Username: ', self.username, '\r\n',
            ])

class Deck(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    Car1 = db.Column(db.String(128), nullable=False)
    Car2 = db.Column(db.String(128), nullable=False)
    Car3 = db.Column(db.String(128), nullable=False)
    Car4 = db.Column(db.String(128), nullable=False)
    Car5 = db.Column(db.String(128), nullable=False)
    def __repr__(self):
        return ''.join([
            'Car 1: ', self.Car1, '\r\n',
            'Car 2: ', self.Car2, '\r\n',
            'Car 3: ', self.Car3, '\r\n',
            'Car 4: ', self.Car4, '\r\n',
            'Car 5: ', self.Car5, '\r\n',
            ])

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
