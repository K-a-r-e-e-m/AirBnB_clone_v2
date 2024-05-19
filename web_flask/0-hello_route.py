#!/usr/bin/python3
'''This module has a function that starts a flask'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellobnb():
    '''Starts a Flask web application'''
    return 'Hello HBNB!'


# web application must be listening on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
