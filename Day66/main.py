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
    return render_template('index.html')


@app.route('/random')
def get_random_cafe():
    cafe = random.choice(db.session.query(Cafe).all())
    return jsonify(cafe=cafe.to_dict()), 200


@app.route('/all')
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes]), 200


@app.route('/search')
def find_cafe():
    cafes = db.session.query(Cafe).filter_by(location=request.args.get('loc').title()).all()
    if len(cafes) != 0: return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200
    return jsonify(error={
        'Not Found': 'Sorry, we don\'t have a cafe at that location.'
    }), 404


@app.route('/add', methods=['POST'])
def add_cafe():
    db.session.add(Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
    ))
    db.session.commit()
    return jsonify(response={
        'success': 'Successfully added the new cafe.'
    }), 200


@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_cafe_price(cafe_id):
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe:
        cafe.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={
            'success': 'Successfully updated the price.'
        }), 200
    return jsonify(error={
        'Not Found': 'Sorry, a cafe with that ID was not found in the database.'
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
