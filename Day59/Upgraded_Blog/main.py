import datetime as dt

import requests
from flask import Flask, render_template
from post import Post


with requests.Session() as session:
    response = session.get(url='https://api.npoint.io/8cb335cb2e29aa02528f')
    response.raise_for_status()
    data = response.json()

all_posts = [Post(post) for post in data]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:id>')
def post(id):
    requested_post = Post({
        'id': -1,
        'title': 'Uh-oh.. :(',
        'subtitle': 'Post not found.',
        'body': 'We cannot find the post you are looking for. Please double-check the URL you are referring to or feel free to get in touch with us.',
        'date': dt.datetime.today().strftime('%Y-%m-%d'),
        'author': 'AlertBot',
    })

    for post in all_posts:
        if id == post.id:
            requested_post = post

    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)