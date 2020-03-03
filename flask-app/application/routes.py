from application import app, db
from application.models import car_list,deck,user
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import LoginForm
from flask import render_template, redirect, url_for, request
@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/cars')
def cars():
    carData = car_list.query.all()
    return render_template('cars.html', title='Cars', carPost=carData)

@app.route('/deck')
@login_required
def deck():
    deckData = deck.query.all()
    form = deckForm()
    return render_template('deck.html', title='Deck', deckPost=deckData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
