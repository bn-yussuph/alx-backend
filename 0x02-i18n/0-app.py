#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: render index.html
"""
from flask import Flask
from flask import render_template


# Instantiate the app object
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index()-> str:
    """Returns index.html"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
