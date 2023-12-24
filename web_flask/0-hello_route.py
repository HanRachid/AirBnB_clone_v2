#!/usr/bin/env python3
"""
Starts Falsk server, listening on route /
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():

    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True)
