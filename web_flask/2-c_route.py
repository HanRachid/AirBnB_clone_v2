#!/usr/bin/python3
"""
Starts flask server listening on route / and
/HBNB
"""
from flask import Flask
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


if __name__ == '__main__':

    app.run(host="0.0.0.0")
