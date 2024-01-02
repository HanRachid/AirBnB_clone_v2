#!/usr/bin/python3
"""
Starts flask server listening on route / and
/HBNB
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    newtext = text.replace("_", " ")
    return f'C {newtext}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    newtext = text.replace("_", " ")
    return f'Python {newtext}'


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if n.isnumeric():
        return f'{n} is a number'
    abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    if n.isnumeric():
        return render_template('5-number.html', number=n)
    abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    if n.isnumeric():
        p = 'even' if int(n) % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', number=n, parity=p)
    abort(404)


if __name__ == '__main__':

    app.run(host="0.0.0.0")
