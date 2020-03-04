from application.models import car_list, deck, user
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = user(email=form.email.data, username=form.username.data, password=hash_pw)

        db.session.add(User)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=user.query.filter_by(email=form.email.data).first()
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
