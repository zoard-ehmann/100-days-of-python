import os
import csv

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
from dotenv import load_dotenv

load_dotenv()

CSV_DATA = 'Day62/Coffee_and_Wifi/cafe-data.csv'


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET')
Bootstrap(app)


class CafeForm(FlaskForm):
    def __insert_choices(emoji: str, can_be_blank: bool=True) -> list:
        """Returns a range of 1-5 of emojis as a list.

        Args:
            emoji (str): Base emoji for the range.
            can_be_blank (bool, optional): Determines if '✘' should appear and act as default choice. Defaults to True.

        Returns:
            list: Range between 1-5 (and '✘' if defined).
        """
        choices = [num * emoji for num in range(1, 6)]
        if can_be_blank: choices.insert(0, '✘')
        return choices
    
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    location = URLField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField(label='Opening Hour', validators=[DataRequired()])
    close = StringField(label='Closing Hour', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=__insert_choices(emoji='☕', can_be_blank=False), validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Rating', choices=__insert_choices(emoji='💪'), validators=[DataRequired()])
    power_outlet = SelectField(label='Power Outlets', choices=__insert_choices(emoji='🔌'), validators=[DataRequired()])
    submit = SubmitField(label='Submit')


def write_cafe_db(cafe_details: dict):
    """Saves a new Café into the Café Database.

    Args:
        cafe_details (dict): Details of the new Café - comes from the form.
    """
    with open(CSV_DATA, mode='a', newline='') as csv_file:
        cafe_db = csv.writer(csv_file, delimiter=',')
        cafe_db.writerow([
            cafe_details['cafe'],
            cafe_details['location'],
            cafe_details['open'],
            cafe_details['close'],
            cafe_details['coffee_rating'],
            cafe_details['wifi_rating'],
            cafe_details['power_outlet']
        ])


# all Flask routes below
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        write_cafe_db(cafe_details=form.data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(CSV_DATA, newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
