#!/usr/bin/python3
""" Starts Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """returns text that is passed to c/<text>"""
    formatted_text = text.replace('_', ' ')
    response = "C {}".format(formatted_text)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
