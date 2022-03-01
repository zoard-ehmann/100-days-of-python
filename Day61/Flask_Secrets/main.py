import os

from flask import Flask, render_template
from dotenv import load_dotenv
from login_form import LoginForm


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)