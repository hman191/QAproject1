from flask import render_template
from application import app
from application.models import car_list,deck,user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/cars')
def cars():
    carData = car_list.query.all()
    return render_template('cars.html', title='Cars', carPost=carData)
@app.route('/about')
def about():
    return render_template('about.html', title='About')
@app.route('/register')
def register():
    return render_template('register.html', title='Register')
@app.route('/login')
def login():
    return render_template('login.html', title='Login')
