#!/usr/bin/python3
'''This module has a function that starts a flask with two routes'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellobnb():
    '''Starts a Flask web application'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Starts a Flask web application with another route'''
    return 'HBNB'


@app.route('/c/<arg>', strict_slashes=False)
def cisfun(arg):
    '''Starts a Flask web application with another route'''
    return f'C {arg.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is_cool"):
    '''Starts a Flask web application with another route'''
    return f'Python {text.replace("_", " ")}'


# int: --> convert data type from str to int
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Starts a Flask web application with another route'''
    if isinstance(n, int):
        return f'{n} is a number'


# web application must be listening on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
