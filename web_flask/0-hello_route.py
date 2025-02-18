#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask


# references this file
hello_route = Flask(__name__)


# creating an index route to avoid a 404, in brackets is the url
# the define the function for that route
@hello_route.route("/", strict_slashes=False)
def index():
    """
    ROUTE  /: Hello HBNB!display
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    hello_route.run(host='0.0.0.0', port=5000)
