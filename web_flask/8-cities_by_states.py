#!/usr/bin/python3
'''Script starts Flask web application.'''
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    '''After each request you must remove the current SQLAlchemy Session.'''
    storage.close()


@app.route('/states_list')
def html_fetch_states():
    """display html page
       fetch sorted states to insert into html in UL tag
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           state_objs=state_objs)


@app.route('/cities_by_states')
def html_fetch_cities_by_states():
    '''To load all cities of a State.'''
    state_objs = [s for s in storage.all("State").values()]
    return render_template('8-cities_by_states.html',
                           state_objs=state_objs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
