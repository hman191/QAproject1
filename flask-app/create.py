from application import db
from application.models import car_list, User, Deck

db.drop_all()
db.create_all()
