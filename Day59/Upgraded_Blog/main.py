import os
import smtplib
import datetime as dt

import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()

EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('MY_PASSWORD')
HOST = os.getenv('SMTP_HOST')
PORT = os.getenv('SMTP_PORT')


with requests.Session() as session:
    response = session.get(url='https://api.npoint.io/8cb335cb2e29aa02528f')
    response.raise_for_status()
    all_posts = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    msg_sent = False

    if request.method == 'POST':
        msg_sent = send_mail(form_data=request.form)

    return render_template('contact.html', msg_sent=msg_sent)


@app.route('/post/<int:id>')
def post(id):
    requested_post = {
        'id': -1,
        'title': 'Uh-oh.. :(',
        'subtitle': 'Post not found.',
        'body': 'We cannot find the post you are looking for. Please double-check the URL you are referring to or feel free to get in touch with us.',
        'date': dt.datetime.today().strftime('%Y-%m-%d'),
        'author': 'AlertBot',
    }

    for post in all_posts:
        if id == post['id']:
            requested_post = post

    return render_template('post.html', post=requested_post)


def send_mail(form_data: dict) -> bool:
    """Takes the data from the contact form and sends the message to the owner's email.

    Args:
        form_data (dict): Data from the contact form.

    Returns:
        bool: Returns True once the functions runs successfully.
    """
    with smtplib.SMTP(host=HOST, port=PORT) as smtp_session:
        smtp_session.starttls()
        smtp_session.login(user=EMAIL, password=PASSWORD)
        smtp_session.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg='Subject:New Message from My Blog\n\n'
            f'Name: {form_data["name"]}\n'
            f'Email: {form_data["email"]}\n'
            f'Phone: {form_data["phone"]}\n'
            f'Message: {form_data["message"]}\n'
            .encode("utf-8")
        )

    return True


if __name__ == '__main__':
    app.run(debug=True)