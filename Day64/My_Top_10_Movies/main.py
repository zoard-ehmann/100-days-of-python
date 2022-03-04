import os

import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
from werkzeug.exceptions import BadRequestKeyError


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
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer, unique=True)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String, nullable=False, unique=True)


class EditForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10', validators=[DataRequired()])
    review = TextAreaField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


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
    movie = Movie.query.get(request.args['id'])
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        with requests.Session() as session:
            response = session.get(url='https://api.themoviedb.org/3/search/movie', params={
                'api_key': os.getenv('TMDB_API_KEY'),
                'query': add_form.title.data
            })
            response.raise_for_status()
            movie_list = response.json()['results']
        
        return render_template('select.html', movie_list=movie_list)

    try:
        tmdb_id = request.args['tmdb_id']
        with requests.Session() as session:
            response = session.get(url=f'https://api.themoviedb.org/3/movie/{tmdb_id}', params={
                'api_key': os.getenv('TMDB_API_KEY')
            })
            response.raise_for_status()
            movie = response.json()
            new_movie = Movie(
                id=tmdb_id,
                title=movie['original_title'],
                year=movie['release_date'].split('-')[0],
                description=movie['overview'],
                img_url=f'https://image.tmdb.org/t/p/original/{movie["backdrop_path"]}'
            )
            db.session.add(new_movie)
            db.session.commit()
        
        return redirect(url_for('edit', id=tmdb_id))

    except BadRequestKeyError:
        return render_template('add.html', add_form=add_form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
