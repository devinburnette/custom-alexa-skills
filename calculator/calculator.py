import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("AddIntent", convert={'first': int, 'second': int})
def add(first, second):
    answer = first + second
    return question("{}, Can I help with something else?".format(answer))

@ask.intent("SubtractIntent", convert={'first': int, 'second': int})
def subtract(first, second):
    answer = first - second
    return question("{}, Can I help with something else?".format(answer))

@ask.intent("MultiplyIntent", convert={'first': int, 'second': int})
def multiply(first, second):
    answer = first * second
    return question("{}, Can I help with something else?".format(answer))

@ask.intent("DivideIntent", convert={'first': int, 'second': int})
def divide(first, second):
    answer = first / second
    return question("{}, Can I help with something else?".format(answer))

@ask.intent("GoodbyeIntent")
def goodbye():
    goodbye_message = render_template('bye')
    return statement(goodbye_message)

if __name__ == '__main__':
    app.run(debug=True)
