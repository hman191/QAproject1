from application import db
from application.models import car_list, user, deck

db.drop_all()
db.create_all()
