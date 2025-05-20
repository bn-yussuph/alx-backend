#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: render index.html
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate the app object
app = Flask(__name__)
app.config.from_object(Config)

# wrap the app in babel
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index()-> str:
    """Returns index.html"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
