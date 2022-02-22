import random
import datetime as dt

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    curr_year = dt.datetime.today().strftime('%Y')
    return render_template('index.html', num=random_number, current_year=curr_year)

if __name__ == '__main__':
    app.run(debug=True)