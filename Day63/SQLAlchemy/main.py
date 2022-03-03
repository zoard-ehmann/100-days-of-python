from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


if __name__ == '__main__':
    db.create_all()

    # INFO: Create new record
    # book = Books(title='Harry Potter', author='J.K. Rowling', rating=9.4)
    # db.session.add(book)
    # db.session.commit()

    # INFO: Read all records
    # all_books = db.session.query(Books).all()
    
    # INFO: Read a particular record by query
    # book = Books.query.filter_by(title='Harry Potter').first()
    
    # INFO: Update a particular record by query
    # book_to_update = Books.query.filter_by(title='Harry Potter').first()
    # book_to_update.title = 'Harry Potter and the Chamber of Secrets'
    # db.session.commit()

    # INFO: Update a record by primary key
    # book_id = 1
    # book_to_update = Books.query.get(book_id)
    # book_to_update.title = 'Harry Potter and the Chamber of Secrets'
    # db.session.commit()

    # INFO: Delete a particular record by primary key
    # book_id = 1
    # book_to_delete = Books.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()
