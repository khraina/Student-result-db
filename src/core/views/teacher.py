from flask import Blueprint, render_template, request, redirect, jsonify, url_for, flash
import pandas as pd
from ..models import *
from .. import db
import json

TeacherViews = Blueprint("TeacherViews", __name__)


@TeacherViews.route("/")
def home():
    return render_template("teacher/teacher_home.html", SectionHeader="Dashboard")


@TeacherViews.route("/addsub", methods=['POST', 'GET'])
def addsub():
    if request.method == 'POST':

        sem = request.form.get('Sem')
        subCode = request.form.get('subcode')

        subject_entry = Subject(Sem=sem, SubCode=subCode)

        db.session.add(subject_entry)
        db.session.commit()

        return redirect("/teacher/addsub")

    subject_list = Subject.query.all()
    print(type(subject_list))

    return render_template("teacher/teacher_add_subject.html", subject_list=subject_list)


@TeacherViews.route('/uploads', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':

        sem = int(request.form.get('Sem'))
        batch = int(request.form.get('Batch'))
        file = request.files['file']

        if file.filename == '':
            flash('No file selected!', 'error')
            return redirect(request.url)

        if file and file.filename.endswith('.csv'):
            print("enter the csv func")
            try:
                # Read the CSV data and store it in the database
                df = pd.read_csv(file)

                if sem == 1:
                    for index, row in df.iterrows():
                        data = Sem1(
                            RegNo=row['RegNo'],
                            Name=row['Name'],
                            PHT100=row['PHT100'],
                            MAT101=row['MAT101'],
                            HUN101=row['HUN101'],
                            EST100=row['EST100'],
                            EST130=row['EST130'],
                            PHL120=row['PHL120'],
                            ESL130=row['ESL130'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                elif sem == 2:
                    for index, row in df.iterrows():
                        data = Sem2(
                            RegNo=row['RegNo'],
                            Name=row['Name'],
                            EST120=row['EST120'],
                            CYT100=row['CYT100'],
                            EST110=row['EST110'],
                            MAT102=row['MAT102'],
                            EST102=row['EST102'],
                            HUN102=row['HUN102'],
                            CYL120=row['CYL120'],
                            ESL120=row['ESL120'],
                            ESL102=row['ESL102'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                elif sem == 3:
                    for index, row in df.iterrows():
                        data = Sem3(
                            RegNo=row['RegNo'],
                            Name=row['Name'],
                            MAT203=row['MAT203'],
                            CST201=row['CST201'],
                            CST203=row['CST203'],
                            CST205=row['CST205'],
                            HUT200=row['HUT200'],
                            MCN201=row['MCN201'],
                            CSL201=row['CSL201'],
                            CSL203=row['CSL203'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                # Add the other semmisters here
                elif sem == 4:
                    print("\n\nAt the If 4\n\n")
                    for index, row in df.iterrows():
                        data = Sem4(
                            RegNo=row['Reg.No'],
                            Name=row['Name'],
                            batch=batch,
                            EST200=row['EST200'],
                            MCN202=row['MCN202'],
                            CST202=row['CST202'],
                            CST204=row['CST204'],
                            CST206=row['CST206'],
                            CSL202=row['CSL202'],
                            CSL204=row['CSL204'],
                            MAT206=row['MAT206'],
                            Earned_Credits=row['Earned Credits'],
                            Cumilative_Credits=row['Cumilative Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                elif sem == 5:
                    for index, row in df.iterrows():
                        data = Sem5(
                            RegNo=row['RegNo'],
                            Name=row['Name'],
                            MCN301=row['MCN301'],
                            CST301=row['CST301'],
                            CST303=row['CST303'],
                            CST305=row['CST305'],
                            CST307=row['CST307'],
                            CST309=row['CST309'],
                            CSL331=row['CSL331'],
                            CSL333=row['CSL333'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                elif sem == 6:
                    for index, row in df.iterrows():
                        data = Sem6(
                            RegNo=row['RegNo'],
                            Name=row['Name'],
                            CST302=row['CST302'],
                            CST304=row['CST304'],
                            CST306=row['CST306'],
                            CST322=row['CST322'],
                            CST332=row['CST332'],
                            HUT200=row['HUT200'],
                            CST308=row['CST308'],
                            CSL332=row['CSL332'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                elif sem == 7:
                    for index, row in df.iterrows():
                        data = Sem7(
                            RegNo=row['RegNo'],
                            Name=row['Name'],
                            CST401=row['CST401'],
                            CST423=row['CST423'],
                            CST433=row['CST433'],
                            MCN401=row['MCN401'],
                            CSL411=row['CSL411'],
                            CSQ413=row['CSQ413'],
                            CSD415=row['CSD415'],
                            CST455=row['CST455'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                elif sem == 8:
                    for index, row in df.iterrows():
                        data = Sem8(
                            RegNo=row['RegNo'],
                            Name=row['Name'],
                            CST402=row['CST402'],
                            CST434=row['CST434'],
                            CST414=row['CST414'],
                            CST466=row['CST466'],
                            CST416=row['CST416'],
                            CST428=row['CST428'],
                            CST448=row['CST448'],
                            CST404=row['CST404'],
                            CSD416=row['CSD416'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                else:
                    print(
                        f"\n\nWarning exited without entering if\n\n {sem=} \n\n")

                flash('CSV file uploaded successfully!', 'success')

            except Exception as e:
                flash(f'Error: {str(e)}', 'error')

            # return redirect(url_for('/teacher/uploads'))
            return redirect(url_for('TeacherViews.upload_csv'))
            # return redirect(url_for('index'))

        flash('Invalid file format. Only CSV files are allowed!', 'error')
        return redirect(request.url)

    return render_template("/teacher/teacher_upload.html", SectionHeader="Uploads")


def filter_students(count: int, sem: int, Grade: str):

    sem = int(sem)
    if sem == 1:
        all_students = Sem1.query.all()
    elif sem == 2:
        all_students = Sem2.query.all()
    elif sem == 3:
        all_students = Sem3.query.all()
    elif sem == 4:
        all_students = Sem4.query.all()
    elif sem == 5:
        all_students = Sem5.query.all()
    elif sem == 6:
        all_students = Sem6.query.all()
    elif sem == 7:
        all_students = Sem7.query.all()
    elif sem == 8:
        all_students = Sem8.query.all()
    # all_students = sem.query.all()

    # all_students = Sem4.query.all()
    students_f_grade = []

    for student in all_students:
        if sem == 1:
            subjects = [
                student.MAT206, student.CST202,
                student.CST204, student.CST206,
                student.EST200, student.MCN202,
                student.CSL202, student.CSL204
            ]
        elif sem == 2:
            subjects = [
                student.EST120, student.CYT100,
                student.EST110, student.MAT102,
                student.EST102, student.HUN102,
                student.CYL120, student.ESL120,
                student.ESL102
            ]

        elif sem == 3:
            subjects = [
                student.MAT203, student.CST201,
                student.CST203, student.CST205,
                student.HUT200, student.MCN201,
                student.CSL201, student.CSL203
            ]

        elif sem == 4:
            subjects = [
                student.MAT206, student.CST202,
                student.CST204, student.CST206,
                student.EST200, student.MCN202,
                student.CSL202, student.CSL204
            ]

        elif sem == 5:
            subjects = [
                student.MCN301, student.CST301,
                student.CST303, student.CST305,
                student.CST307, student.CST309,
                student.CSL331, student.CSL333
            ]

        elif sem == 6:
            subjects = [
                student.CST302, student.CST304,
                student.CST306, student.CST332,
                student.CST322, student.HUT300,
                student.CST308, student.CSL332
            ]

        elif sem == 7:
            subjects = [
                student.CST401, student.CST423,
                student.CST433, student.MCN401,
                student.CSL411, student.CSQ413,
                student.CSD415, student.CST455
            ]

        elif sem == 8:
            subjects = [
                student.CST402, student.CST434,
                student.CST414, student.CST466,
                student.CST416, student.CST428,
                student.CST448, student.CST404,
                student.CSD416
            ]

        f_count = subjects.count(Grade)

        if f_count == count:
            students_f_grade.append(student)

    return students_f_grade


@TeacherViews.route("/filter_by_grade", methods=['GET', 'POST'])
def filter_by_grade():

    sem = ''
    if request.method == 'POST':

        sem = request.form.get('sem')
        Selct_value = request.form.get('Select_value')
        grade = request.form.get('grade')

        if Selct_value == "1":
            students = filter_students(count=1, sem=sem)
            return render_template('teacher/teacher_filter_by.html', students=students, sem=sem)

        elif Selct_value == "2":
            students = filter_students(count=2, sem=sem)
            return render_template('teacher/teacher_filter_by.html', students=students, sem=sem)

        elif Selct_value == "3":
            students = filter_students(count=3, sem=sem)
            return render_template('teacher/teacher_filter_by.html', students=students, sem=sem)

        elif Selct_value == "4":
            students = filter_students(count=4)
            return render_template('teacher/teacher_filter_by.html', students=students, sem=sem)

        elif Selct_value == "5":
            students = filter_students(count=5, sem=sem)
            return render_template('teacher/teacher_filter_by.html', students=students, sem=sem)
        elif Selct_value == "5":
            students = filter_students(count=5, sem=sem)
            return render_template('teacher/teacher_filter_by.html', students=students, sem=sem)
        else:
            students = filter_students(count=2, sem=sem, Grade=Selct_value)
            return render_template('teacher/teacher_filter_by.html', students=students, sem=sem)

    return render_template('teacher/teacher_filter_by.html', sem = sem)


@TeacherViews.route("/view_grade")
def view_grade():
    sem = ''
    return render_template('teacher/teacher_view_grade.html', SectionHeader="List", sem=sem)
