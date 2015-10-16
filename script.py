#!/usr/bin/env python
from flask import Flask, send_file, url_for, render_template
from datetime import datetime

app = Flask(__name__)

dogs = ['Doberman', 'Golden Retriever', 'Snoop', 'Beagle', 'Bull Terrier',\
        'Akita', 'Siberian Husky', 'Pit Bull', 'Pug', 'Black Lab']

@app.route('/')
def index():
    """
    Returns
    """
    url_for('static', filename='x.gif')
    now = datetime.now()
    return render_template('index.html',\
                           time=now)


@app.route('/user/<username>')
def render_username(username):
    """
    Returns a specified page at the url /user/<username>
    """
    url_for('static', filename='hal.jpg')
    return render_template('user.html', username=username)


# TODO: Add another endpoint `/dog/` which sends a message with a random dog..
# It should render a new template 'dogs.html' which is passed a 'dog'
# variable.


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
