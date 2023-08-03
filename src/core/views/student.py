from flask import Blueprint, render_template, redirect, request
from ..models import *

StudentViews = Blueprint("StudentViews", __name__)


# @StudentViews.route("/")
# def home():
#     return render_template("student/student_view.html", SectionHeader="View", sem="2")

@StudentViews.route("/", methods=["GET", "POST"])
def view_grade():
    sem = ''
    if request.method == 'POST':

        sem = request.form.get('sem')
        regno = request.form.get('regno')

        print(f"\n {sem=} \n \n")
        
        if sem == "1":
            students = Sem1.query.filter_by(RegNo=regno).all()
            return render_template('student/student_view.html', students=students, sem=sem)

        elif sem == "2":
            print(f"\n {sem=} \n \n")
            students = Sem2.query.filter_by(RegNo=regno).all()
            return render_template('student/student_view.html', students=students, sem=sem)

        elif sem == "3":
            print(f"\n {sem=} \n \n")
            students = Sem3.query.filter_by(RegNo=regno).all()
            return render_template('student/student_view.html', students=students, sem=sem)

        elif sem == "4":
            print(f"\n {sem=} \n \n")
            students = Sem4.query.filter_by(RegNo=regno).all()
            print(f"\n {students=} \n \n")
            return render_template('student/student_view.html', students=students, sem=sem)

        elif sem == "5":
            print(f"\n {sem=} \n \n")
            students = Sem5.query.filter_by(RegNo=regno).all()
            return render_template('student/student_view.html', students=students, sem=sem)
        elif sem == "6":
            print(f"\n {sem=} \n \n")
            students = Sem6.query.filter_by(RegNo=regno).all()
            return render_template('student/student_view.html', students=students, sem=sem)
        elif sem == "7":
            print(f"\n {sem=} \n \n")
            students = Sem7.query.filter_by(RegNo=regno).all()
            return render_template('student/student_view.html', students=students, sem=sem)
        elif sem == "8":
            students = Sem8.query.filter_by(RegNo=regno).all()
            return render_template('student/student_view.html', students=students, sem=sem)
        else :
            print(f"nothing {sem=}")

        return render_template('student/student_view.html', students=students, SectionHeader="List", sem=sem)

    return render_template('student/student_view.html', SectionHeader="List", sem=sem)