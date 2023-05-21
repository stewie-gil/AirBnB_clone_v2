#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    state = storage.get(State, id)
    if state:
        sorted_cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('state_cities.html', state=state, cities=sorted_cities)
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def teardown_session(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
