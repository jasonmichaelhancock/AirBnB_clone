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

@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def show_default_text(text="is cool"):
    text.replace("_", " ")
    return 'Python %s' % text

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number2(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
