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
    img_url = url_for('static', filename='x.gif')
    now = datetime.now()
    return render_template('index.html',\
                           time=now,\
                           img_url=img_url)


@app.route('/user/<username>')
def render_username(username):
    """
    Returns a specified page at the url /user/<username>
    """
    img_url = url_for('static', filename='hal.jpg')
    return render_template('user.html',\
                           username=username,\
                           img_url=img_url)

# TODO: Add '/dogs/' endpoint that returns random dog from list of dogs.
@app.route('/dogs/')
def render_dogs_page():
    """
    Returns random dog from 'dogs' array above.
    """
    ### PUT CODE HERE
    pass # Remove this line when you write your own code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
