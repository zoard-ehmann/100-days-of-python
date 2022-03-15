import os

import bleach
from flask import Flask, render_template, redirect, request, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from dotenv import load_dotenv
from functools import wraps


#INFO: CONSTANTS
load_dotenv()
HASH_METHOD = 'pbkdf2:sha256'
SALT_LENGTH = 16
ALLOWED_TAGS = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'p']

#INFO: INITIALIZE APP
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET')
ckeditor = CKEditor(app)
Bootstrap(app)

#INFO: SET UP LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


#INFO: CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#INFO: CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    # PARENT RELATIONSHIPS
    posts = relationship('BlogPost', back_populates='author')
    comments = relationship('Comment', back_populates='author')


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    # PARENT RELATIONSHIPS
    comments = relationship('Comment', back_populates='post')
    # CHILD RELATIONSHIPS
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship('User', back_populates='posts')


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    # CHILD RELATIONSHIPS
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship('User', back_populates='comments')
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    post = relationship('BlogPost', back_populates='comments')


#INFO: FUNCTIONS AND DECORATORS
def is_admin():
    if current_user.is_authenticated and current_user.id == 1:
        return True
    return False


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_admin():
            return func(*args, **kwargs)
        return abort(status=403)
    return wrapper


#INFO: USER LOADER FOR LOGIN MANAGER
@login_manager.user_loader
def load_user(id):
    return db.session.query(User).get(id)


#INFO: APP ROUTES
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template('index.html', all_posts=posts, is_admin=is_admin())


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        if db.session.query(User).filter_by(email=register_form.email.data).first():
            flash('You\'ve already registered with this email address. Try to login instead.')
            return redirect(url_for('login'))
        user = User(
            email=register_form.email.data,
            password=generate_password_hash(password=register_form.password.data, method=HASH_METHOD, salt_length=SALT_LENGTH),
            name=register_form.name.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user=user)
        return redirect(url_for('get_all_posts'))
    return render_template('register.html', form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.query(User).filter_by(email=login_form.email.data).first()
        if user:
            if check_password_hash(pwhash=user.password, password=login_form.password.data):
                login_user(user=user)
                return redirect(url_for('get_all_posts'))
            flash('Incorrect password. Please try again.')
        else:
            flash('That email doesn\'t exist. Try to register first.')
            return redirect(url_for('register'))
    return render_template('login.html', form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            db.session.add(Comment(
                text=bleach.clean(text=comment_form.comment.data, tags=ALLOWED_TAGS),
                author=current_user,
                post=requested_post
            ))
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
        flash('Please log in to leave comments.')
        return redirect(url_for('login'))
    return render_template('post.html', post=requested_post, is_admin=is_admin(), form=comment_form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/new-post', methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=bleach.clean(text=form.body.data, tags=ALLOWED_TAGS),
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime('%B %d, %Y')
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = bleach.clean(text=edit_form.body.data, tags=ALLOWED_TAGS)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))

    return render_template('make-post.html', form=edit_form)


@app.route('/delete/<int:post_id>')
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


#INFO: START APP
if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)
