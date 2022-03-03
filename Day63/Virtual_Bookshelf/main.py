from sqlite3 import IntegrityError
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['book_name'],
            author=request.form['book_author'],
            rating=request.form['book_rating']
        )

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template('add.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

