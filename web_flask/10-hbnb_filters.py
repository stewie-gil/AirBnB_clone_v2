#!/usr/bin/python3
"""
Starts a Flask application for HBNB filters.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes db session after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Flask route at /hbnb_filters."""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    data = {"states": states, "amenities": amenities}
    return render_template('10-hbnb_filters.html', **data)
    # Render the template with the loaded data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
