from flask import Blueprint, render_template

StudentViews = Blueprint("StudentViews", __name__)


@StudentViews.route("/")
def home():
    return render_template("student/student_view.html", SectionHeader="View", sem="2")


@StudentViews.route("/result")
def result():
    return "<H1>This a student result page</H1>"


@StudentViews.route("/filter_by")
def filter_by():
    return "<H1>This a student Filter page</H1>"
