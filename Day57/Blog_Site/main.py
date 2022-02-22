import requests
from flask import Flask, render_template
from post import Post


app = Flask(__name__)


def get_data():
    with requests.Session() as session:
        response = session.get('https://api.npoint.io/c790b4d5cab58020d391')
        response.raise_for_status()
        blog_data = response.json()

    return [Post(id=post['id'], title=post['title'], subtitle=post['subtitle'], body=post['body']) for post in blog_data]


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/post/<int:id>')
def post(id):
    requested_post = Post(
        id=-1,
        title='Uh-oh... :(',
        subtitle='Looks like the post does not exist.',
        body='We\'re sorry for the inconvenience. The post you would like to see cannot be found on our systems. It could be a temporary issue or the post was deleted. Please check back later or get in touch with us. Thank you!'
    )

    for post in posts:
        if id == post.id:
            requested_post = post
            
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    posts = get_data()
    app.run(debug=True)
