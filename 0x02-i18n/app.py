#!/usr/bin/env python3
"""app
author
"""
from flask import Flask, render_template, request, g
from typing import Union, Dict
from flask_babel import Babel, _, format_datetime
import pytz


class Config:
    """To configure the lang"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Gets the locale language"""
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """Gets the time zone."""
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            pytz.timezone(url_timezone)
            return url_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    home_title = _('home_title')
    home_header = _('home_header')
    g.time = format_datetime()
    return render_template(
            'index.html', home_title=home_title,
            home_header=home_header, get_locale=get_locale)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
