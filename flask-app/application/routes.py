from application.models import car_list, Deck, User
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, deckForm

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/cars')
def cars():
    carData = car_list.query.all()
    return render_template('cars.html', title='Cars', carPost=carData)

@app.route('/deck', methods=['GET', 'POST'])
@login_required
def deck():
    userid = current_user.user_id
    cars = car_list.query.all()
    deckData = Deck.query.all()
    form = deckForm()
    deckFilter = Deck.query.filter(Deck.user_id == userid).all()
    if form.validate_on_submit():
        deck = Deck(
        user_id=userid,
        Car1=form.Car1.data,
        Car2=form.Car2.data,
        Car3=form.Car3.data,
        Car4=form.Car4.data,
        Car5=form.Car5.data)
        db.session.add(deck)
        db.session.commit()
        deldeck = Deck.query.filter(Deck.user_id == userid).first()
        db.session.delete(deldeck)
        db.session.commit()

        return redirect(url_for('deck'))
    return render_template('deck.html', title='Deck',cars=cars, userid=userid, deckFilter=deckFilter, deckPost=deckData, form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        users = User(email=form.email.data, username=form.username.data, password=hash_pw)
        db.session.add(users)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.user_id
    account = User.query.filter_by(user_id=user).first()
    accountDeck = Deck.query.filter_by(user_id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.delete(accountDeck)
    db.session.commit()
    return redirect(url_for('register'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        userid = current_user.user_id
        deckFilter = Deck.query.filter(Deck.user_id == userid).all()
        if deckFilter==[]:
            deckadd = Deck(user_id=userid, Car1="Car1", Car2="Car2", Car3="Car3", Car4="Car4", Car5="Car5")
            db.session.add(deckadd)
            db.session.commit()
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        users=User.query.filter_by(username=form.username.data).first()
        if users and bcrypt.check_password_hash(users.password, form.password.data):
            login_user(users, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                userid = current_user.user_id
                deckFilter = Deck.query.filter(Deck.user_id == userid).all()
                if deckFilter==[]:
                    deckadd = Deck(user_id=userid, Car1="Car1", Car2="Car2", Car3="Car3", Car4="Car4", Car5="Car5")
                    db.session.add(deckadd)
                    db.session.commit()
                return redirect(next_page)
            else:
                userid = current_user.user_id
                deckFilter = Deck.query.filter(Deck.user_id == userid).all()
                if deckFilter==[]:
                    deckadd = Deck(user_id=userid, Car1="Car1", Car2="Car2", Car3="Car3", Car4="Car4", Car5="Car5")
                    db.session.add(deckadd)
                    db.session.commit()
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
