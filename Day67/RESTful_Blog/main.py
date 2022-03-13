import os
from datetime import date

import bleach
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from dotenv import load_dotenv


load_dotenv()
ALLOWED_TAGS = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'p']

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET')
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', all_posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = db.session.query(BlogPost).get(index)
    return render_template('post.html', post=requested_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/new-post', methods=['GET', 'POST'])
def make_post():
    create_form = CreatePostForm()
    if create_form.validate_on_submit():
        db.session.add(BlogPost(
            title=create_form.title.data,
            subtitle=create_form.subtitle.data,
            author=create_form.author.data,
            img_url=create_form.img_url.data,
            body=bleach.clean(create_form.body.data, tags=ALLOWED_TAGS),
            date=date.today().strftime('%B %d, %Y')
        ))
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=create_form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)