from flask import Blueprint, render_template, request, redirect, jsonify
import pandas as pd
from ..models import Subject, semister, Result
from .. import db
import json

TeacherViews = Blueprint("TeacherViews", __name__)


@TeacherViews.route("/")
def home():
    return "<H1>This a Teacher Homepage</H1>"


@TeacherViews.route("/filter_by")
def filter_by():
    return "<H1>This a Teacher filter_by page</H1>"


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

        sem = request.form.get('Sem')
        batch = request.form.get('Batch')
        file = request.files['file']

        if file.filename == '':
            flash('No file selected!', 'error')
            return redirect(request.url)

        if file and file.filename.endswith('.csv'):
            try:
                # Read the CSV data and store it in the database
                df = pd.read_csv(file)

                if sem == 1:
                    for index, row in df.iterrows():
                        data = Sem1(
                            RegNo=row['RegNo'], Name=row['Name'],
                            MAT206=row['MAT206'],
                            CST202=row['CST202'],
                            CST204=row['CST204'],
                            CST206=row['CST206'],
                            EST200=row['EST200'],
                            MCN202=row['MCN202'],
                            CSL202=row['CSL202'],
                            CSL204=row['CSL204'],
                            Earned_Credits=row['Earned_Credits'],
                            Cumilative_Credits=row['Cumilative_Credits'],
                            SGPA=row['SGPA'],
                            CGPA=row['CGPA']
                        )
                        db.session.add(data)
                        db.session.commit()

                elif sem == 2:
                    pass
                elif sem == 3:
                    pass

                # Add the other semmisters here

                elif sem == 8:
                    pass

                flash('CSV file uploaded successfully!', 'success')

            except Exception as e:
                flash(f'Error: {str(e)}', 'error')

            return redirect(url_for('/teacher/upload'))

        flash('Invalid file format. Only CSV files are allowed!', 'error')
        return redirect(request.url)

    return render_template("/teacher/teacher_upload.html")
