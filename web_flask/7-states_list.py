#!/usr/bin/python3
"""Starts a flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """displays html for states list"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_request
def close_storage(exception):
    """closes storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
