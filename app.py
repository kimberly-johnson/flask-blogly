"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

@app.route("/")
def show_form():
    """display add user form"""

    return render_template('base.html')

@app.route("/user")
def show_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name='first_name', last_name='last_name', image_url='image_url')
    db.session.add(user)
    db.commit()

    return 