from flask import render_template, url_for, flash, redirect
from server import app, db, bcrypt
from server.forms import RegistrationForm, LoginForm
from server.db_models import User
from flask_login import login_user

posts = [
    {
        'institution': 'Rank Tbale',
        'title': '1.',
        'content': 'Top universities in the UK',
        'date_posted': 'April 1, 2020'
    }
]

@app.route('/')
@app.route('/home') # this is the URL path
def home():
    return render_template('home.html', posts=posts, title="UniChecker") #renders html code from the html file

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created, you are now able to log in! ", "success")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user, remember=form.remember.data)
           return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. PLease check your username and password', "danger")
    return render_template('login.html', title='Login', form=form)
