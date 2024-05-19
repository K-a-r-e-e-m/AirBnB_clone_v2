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


# web application must be listening on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
