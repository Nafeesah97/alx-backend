 #!/usr/bin/env python3
"""app"""
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def home():
    """to route to home page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
