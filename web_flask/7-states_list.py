#!/usr/bin/python3

'''Script that starts a Flask web application.'''

from flask import Flask, render_template
from models import *

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list')
def html_fetch_states():
    '''Script that starts a Flask web application.'''
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           state_objs=state_objs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
