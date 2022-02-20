import random

from flask import Flask


HOME = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
HIGH = 'https://media.giphy.com/media/bU3YVJAAXckCI/giphy.gif'
LOW = 'https://media.giphy.com/media/Z2rdURiFnGl0klPaaP/giphy.gif'
CORRECT = 'https://media.giphy.com/media/xUA7bfDqAUodEx64o0/giphy.gif'


solution = random.randint(0, 9)
app = Flask(__name__)


@app.route('/')
def home():
    return(
        '<h1>Guess a number between 0 and 9</h1>'
        f'<img src="{HOME}">'
    )


@app.route('/<int:user_guess>')
def result(user_guess):
    if user_guess < solution:
        return(
            '<h1 style="color: red;">Too low.</h1>'
            f'<img src="{LOW}">'
        )
    elif user_guess > solution:
        return(
            '<h1 style="color: purple;">Too high.</h1>'
            f'<img src="{HIGH}">'
        )
    else:
        return(
            '<h1 style="color: green;">Got it!</h1>'
            f'<img src="{CORRECT}">'
        )


if __name__ == '__main__':
    app.run(debug=True)