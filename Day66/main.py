from crypt import methods
import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/random', methods=['GET'])
def get_random_cafe():
    if request.method == 'GET':
        cafe = random.choice(db.session.query(Cafe).all())
        return jsonify(cafe=cafe.to_dict())


@app.route('/all', methods=['GET'])
def get_all_cafes():
    if request.method == 'GET':
        all_cafes = db.session.query(Cafe).all()
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search/<location>', methods=['GET'])
def find_cafe(location):
    if request.method == 'GET':
        cafes = db.session.query(Cafe).filter_by(location=location.title()).all()
        if len(cafes) != 0: return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
        return jsonify(error={
            'Not Found': 'Sorry, we don\'t have a cafe at that location.'
        })


if __name__ == '__main__':
    app.run(debug=True)
