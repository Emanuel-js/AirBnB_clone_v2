#!/usr/bin/python3
"""helloBNBN"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """hello world method"""
    return ("Hello HBNB!")


app.run(host='0.0.0.0', port=5000)
