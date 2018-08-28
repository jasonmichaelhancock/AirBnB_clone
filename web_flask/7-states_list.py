#!/usr/bin/python3
'''Script that starts a Flask web application.'''
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    '''After each request remove current SQLAlchemy session.'''
    storage.close()


@app.route('/states_list')
def html_fetch_states():
    '''Fetch sorted states to insert into html in UL tag.'''
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           state_objs=state_objs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
