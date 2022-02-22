import random
import datetime as dt

import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    curr_year = dt.datetime.today().strftime('%Y')
    return render_template('index.html', num=random_number, current_year=curr_year)

@app.route('/guess/<name>')
def guess(name):
    with requests.Session() as session:
        agify_response = session.get(f'https://api.agify.io/?name={name}')
        agify_response.raise_for_status()
        predicted_age = agify_response.json()['age']
        
        genderize_response = session.get(f'https://api.genderize.io?name={name}')
        genderize_response.raise_for_status()
        predicted_gender = genderize_response.json()['gender']

    return render_template('guess.html', name=name.title(), age=predicted_age, gender=predicted_gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

    with requests.Session() as session:
        response = session.get(blog_url)
        response.raise_for_status()
        all_posts = response.json()

    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)