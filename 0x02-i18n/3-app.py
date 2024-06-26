#!/usr/bin/env python3
"""app
author
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """To configure the lang"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Gets the locale language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    home_title = _('home_title')
    home_header = _('home_header')
    return render_template(
            '3-index.html', home_title=home_title,
            home_header=home_header, get_locale=get_locale)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
