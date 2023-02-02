#!/usr/bin/env python3
""" Starts a Flask Web Application """

from flask import Flask, render_template
from flask_babel import Babel
from pytz import timezone, UTC

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config for a Flask app. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def hello_world():
    """/ route handler. """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
