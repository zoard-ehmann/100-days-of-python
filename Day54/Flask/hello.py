from flask import Flask


app = Flask(__name__)


def make_bold(function):

    def wrapper_function():
        return f'<b>{function()}</b>'

    return wrapper_function


def make_emphasis(function):

    def wrapper_function():
        return f'<em>{function()}</em>'

    return wrapper_function


def make_underlined(function):

    def wrapper_function():
        return f'<u>{function()}</u>'

    return wrapper_function


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
    '<p>This is a kiscica.</p>' \
    '<img src="https://media2.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif?cid=ecf05e47u029f53b8529rmf4lxefgip8t1s3al6gtak4lv0s&rid=giphy.gif&ct=g" width="200px">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name.title()}, you are {number} years old!'


if __name__ == '__main__':
    app.run(debug=True)