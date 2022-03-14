import os

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv


load_dotenv()

SALT_LENGTH = 8
HASH_METHOD = 'pbkdf2:sha256'
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('APP_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@login_manager.user_loader
def load_user(id):
    return db.session.query(User).get(id)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            email=request.form.get('email'),
            password=generate_password_hash(password=request.form.get('password'), method=HASH_METHOD, salt_length=SALT_LENGTH),
            name=request.form.get('name')
        )
        if db.session.query(User).filter_by(email=user.email).first():
            flash('You\'ve already signed up with that email, try to login instead.')
            return redirect(url_for('login'))
        db.session.add(user)
        db.session.commit()
        login_user(user=user)
        return redirect(url_for('secrets'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.session.query(User).filter_by(email=email).first()
        if user:
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user=user)
                return redirect(url_for('secrets'))
            flash('Incorrect password, please try again.')
        else:
            flash('Sorry, that email does not exist in our database.')
    return render_template('login.html')


@app.route('/secrets')
@login_required
def secrets():
    return render_template('secrets.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == '__main__':
    app.run(debug=True)
