"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def show_form():
    """display add user form"""
    users = User.query.all()
    return render_template('main.html', users=users)

@app.route("/users")
def show_user():
    """Render user-form"""
    return render_template('user_form.html')

@app.route('/add-user-data', methods=["POST"])
def add_user_data():
    """adds user to database"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/")

@app.route('/users/<int:id>')
def show_user_profile(id):
    """displaying user info on user detail page"""
    detail = User.query.get(id)

    first_name = detail.first_name
    last_name = detail.last_name
    image_url = detail.image_url

    return render_template("user_detail.html", user=detail, first_name=first_name, last_name=last_name, image_url=image_url)

@app.route("/users/<int:id>/delete", methods=["POST"])
def delete_user(id):
    """delete user"""

    d_user = User.query.get(id)
    db.session.delete(d_user)
    db.session.commit()

    return redirect("/")