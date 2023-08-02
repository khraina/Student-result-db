from flask import Blueprint, render_template

home = Blueprint("home", __name__)


@home.route('/')
def homepage():
    return render_template("home/home.html")


@home.route('/about')
def about():
    return render_template("home/about.html")


@home.route('/contact')
def contact():
    return render_template("home/contact.html")
