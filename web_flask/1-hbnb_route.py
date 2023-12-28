#!/usr/bin/python3
"""
Starts flask server listening on route / and
/HBNB
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():

    return ""


if __name__ == '__main__':

    app.run(host="0.0.0.0")
