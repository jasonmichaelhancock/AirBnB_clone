#!/usr/bin/python3

'''Script that starts a Flask web application.'''

from flask import Flask

app = Flask('__name__')

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB!'
@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    text.replace("_", " ")
    return 'C %s' % text
@app.route('/python/<string:text>', strict_slashes=False)
def show_default_text(text="is_cool"):
    text.replace("_", " ")
    return 'Python %s' % text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
