from flask import Blueprint, render_template

StudentViews = Blueprint("StudentViews", __name__)


@StudentViews.route("/")
def home():
    return render_template("student/student_view.html", SectionHeader="View", sem="2")


@StudentViews.route("/result")
def result():
    return render_template("student/loginstudent.html")

@StudentViews.route("/filter_by")
def filter_by():
    return "<H1>This a student Filter page</H1>"
