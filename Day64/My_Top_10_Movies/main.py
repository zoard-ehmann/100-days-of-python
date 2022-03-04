import os

import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLITE_DB_PATH')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False, unique=True)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String, nullable=False, unique=True)


class EditForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10', validators=[DataRequired()])
    review = TextAreaField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


@app.route('/')
def home():
    all_movies = Movie.query.all()
    return render_template('index.html', all_movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    movie = Movie.query.get(request.args['id'])
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=edit_form)


@app.route('/delete')
def delete():
    pass


if __name__ == '__main__':
    # db.create_all()
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    app.run(debug=True)
