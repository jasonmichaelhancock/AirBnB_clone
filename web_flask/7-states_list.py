#!/usr/bin/python3

'''Script that starts a Flask web application.'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = []
    for key, value in storage.all('State').items():
        states.append(value)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
